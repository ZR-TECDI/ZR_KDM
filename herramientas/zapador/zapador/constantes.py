from appdirs import AppDirs
from os import environ as env
import os
import sys

VERSION = '1.0.0'

SETTINGS_DIR = AppDirs(appname='zapador', appauthor='ZR-TECDI').site_config_dir
SETTINGS_FILE = SETTINGS_DIR + '\\config.json'
TEMPLATE_DIR = SETTINGS_DIR + '\\plantilla\\'
TEMPLATE_NAME = 'template_ZR.VR'
DIR_SCRIPT = os.path.dirname(os.path.realpath(sys.argv[0]))


KDM_VERSION = 'https://raw.githubusercontent.com/ZR-TECDI/ZR_KDM/{}/template_ZR.VR/configurar_mision.hpp'
LOCAL_KDM_VERSION = TEMPLATE_DIR + 'template_ZR.VR\\configurar_mision.hpp'
KDM_URL = 'https://github.com/ZR-TECDI/ZR_KDM/raw/{}/template_ZR.VR.zip'
ZAPADOR_VERSION = 'https://raw.githubusercontent.com/ZR-TECDI/ZR_KDM/{}/herramientas/zapador/zapador/constantes.py'
ZAPADOR_PAQUETE = 'https://raw.githubusercontent.com/ZR-TECDI/ZR_KDM/{}/herramientas/zapador/paquete/zapador.zip'

SETTINGS_INICIALES = {
    "MPMISSIONS": "",
    "BRANCH": "master"
}

SETTINGS_ACTUALES = {}

LISTA_ALIAS_NOMBRES = {
    "Escritorio": env['USERPROFILE'] + '/Desktop',
    "Carpeta Usuario": env['USERPROFILE']
}


LISTA_BRANCHES = ['master', 'dev-branch']

LISTA_MAPAS = {
    "Altis":".Altis",
    "Stratis":".Stratis",
    "Malden":".Malden",
    "Realidad Virtual":".VR",
    "Bozcaada":".Bozcaada",
    "Bukovina":".Bootcamp_ACR",
    "Bystrica":".Woodland_ACR",
    "Chernarus":".chernarus",
    "Chernarus (Verano)":".chernarus_summer",
    "Chernarus (Invierno)":".Chernarus_Winter",
    "Desierto":".Desert_E",
    "Fallujah":".fallujah",
    "GOS. Al Rayak":".pja310",
    "GOS. Dariyah":".pj307",
    "Hazar-Kot (valle)":".MCN_HazarKot",
    "Kidal":".Kidal",
    "Kunduz, Afganistán":".Kunduz",
    "Porto":".porto ",
    "Campo de pruebas":".ProvingGrounds_PMC",
    "Rahmadi":".intro ",
    "Sahrani":".sara ",
    "Sahrani del Sur":".saralite",
    "Sahrani Unida":".sara_dbe1",
    "Shapur":".Shapur_BAF",
    "Takistán":".takistan",
    "Takistán (montañas)":".Mountains_ACR",
    "Tanoa":".Tanoa",
    "Utes":".utes",
    "Zargabad":".zargabad",
    "Prei (Camboya)":".prei_khmaoch_luong",
    "Otro":"CUSTOM"
}

API_JSON_TEST = {
    "CAMPANAS": [
        "campaña prueba 1",
        "campaña prueba 2",
        "campaña prueba 3",
        "campaña prueba 4",
        "Crear Nueva"
    ]
}

TIPO_MISION = {
    "Campaña":"CAMPANA",
    "Entrenamiento":"ENTRENAMIENTO",
    "Gala":"GALA",
    "Improvisada":"IMPROVISADA",
    "Curso":"CURSO",
    "Cooperativa":"COOPERATIVA",
    "Otro":"OTRO"
}

TIPO_MISION_IMPORTAR = {
    "CAMPANA":"Campaña",
    "ENTRENAMIENTO":"Entrenamiento",
    "GALA":"Gala",
    "IMPROVISADA":"Improvisada",
    "CURSO":"Curso",
    "COOPERATIVA":"Cooperativa",
    "OTRO":"Otro"
}