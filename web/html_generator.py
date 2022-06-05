
from fpdf import FPDF ,HTMLMixin
import subprocess
import re
from pathlib import Path
from soild import settings

def subprocess_human_summary(name):
    return subprocess.getoutput(f"slither {'./files/'+name}   --print human-summary --solc-disable-warnings")
     
def subprocess_vars_auth(name):
    return subprocess.getoutput(f"slither  {'./files/'+name} --print vars-and-auth --solc-disable-warnings")


def table(text):

    table = '''<table class="table" width="100%" border="1">'''+text+''''</table>'''
    
    return table
def head(text):
    return '<thead>'+text+'</thead>'
def body(text):
    return '<tbody>'+text+'</tbody>'

class HTMLDataExtractor:
    def __init__(self,name ,data_question):
        self.name = name
        self.data_question = data_question
        self.namex = str(name).replace(".sol",".pdf")
        self.data = []
        self.fw = open(f"{settings.MEDIA_ROOT / self.namex}","w+")


    def changer(self,line):
        if len(line) > 0 and line[0] == "+":
            return False
        if len(line) > 0 and line[0] == "|":
            #print(line)
            self.data.append( list(line.split("|")[1:-1]))
            return False
        return line


    def get_human_summary_data(self):
        self.data = []

        p = subprocess_human_summary(self.name)
        for i in p.split("\n"):
            reg = re.sub(r'\x1b\[[0-9]*m',"",i)
            reg = self.changer(reg)
            if reg :
                self.fw.write(f'<div>{reg}</div><br>')

        html = ""
        part_html = ""
        for idx,i in enumerate(self.data):
            part= ""
            if idx ==0 :
                part +="<tr>"
                for p in i :
                    part += "<th  scope='col' width='15%' >"+p+"</th>"
                part +="</tr>"
                html += head(part)
            else:
                part += "<tr>"
                for p in i :
                    part += "<th scope='row' >"+p+"</th>"
                part += "</tr>"
                part_html += part
        html += body(part_html)
        html = table(html)
        self.fw.write(html+"<br>")
        # self.fw.write_html(html)
        # self.fw.add_page()

    def get_contract_summary(self):
        self.data = []
        p = subprocess.getoutput(f"slither  {'./files/'+self.name} --print contract-summary --solc-disable-warnings")
        for pp2 in p.split("\n"):
            reg = re.sub(r'\x1b\[[0-9]*m',"",pp2)
            self.fw.write(f'<div>{reg}</div><br>')
        # self.fw.add_page()

    def get_vars_auth(self):
        self.data = []
        html = ''
        part_html = ''
        table_end = 0
        p3 = subprocess.getoutput(f"slither  {'./files/'+self.name} --print vars-and-auth --solc-disable-warnings")
        for i3 in p3.split("\n"):
            reg = re.sub(r'\x1b\[[0-9]*m',"",i3)
            if len(reg) >0  and reg[0] == "+" and table_end ==0 :
  #              print("table set to 1")
                table_end = 1

            if len(reg) > 0 and table_end:
   #             print("inside if")
                if reg[0] not in ["|","+"]:
                    for idx,i in enumerate(self.data):
                        # print(i)
                        part= ""
                        if idx ==0 :
                            part +="<tr>"
                            for pid , p in enumerate(i) :
                                if pid == 1:
                                    part += "<th scope='col' width='60%' >"+p+"</th>"
                                else:
                                    part += "<th scope='col' width='20%' >"+p+"</th>"

                            part +="</tr>"
                            html += head(part)
                        else:
                            part += "<tr>"
                            for p in i :
                                part += "<th scope='row' >"+p+"</th>"
                            part += "</tr>"
                            part_html += part
                    html += body(part_html)
                    html = table(html)
                    self.fw.write(html)
                    html = ''
                    part_html = ''
                    table_end = 0
            reg = self.changer(reg)
            if  reg :
                self.fw.write(f'<div>{reg}</div><br>')

        html += body(part_html)
        html = table(html)
        self.fw.write(html)

    def get_function(self):
        self.data = []
        html = ''
        part_html = ''
        table_end = 0
        plus_len = 0
        p4 = subprocess.getoutput(f"slither  {'./files/'+self.name} --print function-summary --solc-disable-warnings")
        p4 = p4.split("\n")
        for idd,i4 in enumerate(p4):
            reg = re.sub(r'\x1b\[[0-9]*m',"",i4)
            if len(reg) > 0  and reg[0] == "+" and table_end == 0 :
                plus_len = reg.count("+") - 1
                table_end = 1
            if len(reg) >= 0  and table_end:
                
                if reg[0] == "+" and len(p4[idd+1]) == 0 :
                    if len(self.data) ==1 :
                        self.data.append(['#' for _ in self.data[0]])
                    for idx,i in enumerate(self.data):
                    
                        part= ""
                        if idx ==0 :
                            part +="<tr>"
                            for pid , p in enumerate(i) :
                                if pid in [0,6]:
                                    part += f"<th scope='col' width='25%' >"+p+"</th>"
                                else:
                                    part += f"<th scope='col' width='10%' >"+p+"</th>"
                            part +="</tr>"
                            html += head(part)
                        else:
                            part += "<tr>"
                            for p in i :
                                part += "<th scope='row' >"+p+"</th>"
                            part += "</tr>"
                            part_html += part
                    html += body(part_html)
                    html = table(html)
                    self.fw.write(html)
                    self.data= []
                    html = ''
                    part_html = ''
                    table_end = 0
            reg = self.changer(reg)
            if  reg :
                self.fw.write(f'<div>{reg}</div><br>')

    def save(self):
 
        self.fw.close()
