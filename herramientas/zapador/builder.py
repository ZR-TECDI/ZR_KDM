import subprocess
import os
import sys
import shutil

dir_script = os.path.dirname(os.path.realpath(sys.argv[0]))

def proceso(weaita):
    proc = subprocess.Popen('pyinstaller '+weaita , shell=True)
    proc.wait()

def build_all():
    zapadorexe = "main.py --name zapador --onefile --uac-admin -i "+dir_script+"/zapador.ico"
    autoupdateexe = "auto_update.py --onefile --uac-admin"

    proceso(zapadorexe)
    proceso(autoupdateexe)

if __name__ == "__main__":
    build_all()
    shutil.move(dir_script+'/dist/zapador.exe', dir_script)
    shutil.move(dir_script+'/dist/auto_update.exe', dir_script)