from celery import shared_task
import subprocess
import re
from web.models import AnaysisStatus
from web.pdf_generator import running
from web.utils import get_object ,  version_installed , switch_current_verison

@shared_task
def switch(filename,ver,oid):
    x = get_object(oid)
    if not version_installed(ver):
        subprocess.getoutput(f"solc-select install {ver}")
    if switch_current_verison(ver): 
        try:
            print("enter test work")
            output = subprocess.check_output(
        f"slither {'./files/'+filename} ", stderr=subprocess.STDOUT, shell=True, timeout=120,
        universal_newlines=True)
        except subprocess.CalledProcessError as exc:
            print("[*] error code  ",exc.returncode)
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

        stat = running(filename,data=x.data)
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
