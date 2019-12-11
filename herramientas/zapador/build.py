import os
import shutil
import sys
from subprocess import Popen
from distutils.dir_util import copy_tree
import zipfile
import cowsay
import random

# constantes
DIR_SCRIPT = os.path.dirname(os.path.realpath(sys.argv[0]))
PAQUETE = DIR_SCRIPT + '/paquete'
ORIGEN = DIR_SCRIPT + '/zapador'
COSO = DIR_SCRIPT + '/dist/zapador'
DIST = DIR_SCRIPT + '/dist'
PACK = DIST + '/pack/'
BINARIOS = DIST + '/binarios_zapador/'

# clasese y funciones
class Zipeador():
    ruta = None
    archivo_zip = None
    zipy = None

    def __init__(self, ruta, archivo_zip):
        self.ruta = ruta
        self.archivo_zip = archivo_zip
        self.zipy = zipfile.ZipFile(archivo_zip, 'w')
    
    def zipear(self):
        for elemento in os.listdir(self.ruta):
            full_path = self.ruta + '/' + elemento
            if os.path.isfile(full_path):
                print('zipeando archivo: ' + elemento)
                self.zipy.write(DIST + '/' + elemento, elemento)
            if os.path.isdir(full_path):
                print('zipeando carpeta: ' + elemento)
                self.tratar_carpetas(elemento)
        self.zipy.close()
    def tratar_carpetas(self, carpeta):
        for elemento in os.listdir(carpeta):
            full_path = self.ruta + '/' + carpeta + '/' + elemento
            if os.path.isfile(full_path):
                print('zipeando archivo en carpeta: ' + carpeta + '/' + elemento)
                self.zipy.write(carpeta + '/' + elemento)
            if os.path.isdir(full_path):
                self.tratar_carpetas(carpeta + '/'+ elemento)



# eliminar absolutamente todo en dist
print('#####################################################')
print('Limpiando carpeta dist')
for root, dirs, files in os.walk(DIST):
    for file in files:
        os.remove(DIST + '/' +file)
    for dire in dirs:
        shutil.rmtree(DIST + '/' +dire)
    
# buildear zapador.exe
print('#####################################################')
print('Buildeando zapador')
comm = Popen('python -m PyInstaller build.spec')
comm.wait()
# buildear auto_update.exe
print('#####################################################')
print('Buildeando auto_update')
comm = Popen('python -m PyInstaller --onefile auto_update.py')
comm.wait()
if os.path.isfile(DIR_SCRIPT + '/auto_update.spec'):
    os.remove(DIR_SCRIPT + '/auto_update.spec')

# copiar archivos sueltos a dist
print('#####################################################')
print('Creando carpeta de archivos sueltos')
os.mkdir(COSO)
for root, dirs, files in os.walk(ORIGEN):
    for dire in dirs:
        print(dire)
        if dire == 'assets' or dire == 'kv':
            print('Encontrada carpeta para copiar: ' + dire)
            copy_tree(ORIGEN + '/' +dire, COSO + '/' + dire)

# comprimir archivos para paquete
print('#####################################################')
print('Creando paquete de actualización')
for root, dirs, files in os.walk(DIST):
    for dire in dirs:
        if dire == 'zapador':
            copy_tree(DIST + '/' + dire, PACK + dire)
    
    for file in files:
        if file == 'zapador.exe':
            shutil.copyfile(DIST + '/' + file, PACK + file)

ziper = Zipeador(PACK, PAQUETE + '/zapador.zip')
ziper.zipear()

if os.path.isdir(PACK):
    shutil.rmtree(PACK)

print('#####################################################')
print('Creando paquete binarios distribuible')
os.mkdir(BINARIOS)
for root, dirs, files in os.walk(DIST):
    for dire in dirs:
        if dire == 'zapador':
            copy_tree(DIST + '/' + dire, BINARIOS + dire)
    for file in files:
        if file == 'zapador.exe' or file == 'auto_update.exe':
            shutil.copyfile(DIST + '/' + file, BINARIOS + file)

ziper = Zipeador(BINARIOS, DIST + '/binarios_zapador.zip')
ziper.zipear()
if os.path.isdir(DIST + '/binarios_zapador'):
    shutil.rmtree(DIST + '/binarios_zapador')

# Fin de proceso de build
personajes = cowsay.chars
cowsay.personaje = random.choice(personajes)
cowsay.personaje('Se acabó el build!')
