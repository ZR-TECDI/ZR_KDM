import zapador.constantes as cons
import json
import requests
from tqdm import tqdm
from os import system

with open(cons.SETTINGS_FILE, 'r', encoding='UTF-8') as f:
    cons.SETTINGS_ACTUALES = json.load(f)

r = requests.get(cons.ZAPADOR_PAQUETE, stream=True)
total_size = int(r.headers.get('content-length', 0))
block_size = 1024

t=tqdm(total=total_size, unit='iB', unit_scale=True)
with open(cons.DIR_SCRIPT + '/'+'zapador.exe', 'wb') as f:
    for data in r.iter_content(block_size):
        t.update(len(data))
        f.write(data)
t.close()
print('Actualización exitosa. Vuelve a abrir Zapador.')
system('pause')
quit()
if total_size != 0 and t.n != total_size:
    print("ERROR, Algo salió mal...")
