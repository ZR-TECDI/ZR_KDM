from appdirs import AppDirs

SETTINGS_DIR = AppDirs(appname='zapador', appauthor='ZR-TECDI').site_config_dir
TEMPLATE_DIR = SETTINGS_DIR + '/template/'


BUILD_VERSION = '0.9.0'
KDM_VERSION = 'https://raw.githubusercontent.com/ZR-TECDI/ZR_KDM/{}/template_ZR.VR/configurar_mision.hpp'
LOCAL_KDM_VERSION = TEMPLATE_DIR + '/template_ZR.VR/configurar_mission.hpp'
ZAPADOR_VERSION = 'https://raw.githubusercontent.com/ZR-TECDI/ZR_KDM/{}/herramientas/zapador/versionado.py'


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