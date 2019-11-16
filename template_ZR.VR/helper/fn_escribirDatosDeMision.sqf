/*
    Autor: Riquelme
    Desc : Helper que escribe los datos de misión según fueron configurados en Zapador para luego ser 
    capturados por la base de datos de ZRStats.

    Argumentos:
    --

    Retorna:
    --

    Ejemplos:
    --

    Pública: No
 */

prefix = "ZRSTATS";

NOMBRE_MISION = getMissionConfigValue "onLoadName";
DESC_MISION   = getMissionConfigValue "OnLoadMission";
AUTOR_MISION  = getMissionConfigValue "author";
TIPO_MISION   = getMissionConfigValue "TIPO_MISION";

if (TIPO_MISION isEqualTo "CAMPANA") then{
    NOMBRE_CAMPA = getMissionConfigValue "NOMBRE_CAMPA";
};

ES_OFICIAL = getMissionConfigValue "es_oficial";
MAPA_MISION   = worldName;

diag_log format["%1: NOMBRE_MISION %2", prefix, NOMBRE_MISION];
diag_log format["%1: DESC_MISION %2", prefix, DESC_MISION];
diag_log format["%1: AUTOR_MISION %2", prefix, AUTOR_MISION];
diag_log format["%1: TIPO_MISION %2", prefix, TIPO_MISION];
if (!isNil "NOMBRE_CAMPA") then {
    diag_log format["%1: NOMBRE_CAMPA %2", prefix, NOMBRE_CAMPA];
};
diag_log format["%1: ES_OFICIAL %2", prefix, ES_OFICIAL];
diag_log format["%1: MAPA_MISION %2", prefix, MAPA_MISION];