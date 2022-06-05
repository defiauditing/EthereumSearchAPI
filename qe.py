

from fpdf import FPDF ,HTMLMixin
import subprocess
import re
from soild import settings
class PDF(FPDF, HTMLMixin):
    pass



fw = PDF()
fw.add_page()
fw.set_font("Arial",size=10)
def table(text):
    return '''<table width="100%" border="1">'''+text+''''</table>'''
def head(text):
    return '<thead>'+text+'</thead>'
def body(text):
    return '<tbody>'+text+'</tbody>'


def changer(line):
    if len(line) > 0 and line[0] == "+":
        return False
    if len(line) > 0 and line[0] == "|":
        #print(line)
        data.append( list(line.split("|")[1:-1]))
        return False
    return line
data = []
