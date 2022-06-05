from django.shortcuts import redirect, render
from web.forms import LoginForm ,RegisterForm
from web.models import User 
from django.contrib.auth import authenticate , login ,logout
from django.contrib.auth.decorators import login_required


def register(request):

    if request.user.is_authenticated:
        return redirect("/")
    form = RegisterForm()
    if request.method == "GET":
        return render(request,"register.html",context={"form":form})
    try:
        data = request.POST
        print(data['password'])
        if len(data['password']) < 8 :
            return render(request,"register.html",context={"form":form,"err":"password should be at least 8 characthers"})
        if data['password'] != data['password2']:
            return render(request,"register.html",context={"form":form,"err":"password doesn't match "})
        if User.objects.filter(username=data['username']).exists():
            return render(request,"register.html",context={"form":form,"err":"username already exists"})
        data = dict(data)
        data.pop("csrfmiddlewaretoken")
        data.pop("password2")
        User.objects.create_user(**{k:v[0] for k,v in data.items()})
    except Exception as e:

        return render(request,"register.html",context={"form":form,"err":str(e)})
    return render(request,"register.html",context={"form":form,"success":"Account created successfully, Redirecting"})


def login_page(request):

    if request.user.is_authenticated:
        return redirect("/")
    form = LoginForm()     
    if request.method == "GET":
        return render(request,"login.html",context={"form":form})
    data = request.POST
    print(data)
    username = data["username"]
    password = data["password"]
    print(username)
    user = authenticate(request,username = username, password = password)
    if user:
        login(request,user=user)
        return redirect("/")
    else:
        return render(request,"login.html",context={"form":form,"err":"Invaild username/password"})

@login_required(login_url="/login")
def log_out(request):
    logout(request)
    return redirect("/login")