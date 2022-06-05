from celery import shared_task
import subprocess
import re
from web.models import AnaysisStatus
from web.data_extracts import running
from web.utils import get_object ,  version_installed , switch_current_verison
from web.pdf_generator import PDFDataExtractor
from web.html_generator import HTMLDataExtractor
def run_pdf(name,question):
    data = PDFDataExtractor(name,question)
    data.get_human_summary_data()
    data.get_contract_summary()
    data.get_vars_auth()
    data.get_function()
    data.save()
    return True

def run_html(name,question):
    data = HTMLDataExtractor(name,question)
    data.get_human_summary_data()
    data.get_contract_summary()
    data.get_vars_auth()
    data.get_function()
    data.save()
    return True

@shared_task
def switch(filename,ver,oid):
    x = get_object(oid)
    if not version_installed(ver):
        subprocess.getoutput(f"solc-select install {ver}")
    if switch_current_verison(ver): 
        try:
            print("enter test work")
            print(filename)
            output = subprocess.check_output(
        f"slither {'./files/'+filename} ", stderr=subprocess.STDOUT, shell=True, timeout=120,
        universal_newlines=True)
        except subprocess.CalledProcessError as exc:
            print(exc)
            print("[*] error code Unknown  ",exc.returncode)
            if str(exc.returncode) not in ["8","59"] :
                stdout = exc.output 
                li = re.findall(r'(/[\w\s\-\./]*)',stdout)
                li_fun = lambda x: "/".join(x.split("/")[:-1])
                for i in li :
                    stdout = stdout.replace(li_fun(i),"/docker_executor")
                x.stdout = stdout 
                x.status = AnaysisStatus.FAILED
                x.save()
                return True 
        try:
            stat = run_pdf(filename,x.data)
            stat = run_html(filename,x.data)
        except : 
             stat = 0

        if stat :
            x.status = AnaysisStatus.COMPLETED
            x.save()
        else : 
            x.status = AnaysisStatus.FAILED
        x.save()
    else :
        x.status = AnaysisStatus.FAILED
        x.save()
    return True
