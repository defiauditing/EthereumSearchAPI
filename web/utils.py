import subprocess
from web.models import AnaysisStatus , Analysis
def version_installed(v):
    versions = subprocess.getoutput(f"solc-select versions").split("\n")
    for i in versions:
        if v in i :
            return True
    return False

def switch_current_verison(v):
    print("try Switch")
    out = subprocess.getoutput(f"solc-select use {v}")
    if "Switched" in out:
        print("Switched")
        return True

    
    return False

def change_object_status(o):
    o.status = AnaysisStatus.COMPLETED
    o.save()
    return o

def get_object(oid):
    obj = Analysis.objects.get(id=oid)
    return obj
