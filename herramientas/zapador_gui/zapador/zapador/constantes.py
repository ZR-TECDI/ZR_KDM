from appdirs import AppDirs

SETTINGS_DIR = AppDirs(appname='zapador', appauthor='ZR-TECDI').site_config_dir
TEMPLATE_DIR = SETTINGS_DIR + '/template/'


BUILD_VERSION = '0.9.0'
KDM_VERSION = 'https://raw.githubusercontent.com/ZR-TECDI/ZR_KDM/{}/template_ZR.VR/configurar_mision.hpp'
LOCAL_KDM_VERSION = TEMPLATE_DIR + '/template_ZR.VR/configurar_mission.hpp'
ZAPADOR_VERSION = 'https://raw.githubusercontent.com/ZR-TECDI/ZR_KDM/{}/herramientas/zapador/versionado.py'

