import requests
from fpdf import FPDF ,HTMLMixin
from requests.auth import HTTPBasicAuth
headers = {
"Content-Type": "application/json",
"Authorization":"Bearer A21AAIaGL2TrmXxYWKXhslquPjatiYmn-iAyg1NL6y0i75GWwPdb0EUUoiJBxPKVr3yYpIRTXEmh7fXXPgydgZnXbph2LXoQg"
}
data= {"grant_type":"client_credentials"}
# req = requests.get("https://api-m.sandbox.paypal.com/v1/reporting/balances",headers=headers)
# req = requests.post("https://api-m.sandbox.paypal.com/v1/oauth2/token",auth=HTTPBasicAuth('AcKZJkmCcErA0bnpRbj4e2btKvuu4YewQkW__naXDEvMBA6uNf08-5rtFP9qkIO8Py2q5foxxCjsQ5Gb'\
#    ,'EKkDYtuOMkEf3CFwEbrspg9oW29C8fcXsYcT12d1ezpfTqy5JJQdzyUQrgIak7l1k44GN__kaPOU9kHJ'),headers=headers,data=data)
# print(req.text)
'''
A21AAIaGL2TrmXxYWKXhslquPjatiYmn-iAyg1NL6y0i75GWwPdb0EUUoiJBxPKVr3yYpIRTXEmh7fXXPgydgZnXbph2LXoQg
'''
'''
AcKZJkmCcErA0bnpRbj4e2btKvuu4YewQkW__naXDEvMBA6uNf08-5rtFP9qkIO8Py2q5foxxCjsQ5Gb
EKkDYtuOMkEf3CFwEbrspg9oW29C8fcXsYcT12d1ezpfTqy5JJQdzyUQrgIak7l1k44GN__kaPOU9kHJ
curl -v -X POST "https://api-m.sandbox.paypal.com/v1/oauth2/token" \
    -u "<CLIENT_ID>:<CLIENT_SECRET>" \
    -H "Content-Type: application/x-www-form-urlencoded" \
    -d "grant_type=client_credentials"  


'''
import subprocess
import re
p = subprocess.getoutput("slither fady.sol --print human-summary")
import subprocess
try:
    output = subprocess.check_output(
        "slither aa.pdf", stderr=subprocess.STDOUT, shell=True, timeout=3,
        universal_newlines=True)
except subprocess.CalledProcessError as exc:
    print("Status : FAIL", exc.returncode, exc.output)

# print("##############################")
# from reportlab.pdfgen.canvas import Canvas
# from reportlab.platypus.tables import Table , colors , TableStyle
# c = Canvas("test.pdf",bottomup=0)
# y = 9
# c.setLineWidth(0.1)
# c.setFont(size=9,psfontname='Helvetica')
# def pluser(line):
#     try:
#         if line[0] == "+":
#             line =str(line).replace("+-","+--",1)
#     except:
#         pass
#     return line

# def linee(line):
#     try :
#         if line[0] =="|":
#             c.setFont(size=7.3,psfontname='Helvetica')
#     except:
#         pass

# def changer(line):
#     if len(line) > 0 and line[0] == "|":
#         line = line.replace("Complex code","Complex co.")
#         line = line.replace("Name","#Name.")
#         line = line.replace("functions","functions  ")
#         line = line.replace(" ERC20 info","ERC20 info")
#         line = line.replace(" ERCS","ERCS")
#         if str(line).find("#Name") == -1 :
#             linex = line
#             line = []
#             dic = {"1":13,"2":20,"3":10,"4":20,"5":19,"6":17}
#             for idx,i in enumerate(linex.split("|")):
#                 try:
#                     wides = dic[str(idx)]
#                     if len(i) > wides :
#                         print("not appeending")
#                         line.append(i[:wides])
#                     else:
#                         print("appending")
#                         # print(f"{i:^18s} #")
#                         # line.append(f"{i:^18s}")
#                         line.append("{i:<{width}}".format(  i=i,width=wides  )  )
#                 except:
#                     print("error")
#                     line.append(i)
#             line = "|".join(line)
#     return line

# # for i in p.split("\n"):
#     # reg = re.sub(r'\x1b\[[0-9]*m',"",i)
#     # linee(reg)
#     # reg = pluser(reg)
#     # reg = changer(reg)
#     # c.drawString(0,y,reg)
#     # c.setFont(size=9,psfontname='Helvetica')
#     # print(reg)
#     # y += 9
# # 
# ts = [
#     #header style    
#     ('GRID', (0,0), (-1,-1), 1,colors.gray),
# ]
# ts = TableStyle([
# ('TOPPADDING', (0,0), (-1,-1), 0.25, colors.black),
# ])

# data = [
#     ["a","a","a"],
#     ["a","a","a"]


# ]
# f = Table(data)#,style=ts)
# f.setStyle(TableStyle([('ALIGN',(1,1),(-2,-2),'RIGHT'),
#  ('TEXTCOLOR',(1,1),(-2,-2),colors.red),
#  ('VALIGN',(0,0),(0,-1),'TOP'),
#  ('TEXTCOLOR',(0,0),(0,-1),colors.blue),
#  ('ALIGN',(0,-1),(-1,-1),'CENTER'),
#  ('VALIGN',(0,-1),(-1,-1),'MIDDLE'),
#  ('TEXTCOLOR',(0,-1),(-1,-1),colors.green),
#  ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
#  ('BOX', (0,0), (-1,-1), 0.25, colors.black),
#  ]))

# f.wrapOn(c,500,200)
# f.drawOn(c,30,30)
# c.save()


# class PDF(FPDF, HTMLMixin):
#     pass

# fw = PDF()
# fw.add_page()
# fw.set_font("Arial",size=10)
# # fw.set_font_size(16)

# # f.set_font("Helvetica",size=10)
# # line_height = f.font_size * 2.5
# col_width = 2
# def table(text):
#     return '''<table width="100%" border="1">'''+text+''''</table>'''
# def head(text):
#     return '<thead>'+text+'</thead>'
# def body(text):
#     return '<tbody>'+text+'</tbody>'

# html = ''
# part_html = ''
# for idx,i in enumerate(data):
#     part= ""
#     if idx ==1 :
#         part +="<tr>"
#         for p in i :
#             part += "<th width='33%'>"+p+"</th>"
#         part +="</tr>"
#         html += head(part)
#     else:
#         part += "<tr>"
#         for p in i :
#             part += "<th >"+p+"</th>"
#         part += "</tr>"
#         part_html += part
# # part_html = body(part_html)
# html += body(part_html)
# html = table(html)
# print(html)
# fw.set_text_color(200,150,120)
# fw.write(txt="hello sir")
# fw.set_text_color(100,250,20)

# fw.write_html(html)
# fw.output("hello2.pdf")


