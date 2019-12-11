import os
import shutil
import sys
from subprocess import Popen
from distutils.dir_util import copy_tree
import cowsay

# constantes
DIR_SCRIPT = os.path.dirname(os.path.realpath(sys.argv[0]))
PAQUETE = DIR_SCRIPT + '/paquete'
DIST = DIR_SCRIPT + '/dist'
ORIGEN = DIR_SCRIPT + '/zapador'
COSO = DIR_SCRIPT + '/dist/zapador'

# funciones
def make_archive(source, destination):
        base = os.path.basename(destination)
        name = base.split('.')[0]
        format = base.split('.')[1]
        archive_from = os.path.dirname(source)
        archive_to = os.path.basename(source.strip(os.sep))
        shutil.make_archive(name, format, archive_from, archive_to)
        shutil.move('%s.%s'%(name,format), destination)

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

# # comprimir archivos para paquete
print('#####################################################')
print('Creando paquete de actualización')
os.mkdir(DIST + '/paquete')
for root, dirs, files in os.walk(DIST):
    for dire in dirs:
        if dire == 'zapador':
            copy_tree(DIST + '/' + dire, DIST + '/paquete'+ '/' + dire)
    
    for file in files:
        if file == 'zapador.exe':
            shutil.copyfile(DIST + '/' + file, DIST + '/paquete/' + file)


make_archive(DIST + '/paquete', PAQUETE + '/zapador.zip')
if os.path.isdir(DIST + '/paquete'):
    shutil.rmtree(DIST + '/paquete')

print('#####################################################')
print('Creando paquete binarios distribuible')
os.mkdir(DIST + '/binarios_zapador')
for root, dirs, files in os.walk(DIST):
    for dire in dirs:
        if dire == 'zapador':
            copy_tree(DIST + '/' + dire, DIST + '/' + dire + '/binarios_zapador')
    for file in files:
        if file == 'zapador.exe' or file == 'auto_update.exe':
            shutil.copyfile(DIST + '/' + file, DIST + '/binarios_zapador/' + file)

make_archive(DIST + '/binarios_zapador', DIST + '/binarios_zapador.zip')
if os.path.isdir(DIST + '/binarios_zapador'):
    shutil.rmtree(DIST + '/binarios_zapador')

# Fin de proceso de build
cowsay.cow('Se acabó el build!')
