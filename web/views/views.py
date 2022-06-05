from django.http import Http404 
from django.shortcuts import redirect, render

from web.forms import  UploadForm 
from django.http.response import HttpResponse
from web.models import Profile , Analysis , AnaysisStatus
from django.core.files.storage import FileSystemStorage
from datetime import datetime
from django.core.exceptions import PermissionDenied 
from django.contrib.auth.decorators import login_required
# Create your views here.
from web.task import switch
from soild import settings

from django.urls import reverse
from paypal.standard.forms import PayPalPaymentsForm
import mimetypes

def check_permission(ouser , ruser):
    if ouser != ruser :
        raise PermissionDenied()

def index(request):
    user= request.user
    if request.user.is_authenticated :
        expire=Profile.objects.get(user=user).due_date
        return render(request,"index.html",context={"user":user,"expire":expire})
    return render(request,"nindex.html")

@login_required(login_url="/login")
def download_file(request, filename=''):
    if filename != '':
        obj = Analysis.objects.get(file__contains=filename)
        check_permission(request.user,obj.user)
        # Define Django project base directory
        BASE_DIR = settings.MEDIA_ROOT
        # Define the full file path
        # print()
        filename = str(obj.file).replace(".sol",".pdf")
        filepath = BASE_DIR  / filename
        # Open the file for reading content
        path = open(filepath, 'rb')
        # Set the mime type
        mime_type, _ = mimetypes.guess_type(filepath)
        # Set the return value of the HttpResponse
        response = HttpResponse(path, content_type=mime_type)
        # Set the HTTP header for sending to browser
        response['Content-Disposition'] = "attachment; filename=%s" % filename
        # Return the response value
        return response
    else:
        raise Http404


@login_required(login_url="/login")
def view_download(request,oid):
    user = request.user
    expire=Profile.objects.get(user=user).due_date
    obj = Analysis.objects.get(id=oid)
    check_permission(obj.user,request.user)

    filename = str(obj.file).replace(".sol","")
    html_out = str(obj.file).replace(".sol",".html")
    html_data = []
    out_length = 0
    BASE_DIR = settings.MEDIA_ROOT
    with open( BASE_DIR  / html_out , "r+" ) as pp :
        for line in pp.readlines():
            out = line.split("<brspace>")
            out_length = len(out)
            html_data.append(out[0])
            html_data.append(out[1])
            html_data.append(out[2])
            html_data.append(out[3])
    context = {"file_name":filename,"data":obj,"user":user,
                    "expire":expire,"html_out1":html_data[0],
                     "html_out2":html_data[1],"html_out3":html_data[2],"html_out4":html_data[3], "length" : out_length}
    return render(request, 'files.html',context=context)


@login_required(login_url="/login")
def upload(request):
    u = request.user
    user = Profile.objects.get(user=u)
    ############# check If user Premium ###################
    curr = datetime.date(datetime.now())
    if not user.due_date or user.due_date <  curr :
        user.permium = 0
        user.save()
        return redirect("/payment")
    #######################################################

    form = UploadForm()
    if request.method == "GET":
        return render(request,"upload.html",context={"form":form,"user":u,"expire":user.due_date})
    file = request.FILES['file']
    data = request.POST
    ########################Validate Data##########################
    if not data['address'].startswith("0x") :
        context = {"err":"address should start with 0x","form":form}
        return render(request,"upload.html",context=context)
    if not file.name[-4:] == ".sol" :
        context = {"err":"enter correct Contract file","form":form}
        return render(request,"upload.html",context=context)
    ##############################################################

    fs = FileSystemStorage()
    filename =str(request.user.username)+"-"+str(int(datetime.now().timestamp()))+".sol"
    filename = fs.save(filename,file)
    obj = Analysis.objects.create(status=AnaysisStatus.PENDING,file=filename,user=u,data=\
    {"project":data['project'],"address":data['address'],\
        "version":data['version'],"blockchain":data['blockchain']}\
        )
    context = {"success":"file uploaded successfully.","form":form,"user":u,"expire":user.due_date}

    ############# Start Background Job ######################
    switch.apply_async((filename,data['version'],obj.id))
    #########################################################
    return render(request,"upload.html",context=context)

@login_required(login_url="/login")
def list_uploads(request):
    user = request.user
    expire=Profile.objects.get(user=user).due_date
    data = Analysis.objects.filter(user=user)\
    .order_by("-created_at")\
        .only("id","data","status","created_at")\
            .all()
    data = [data[i:i+3] for i in range(0,len(data),3)]
    return render(request,"lists.html",context={"data":data,"user":user,"expire":expire})



@login_required(login_url="/login")
def upgrade(request):
    user= request.user
    expire=Profile.objects.get(user=user).due_date

    form = PayPalPaymentsForm(initial={'item_name':'1 Month subscribe','business':settings.BEMAIL,\
        "currency_code":"USD","amount":settings.AMOUNT,\
                "invoice":f'{request.user.id}-{int(datetime.timestamp(datetime.now()))}',
                "notify_url":request.build_absolute_uri(reverse('paypal-ipn')) ,#  'https://f927-197-63-238-246.ngrok.io/paypal/', #TODO 
            "return_url": request.build_absolute_uri(reverse('paypal-return')),
            "cancel_return": request.build_absolute_uri(reverse('paypal-cancel')),
            "lc": 'EN',
            "no_shipping": '1', 

        },button_type="subscribe").render()
    return render(request,"payment.html",context={"form":form,"user":user,"expire":expire,"amount":settings.AMOUNT})
