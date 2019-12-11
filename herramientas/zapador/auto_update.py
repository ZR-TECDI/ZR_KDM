import zapador.constantes as cons
from json import load
from requests import get
from tqdm import tqdm
from os import system
from os.path import isfile, isdir
from zipfile import ZipFile
from os import remove
from shutil import rmtree

with open(cons.SETTINGS_FILE, 'r', encoding='UTF-8') as f:
    cons.SETTINGS_ACTUALES = load(f)

url = cons.ZAPADOR_PAQUETE.format(cons.SETTINGS_ACTUALES['BRANCH'])

r = get(url, stream=True)
total_size = int(r.headers.get('content-length', 0))
block_size = 1024

print("""
                       _____________________________________________________
                      |                                                     |
            / _____ | |                                                     |
           / /(__) || |                    ACTUALIZANDO                     |
             _______  |                       ZAPADOR                       |
  ________/ / |OO| || |                                                     |
 |         |-------|| |                                                     |
(|         |     -.|| |_______________________                              |
 |  ____   \       ||_________||____________  |             ____      ____  |
/| / __ \   |______||     / __ \   / __ \   | |            / __ \    / __ \ |
\|| /  \ |_______________| /  \ |_| /  \ |__| |___________| /  \ |__| /  \|_|/
   | () |                 | () |   | () |                  | () |    | () |
    \__/                   \__/     \__/                    \__/      \__/

    """)

t=tqdm(total=total_size, unit='iB', unit_scale=True)
with open(cons.DIR_SCRIPT + '/'+'zapador.zip', 'wb') as f:
    for data in r.iter_content(block_size):
        t.update(len(data))
        f.write(data)
t.close()

if isfile(cons.DIR_SCRIPT + '/zapador.exe'):
    remove(cons.DIR_SCRIPT + '/zapador.exe')
if isdir(cons.DIR_SCRIPT + '/zapador'):
    rmtree(cons.DIR_SCRIPT + '/zapador')


print(cons.DIR_SCRIPT + '/zapador.zip')
with ZipFile(cons.DIR_SCRIPT + '/zapador.zip', 'r') as zip_ref:
    zip_ref.extractall(cons.DIR_SCRIPT)

if total_size != 0 and t.n != total_size:
    print("ERROR, Algo salió mal...")
    system('pause')
print('Actualización exitosa. Vuelve a abrir Zapador.')

system('pause')

if isfile(cons.DIR_SCRIPT + '/zapador.zip'):
    remove(cons.DIR_SCRIPT + '/zapador.zip')