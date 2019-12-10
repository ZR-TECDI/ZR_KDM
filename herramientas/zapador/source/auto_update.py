import os
import time
import sys
import urllib.request
from subprocess import Popen, CREATE_NEW_CONSOLE
import json

dir_script = os.path.dirname(os.path.realpath(sys.argv[0]))

try:
    with open(dir_script + '/zapador_config.json') as f:
        CONFIG_DICT = json.load(f)
    branch = CONFIG_DICT['branch']

except Exception as e:
    print(str(e))

url = "https://github.com/ZR-TECDI/ZR_KDM/raw/{}/herramientas/zapador/zapador.exe".format(branch)
#Espero un segundo pa que se haya cerrado el otro programa
time.sleep(0.3)

try:
    ultimo_estable = urllib.request.urlretrieve(url, dir_script+'/zapador.exe')
except Exception as e:
    print('No se pudo descargar la última versión de Zapador')
    print(str(e))
else:
    print('Última versión descargada con éxito')
finally:
    os.system('pause')
    Popen(dir_script+'/zapador.exe', creationflags=CREATE_NEW_CONSOLE)
    quit()
