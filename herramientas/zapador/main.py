#!/usr/bin/env python3
# -*- coding: utf-8 -*-
 
"""Zapador es un pequeño script que se encarga de la logística de actualizar el KDM a su última versión y
generar archivos para una nueva misión"""
 
# imports
import urllib.request
import os
import zipfile
import time
import shutil
from pathlib import Path
import generador_mision 

# globales
url                 = "https://github.com/ZR-TECDI/ZR_KDM/archive/master.zip"
quiere_crear        = False
dir_script          = os.path.dirname(os.path.realpath(__file__))
directorio_descarga = dir_script + "\\descargas"
MPMISSIONS_DIR = ""

main_menu = """
    +=======================+===============================================================================+
    |        Comando        |                                  Descripción                                  |
    +=======================+===============================================================================+
    | 1- Setear mpmissions  | Guarda la ruta a tu carpeta de misiones                                       |
    +-----------------------+-------------------------------------------------------------------------------+
    | 2- Actualizar KDM     | Descarga la última versión estable de KDM y la mueve a tu carpeta de misiones |
    +-----------------------+-------------------------------------------------------------------------------+
    | 3- Actualizar y crear | Lo mismo que la anterior, pero también crea archivos para tu nueva misión     |
    +-----------------------+-------------------------------------------------------------------------------+
    | 4- Olvidar seteo      | Olvida la dirección de tu carpeta de misiones                                 |
    +-----------------------+-------------------------------------------------------------------------------+
    | 5- Salir              | Cierra la aplicación                                                          |
    +-----------------------+-------------------------------------------------------------------------------+
"""
sepa = """   .     .     .     .     .     .     .     .     .     .
_.` `._.` `._.` `._.` `._.` `._.` `._.` `._.` `._.` `._.` `."""

AUTOR         = '"ZR Army - Dept. Tecnico y Diseño";'
NOMBRE_MISION = '"TEMPLATE ZR";'
quiere_foto   = False
FOTO_MISION   = '"img\loadscreen.jpg";'
DESC_MISION   = '"Uso exclusivo de Zona Roja Army.";'
EXT_MAPA      = '.VR'
 
# funciones

def descarga():
    """Descarga la última versión disponible del KDM en un directorio nuevo llamado 'descargas'"""

    print(sepa)
    print("Descargando última versión estable desde: "+ url)

    try:
        os.mkdir(dir_script + "\\descargas")
    except Exception as e:
        print("ERROR AL CREAR DIRECTORIO DE DESCARGA: " + str(e))
        os.system("pause")
    else:
        print("Directorio de descarga temporal creado con éxito")
        os.chdir(dir_script + "\\descargas")

    try:
        ultimo_estable = urllib.request.urlretrieve(url, directorio_descarga+"\\kdm.zip")
    except Exception as e:
        print("ERROR AL DESCARGAR: "+ str(e))
        os.system("pause")
    else:
        ultimo_estable = ultimo_estable[0]
        print("Archivo descargado con éxito en: "+ultimo_estable)
        unzip(ultimo_estable)


def unzip(archivo):
    """Descomprime el archivo descargado"""

    print("Extrayendo archivo zip en " + directorio_descarga)
    with zipfile.ZipFile(archivo, 'r') as zip_ref:
        zip_ref.extractall(directorio_descarga)
    mover_carpeta(directorio_descarga)


def mover_carpeta(carpeta):
    """Mueve la carpeta de plantilla desde la descarga hasta la carpeta de misiones del editor"""

    global MPMISSIONS_DIR

    os.system("cls")
    os.chdir(carpeta)
    ruta_plantilla = Path(MPMISSIONS_DIR + "\\template_ZR.VR\\")
    if ruta_plantilla.exists():
        shutil.rmtree(MPMISSIONS_DIR + "\\template_ZR.VR")

    ruta = os.listdir(carpeta)

    for i in ruta:
        es_carpeta = os.path.isdir(i)
        if es_carpeta:
            try:
                shutil.move(i + "\\template_ZR.VR", MPMISSIONS_DIR)
            except Exception as e:
                print("ERROR AL MOVER PLANTILLA A CARPETA DE MISIÓN: ")
                print(str(e))
            else:
                print("Plantilla movida con éxito")
            finally:
                os.chdir(dir_script)
                shutil.rmtree(carpeta)
                os.system("pause")

    carpeta_final = MPMISSIONS_DIR + "\\template_ZR.VR"

    if quiere_crear:
        crear_archivos(carpeta_final)

