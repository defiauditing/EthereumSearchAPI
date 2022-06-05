from fabric import Connection 
from pathlib import Path
import glob
x = glob.glob("*.html",root_dir="./web/templates")
print(x)
c = Connection("34.125.213.99", port=22, user="fady", connect_kwargs={'look_for_keys': False,'key_filename':'priv'})
for i in x:
    c.put(f"./web/templates/{i}",f"/home/fady/soild/web/templates/{i}")
res = c.run("sudo service uwsgi restart")
res = c.run("sudo service nginx restart")
print("Done")
