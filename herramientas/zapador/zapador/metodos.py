import zapador.constantes as cons
from kivy.factory import Factory
import os
import json

# GUI


def toggleado(wea):
    """Aplasta el botón de la página abierta en la GUI"""

    if wea.state == 'normal':
        wea.state = 'down'


def mapa_custom(mapa, popup):
    """Guarda el nombre código del mapa personalizado que introdujo el usuario"""

    cons.LISTA_MAPAS['Otro'] = mapa
    popup.dismiss()


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
        manejador_plantilla()
    ### bajar plantilla y almacenar en carpeta de config/plantilla || si no hay internet informar y no hacer nada
    # comprobar versión zapador || Si no hay internet informar y continuar
    ### actualizar zapador y volver a abrir
    # comprobar versión plantilla || Si no hay internet informar y continua
    ### preguntar si quiere actualizar
    ##### bajar plantilla y almacenar en carpeta de config/plantilla

    
def leer_config():
    """Lee la configuración desde el archivo local"""

    with open(cons.SETTINGS_FILE, 'r', encoding='UTF-8') as f:
        return json.load(f)

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

    json_settings = cons.SETTINGS_INICIALES
    json_settings['MPMISSIONS'] = ruta

    os.makedirs(cons.SETTINGS_DIR)
    with open(cons.SETTINGS_FILE, 'w', encoding='UTF-8') as f:
        f.write(json.dumps(json_settings, sort_keys=True, indent=4))

    pre_run()

def manejador_plantilla():
    if not os.path.isdir(cons.TEMPLATE_DIR):
        print('No hay carpeta de plantilla, se intentará bajar')