def crear_archivos(carpeta_final):
    """Consulta al usuario una serie de datos para crear archivos de misión en base a una plantilla"""

    global AUTOR
    global NOMBRE_MISION
    global quiere_foto
    global FOTO_MISION
    global DESC_MISION
    global EXT_MAPA

    AUTOR         = input('Ingresa el autor de la misión (DEFAULT: "ZR Army - Dept. Tecnico y Diseño"):\n')
    if AUTOR == "":
        AUTOR = "ZR Army - Dept. Técnico y Diseño"

    NOMBRE_MISION = input('Ingresa el nombre de la misión (DEFAULT: "TEMPLATE ZR"):\n')
    if NOMBRE_MISION == "":
        NOMBRE_MISION = "TEMPLATE ZR"

    quiere_foto   = input('¿Deseas agregar una foto durante la carga de misión? [S/N]\n').lower()
    if quiere_foto == "s":
        FOTO_MISION = input('Ingresa la dirección relativa de la foto que quieres usar (DEFAULT: "img\loadscreen.jpg"):\n')
        if FOTO_MISION == "":
            FOTO_MISION = "img\loadscreen.jpg"
        quiere_foto = True
    else:
        quiere_foto = False

    DESC_MISION   = input('Ingresa una descripción breve para tu misión (DEFAULT: "Uso exclusivo de Zona Roja Army."):\n')
    if DESC_MISION == "":
        DESC_MISION = "Uso exclusivo de Zona Roja Army."

    print("Elige el mapa donde se va a realizar la misión:\n")
    print("1. Altis") #.Altis
    print("2. Stratis") #.Stratis
    print("3. Malden") #.Malden
    print("4. Realidad Virtual")#.VR
    print("5. Bozcaada")#.Bozcaada
    print("6. Bukovina")#.Bootcamp_ACR
    print("7. Bystrica")#.Woodland_ACR
    print("8. Chernarus")#.chernarus
    print("9. Chernarus (Verano)")#.chernarus_summer
    print("10. Chernarus (Invierno)")#.Chernarus_Winter
    print("11. Desierto")#.Desert_E
    print("12. Fallujah")#.fallujah
    print("13. G.O.S. Al Rayak")#.pja310
    print("14. G.O.S. Dariyah")#.pj307
    print("15. Hazar-Kot (valle)")#.MCN_HazarKot
    print("16. Kidal")#.Kidal
    print("17. Kunduz, Afganistán")#.Kunduz
    print("18. Porto")#.porto 
    print("19. Campo de pruebas")#.ProvingGrounds_PMC
    print("20. Rahmadi")#.intro 
    print("21. Sahrani")#.sara 
    print("22. Sahrani del Sur")#.saralite
    print("23. Sahrani Unida")#.sara_dbe1
    print("24. Shapur")#.Shapur_BAF
    print("25. Takistán")#.takistan
    print("26. Takistán (montañas)")#.Mountains_ACR
    print("27. Tanoa")#.Tanoa
    print("28. Utes")#.utes
    print("29. Zargabad")#.zargabad

    EXT_MAPA = input("El número de tu elección:\n> ")

    if EXT_MAPA == 1:
        EXT_MAPA = '.Altis'
    elif EXT_MAPA == '2':
        EXT_MAPA = ".Stratis"
    elif EXT_MAPA == '3':
        EXT_MAPA = '.Malden'
    elif EXT_MAPA == '4':
        EXT_MAPA = '.VR'
    elif EXT_MAPA == '5':
        EXT_MAPA = '.Bozcaada'
    elif EXT_MAPA == '6':
        EXT_MAPA = '.Bootcamp_ACR'
    elif EXT_MAPA == '7':
        EXT_MAPA = '.Woodland_ACR'
    elif EXT_MAPA == '8':
        EXT_MAPA = '.chernarus'
    elif EXT_MAPA == '9':
        EXT_MAPA = '.chernarus_summer'
    elif EXT_MAPA == '10':
        EXT_MAPA = '.Chernarus_Winter'
    elif EXT_MAPA == '11':
        EXT_MAPA = '.Desert_E'
    elif EXT_MAPA == '12':
        EXT_MAPA = '.fallujah'
    elif EXT_MAPA == '13':
        EXT_MAPA = '.pja310'
    elif EXT_MAPA == '14':
        EXT_MAPA = 'pj307'
    elif EXT_MAPA == '15':
        EXT_MAPA = '.MCN_HazarKot'
    elif EXT_MAPA == '16':
        EXT_MAPA = '.Kidal'
    elif EXT_MAPA == '17':
        EXT_MAPA = '.Kunduz'
    elif EXT_MAPA == '18':
        EXT_MAPA = '.porto'
    elif EXT_MAPA == '19':
        EXT_MAPA = '.ProvingGrounds_PMC'
    elif EXT_MAPA == '20':
        EXT_MAPA = '.intro'
    elif EXT_MAPA == '21':
        EXT_MAPA = 'sara'
    elif EXT_MAPA == '22':
        EXT_MAPA = '.saralite'
    elif EXT_MAPA == '23':
        EXT_MAPA = '.sara_dbe1'
    elif EXT_MAPA == '24':
        EXT_MAPA = '.Shapur_BAF'
    elif EXT_MAPA == '25':
        EXT_MAPA = '.takistan'
    elif EXT_MAPA == '26':
        EXT_MAPA = '.Mountains_ACR'
    elif EXT_MAPA == '27':
        EXT_MAPA = '.Tanoa'
    elif EXT_MAPA == '28':
        EXT_MAPA = '.utes'
    elif EXT_MAPA == '29':
        EXT_MAPA = '.zargabad'
    else:
        print('Error, la opción elegida no es válida. Usando valor DEFAULT')
        os.system('pause')

    generador_mision.main(carpeta_final, AUTOR, NOMBRE_MISION, quiere_foto, FOTO_MISION, DESC_MISION, EXT_MAPA, MPMISSIONS_DIR)


