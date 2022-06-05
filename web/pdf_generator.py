from fpdf import FPDF ,HTMLMixin
import subprocess
import re
from pathlib import Path


# from soild import settings
class PDF(FPDF, HTMLMixin):
    pass

class settings:
    MEDIA_ROOT = Path(__file__).resolve().parent
    BASE_DIR = Path(__file__).resolve().parent

def running(name,data_question ):
    namex = str(name).replace(".sol",".pdf")
    fw = PDF()
    fw.add_page()
    fw.set_font("Arial",size=10)
    for k,v in data_question.items():
        fw.multi_cell(w=0,h=7,ln=1,txt=str(k)+":"+str(v)+"\n")
    fw.multi_cell(w=0,h=7,ln=1,txt="#"*30+"\n")
    p = subprocess.getoutput(f"slither {'./files/'+name}   --print human-summary --solc-disable-warnings")
    global data
    data = []
    def changer(line):
        if len(line) > 0 and line[0] == "+":
            return False
        if len(line) > 0 and line[0] == "|":
            #print(line)
            data.append( list(line.split("|")[1:-1]))
            return False
        return line
    for i in p.split("\n"):
        reg = re.sub(r'\x1b\[[0-9]*m',"",i)
        reg = changer(reg)
        if  reg :
            print("#reg is",reg)
            fw.multi_cell(w=0,h=7,ln=1,txt=reg+"\n")
    #print(data)
    def table(text):
        return '''<table width="100%" border="1">'''+text+''''</table>'''
    def head(text):
        return '<thead>'+text+'</thead>'
    def body(text):
        return '<tbody>'+text+'</tbody>'

    html = ''
    part_html = ''
    for idx,i in enumerate(data):
#        print(i)
        part= ""
        if idx ==0 :
            part +="<tr>"
            for p in i :
                part += "<th width='15%' >"+p+"</th>"
            part +="</tr>"
            html += head(part)
        else:
            part += "<tr>"
            for p in i :
                part += "<th >"+p+"</th>"
            part += "</tr>"
            part_html += part
    html += body(part_html)
    html = table(html)


    fw.write_html(html)
    fw.add_page()
    fw.set_text_color(0,0,0)
    ################################
    p2 = subprocess.getoutput(f"slither  {'./files/'+name} --print contract-summary --solc-disable-warnings")
    for pp2 in p2.split("\n"):
        reg = re.sub(r'\x1b\[[0-9]*m',"",pp2)
        fw.multi_cell(w=0,h=7,ln=1,txt=reg+"\n")
    ####################################
    fw.add_page()
    data = []
    html = ''
    part_html = ''
    table_end = 0
    p3 = subprocess.getoutput(f"slither  {'./files/'+name} --print vars-and-auth --solc-disable-warnings")
    for i3 in p3.split("\n"):
        reg = re.sub(r'\x1b\[[0-9]*m',"",i3)
        if len(reg) >0  and reg[0] == "+" and table_end ==0 :
  #          print("table set to 1")
            table_end = 1

        if len(reg) > 0 and table_end:
   #         print("inside if")
            if reg[0] not in ["|","+"]:
                fw.set_font_size(7)
                for idx,i in enumerate(data):
                    # print(i)
                    part= ""
                    if idx ==0 :
                        part +="<tr>"
                        for pid , p in enumerate(i) :
                            if pid == 1:
                                part += "<th width='60%' >"+p+"</th>"
                            else:
                                part += "<th width='20%' >"+p+"</th>"

                        part +="</tr>"
                        html += head(part)
                    else:
                        part += "<tr>"
                        for p in i :
                            part += "<th >"+p+"</th>"
                        part += "</tr>"
                        part_html += part
                html += body(part_html)
                html = table(html)
                fw.write_html(html)
                html = ''
                part_html = ''
                table_end = 0
        reg = changer(reg)
        if  reg :
            fw.set_font_size(10)
            fw.multi_cell(w=0,h=7,ln=1,txt=reg+"\n")

    # part_html = body(part_html)
    html += body(part_html)
    html = table(html)
    fw.write_html(html)
    settings.BASE_DIR
#####################################################################
    fw.add_page()
    data = []
    html = ''
    part_html = ''
    table_end = 0
    plus_len = 0
    p4 = subprocess.getoutput(f"slither  {'./files/'+name} --print function-summary --solc-disable-warnings")
    p4 = p4.split("\n")
    for idd,i4 in enumerate(p4):
        reg = re.sub(r'\x1b\[[0-9]*m',"",i4)
        if len(reg) > 0  and reg[0] == "+" and table_end ==0 :
            plus_len = reg.count("+")-1
            #print("table set to 1")
            table_end = 1
        if len(reg) >= 0  and table_end:
        
            if reg[0] == "+" and len(p4[idd+1]) ==0 :
                fw.set_font_size(7)
                if len(data) ==1 :
                    data.append(['#' for _ in data[0]])
                for idx,i in enumerate(data):
                
                    part= ""
                    if idx ==0 :
                        part +="<tr>"
                        for pid , p in enumerate(i) :
                            if pid in [0,6]:
                                part += f"<th width='25%' >"+p+"</th>"
                            else:
                                part += f"<th width='10%' >"+p+"</th>"
                        part +="</tr>"
                        html += head(part)
                    else:
                        part += "<tr>"
                        for p in i :
                            part += "<th >"+p+"</th>"
                        part += "</tr>"
                        part_html += part
                html += body(part_html)
                html = table(html)
                fw.write_html(html)
                data= []
                html = ''
                part_html = ''
                table_end = 0
        reg = changer(reg)
        if  reg :
            fw.set_font_size(10)
            fw.multi_cell(w=0,h=7,ln=1,txt=reg+"\n")
#########################################################################
    
###################################################################
    # part_html = body(part_html)
    html += body(part_html)
    html = table(html)
    fw.write_html(html)
    #settings.BASE_DIR
    #################################
    fw.output(f"{settings.MEDIA_ROOT / namex}")
    return True
from html_generator import DataExtractor
# running("fady-1652350000.sol",{"name":"fady","version":3.2})
data = DataExtractor("fady-1652350000.sol",{"name":"fady","version":3.2})
data.get_human_summary_data()
data.get_contract_summary()
data.get_vars_auth()
# data.get_function()
data.save()