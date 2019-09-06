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

# globales
url                 = "https://github.com/ZR-TECDI/ZR_KDM/archive/master.zip"
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
           / /(__) || |                       v0.1.0                        |
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
            pass
        if choice == "4":
            olvidar_mpmissions()
        if choice == "5":
            loop = False
            quit()

if __name__ == "__main__":
	intro()