def set_mpmission():
    """Crea o sobrescribe el archivo desde el que se toma la ruta a la carpeta de misiones"""

    global MPMISSIONS_DIR
    os.system("cls")
    print("Busca la ruta a tu carpeta de misiones, debería verse algo así: ")
    print("C:\TU-USUARIO\Documents\Arma 3 - Other Profiles\TU-PERFIL-DE-ARMA\mpmissions")
    print()
    MPMISSIONS_DIR = input("Ingresa la ruta ahora: ")
    with open(dir_script+"/mpmissions.txt", 'w') as f:
        f.write(MPMISSIONS_DIR)
    main()


def olvidar_mpmissions():
    """Elimina el archivo desde donde se toma la carpeta de misiones"""

    os.system("cls")
    try:
        os.remove(dir_script + "/mpmissions.txt")
    except Exception as e:
        print("ERROR AL INTENTAR ELIMINAR DATO: ")
        print(str(e))
    else:
        print("Dato eliminado con éxito")
    finally:
        os.system("pause")


def intro():
    """Presenta la aplicación con su versión y créditos"""

    global MPMISSIONS_DIR

    try: 
        with open(dir_script + "/mpmissions.txt", 'r') as f:
            MPMISSIONS_DIR = f.readline()
    except:
        pass

    print()
    print("""
                       _____________________________________________________
                      |                                                     |
            / _____ | |                       ZAPADOR                       |
           / /(__) || |                       v0.2.0                        |
             _______  |                                                     |
  ________/ / |OO| || |              Escrito por: Riquelme                  |
 |         |-------|| |                                                     |
(|         |     -.|| |_______________________                              |
 |  ____   \       ||_________||____________  |             ____      ____  |
/| / __ \   |______||     / __ \   / __ \   | |            / __ \    / __ \ |
\|| /  \ |_______________| /  \ |_| /  \ |__| |___________| /  \ |__| /  \|_|/
   | () |                 | () |   | () |                  | () |    | () |
    \__/                   \__/     \__/                    \__/      \__/

    """)
    print()
    if MPMISSIONS_DIR == "":
        print("Carpeta de misión sin setear")
    else:
        print("Carpeta de misión: "+ MPMISSIONS_DIR)
    time.sleep(2)
    os.system("pause")
    os.system("cls")
    main()


def main():
    """Menú principal de la aplicación"""

    global quiere_crear

    loop = True
    while loop:
        os.system("cls")
        print(main_menu)

        choice = input("> ")

        if choice == "1":
            set_mpmission()
        if choice == "2":
            descarga()
        if choice == "3":
            quiere_crear = True
            descarga()
        if choice == "4":
            olvidar_mpmissions()
        if choice == "5":
            loop = False
            quit()

if __name__ == "__main__":
	intro()