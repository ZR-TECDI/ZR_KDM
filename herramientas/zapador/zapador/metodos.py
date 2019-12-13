import zapador.constantes as cons
from kivy.factory import Factory
import os
from shutil import rmtree
import json
import requests as r
import zipfile
import re
from packaging import version
from subprocess import Popen, CREATE_NEW_CONSOLE

# GUI
def cancelar_config(mpmissions, branch):
    cons.SETTINGS_ACTUALES = leer_config()

    mpmissions.text = cons.SETTINGS_ACTUALES['MPMISSIONS']
    branch.text = cons.SETTINGS_ACTUALES['BRANCH']

def toggleado(wea):
    """Aplasta el botón de la página abierta en la GUI"""

    if wea.state == 'normal':
        wea.state = 'down'

def widget_condicional(master, child, cond):
    """Permite deshabilitar un widget teniendo una condición en otro"""

    if master == cond:
        child.disabled = False
    else:
        child.disabled = True

# Lógica


def pre_run():
    """Método que se ejecuta durante el inicio de la app. Maneja todas las tareas
    relevantes a la actualización de medios."""

    # comprobar si es primera vez
    if not os.path.isfile(cons.SETTINGS_FILE):
        Factory.PrimeraVez().open()
    else:
        cons.SETTINGS_ACTUALES = leer_config()
    # comprobar versión zapador || Si no hay internet informar y continuar
    ### actualizar zapador y volver a abrir
        manejador_zapador()
    ### bajar plantilla y almacenar en carpeta de config/plantilla || si no hay internet informar y no hacer nada
        manejador_plantilla()
    # comprobar versión plantilla || Si no hay internet informar y continua
    ### preguntar si quiere actualizar
    ##### bajar plantilla y almacenar en carpeta de config/plantilla

    
def leer_config():
    """Lee la configuración desde el archivo local"""

    if not os.path.isfile(cons.SETTINGS_FILE):
        return cons.SETTINGS_INICIALES

    with open(cons.SETTINGS_FILE, 'r', encoding='UTF-8') as f:
        return json.load(f)

def get_config(key):
    """Retorna el valor de una opción desde el archivo de opciones"""

    opciones = leer_config()
    return opciones[key]

def escribir_config(config):
    """Escribe la configuración pasada por parámetro en el archivo local"""

    cons.SETTINGS_ACTUALES = config

    with open(cons.SETTINGS_FILE, 'w', encoding='UTF-8') as f:
        f.write(json.dumps(config, sort_keys=True, indent=4))
    
def crear_archivo_config(popup, ruta):
    """Crea el archivo local de configuración, permite la persistencia de datos"""

    if not os.path.isdir(ruta):
        error = Factory.ERROR(
            titulo='¡La ruta no existe!',
            mensaje='Ocurrió un problema y no encuentro la ruta que me diste.')
        
        error.open()
    else:
        popup.dismiss()

    cons.SETTINGS_ACTUALES = cons.SETTINGS_INICIALES
    cons.SETTINGS_ACTUALES['MPMISSIONS'] = ruta

    if not os.path.isdir(cons.TEMPLATE_DIR):
        os.makedirs(cons.TEMPLATE_DIR)
    with open(cons.SETTINGS_FILE, 'w', encoding='UTF-8') as f:
        f.write(json.dumps(cons.SETTINGS_ACTUALES, sort_keys=True, indent=4))

    pre_run()

def actualizar_zapador():
    Popen(cons.DIR_SCRIPT + '/auto_update.exe', creationflags=CREATE_NEW_CONSOLE)
    quit()

def manejador_zapador():
    """Comprueba versión actual de zapador y maneja la actualización de ser necesario"""
    if not chequear_version('ZAPADOR', cons.ZAPADOR_VERSION):
        Factory.NuevaVersion().open()

def manejador_plantilla():
    """El manejador de plantillas maneja las plantillas"""

    if not os.path.isdir(cons.TEMPLATE_DIR + '/' + cons.TEMPLATE_NAME):
        descargar_plantilla = Factory.Descargando(
            titulo='Descargando plantilla',
            mensaje='Descargando la última versión estable de KDM'
        )
        descargar_plantilla.open()

        descargar_plantilla.descargar(cons.KDM_URL, cons.TEMPLATE_DIR + cons.TEMPLATE_NAME + '.zip', unzip=True)
    else:
        if not chequear_version(cons.LOCAL_KDM_VERSION, cons.KDM_VERSION):
            rmtree(cons.TEMPLATE_DIR + cons.TEMPLATE_NAME)
            manejador_plantilla()
        
def un_zip(zip, ruta, objeto):
    """Saca del zip las cosas :O"""

    if os.path.isfile(ruta+'/'+objeto):
        os.remove(ruta+'/'+objeto)

    if os.path.isdir(ruta+'/'+objeto):
        rmtree(ruta+'/'+objeto)


    with zipfile.ZipFile(zip, 'r') as zip_ref:
        zip_ref.extractall(ruta)

def chequear_version(local, remoto):
    """Comprueba la versión local y remoto, avisa si hay actualización"""

    busqueda = re.compile('''version = ['"](\d+\.\d+\.\d+)['"]''', re.I)

    try:
        url = remoto.format(cons.SETTINGS_ACTUALES['BRANCH'])
        remoto = r.get(url).text

    except Exception as e:
        error = Factory.ERROR(
            titulo='Algo salió mal...',
            mensaje=str(e)
        )
        error.open()
    else:
        if local == 'ZAPADOR':
            version_local = cons.VERSION
        else:
            with open(local, 'r', encoding='UTF-8') as f:
                local = f.read()

            version_local = re.search(busqueda, local)
        version_remoto = re.search(busqueda, remoto)
        if not type(version_local) == str:
            version_local = version_local.group(1)
        version_remoto = version_remoto.group(1)


        print('versiones: ' + version_local, version_remoto)

        if version.parse(version_local) >= version.parse(version_remoto):
            return True
            print('versiones parecen ser igual o mejor que en server')
        else:
            print('versión está desfasada con server')
            return False
