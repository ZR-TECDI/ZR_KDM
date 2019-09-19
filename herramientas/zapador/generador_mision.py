#!/usr/bin/env python3
# -*- coding: utf-8 -*-
 
"""Este script se encarga de generar el archivo de misión con los datos que ingrese el usuario"""

# Imports
import os
import cgi

# globales
CARPETA_MISION = ""
AUTOR          = '"ZR Army - Dept. Tecnico y Diseño";'
NOMBRE_MISION  = '"TEMPLATE ZR";'
QUIERE_FOTO    = False
FOTO_MISION    = '"img\loadscreen.jpg";'
DESC_MISION    = '"Uso exclusivo de Zona Roja Army.";'
EXT_MAPA       = '.VR'
MPMISSIONS_DIR = ""

# Funciones
def escribir(data, mode):
    archivo_mision = CARPETA_MISION + "\\configurar_mision.hpp" 
    try:
        with open(archivo_mision, mode) as f:
            f.write(data)
    except BaseException as e:
        print(e)

def header():
    data = \
"""
/*********************************************************
********** configurar_mision.hpp *************************
**********************************************************
* Archivo creado de forma automatizada con ZAPADOR.      *
*                                                        *
* Por favor, informar cualquier error, sugerencia,       *
* petición en:                                           *
* https://github.com/ZR-TECDI/ZR_KDM/issues/new          *
* (Requiere registrarse en el sitio)                     *
**********************************************************/
"""

    escribir(data, 'w')
    
    escribir_autor()

def escribir_autor():
    global AUTOR

    data = 'author = "'+AUTOR+'";\n'
    escribir(data, 'a')
    
    escribir_nombre_mision()

def escribir_nombre_mision():
    global NOMBRE_MISION

    data = 'OnLoadName = "'+NOMBRE_MISION+'";\n'
    escribir(data, 'a')
    
    escribir_desc_mision()

def escribir_desc_mision():
    global DESC_MISION

    data = 'OnLoadMission = "'+DESC_MISION+'";\n'
    escribir(data, 'a')
    
    escribir_foto_mision()

def escribir_foto_mision():
    global QUIERE_FOTO
    global FOTO_MISION

    if not QUIERE_FOTO:
        pass
    else:
        data = 'loadScreen = "'+FOTO_MISION+'";\n'
        escribir(data, 'a')
    
    header_datos_mision()

def header_datos_mision():
    data = """\
\n\n/*****************************************************
*************Datos de misión******************************
**********************************************************/\n\n"""
    escribir(data, 'a')

    escribir_tipo_mision()
                                                    
def escribir_tipo_mision():
    os.system('cls')
    print('Tipo de misión: ')
    print('1. Misión oficial')
    print('2. Entrenamiento')
    print('3. Improvisada')
    print('4. Gala')
    print('5. Instrucción')
    print('6. Otro')
    TIPO_MISION = input('Elige un tipo de misión: \n>')

    if TIPO_MISION == '1':
        TIPO_MISION = 'Misión Oficial'
    elif TIPO_MISION == '2':
        TIPO_MISION = 'Entrenamiento'
    elif TIPO_MISION == '3':
        TIPO_MISION = 'Improvisada'
    elif TIPO_MISION == '4':
        TIPO_MISION = 'Gala'
    elif TIPO_MISION == '5':
        TIPO_MISION = 'Instrucción'
    elif TIPO_MISION == '6':
        TIPO_MISION = 'Otro'
    else:
        print('Opción ingresada no es válida. Procediendo con valor default "Otro".')

    data = 'TIPO_MISION = "{}";\n'.format(TIPO_MISION)
    escribir(data, 'a')

    escribir_campa()  

def escribir_campa():
    os.system('cls')
    NOMBRE_CAMPA = input('¿Es esta misión parte de una campaña? ¿Cuál?\n Presiona enter sin ingresar nada para saltar.\n> ')
    if NOMBRE_CAMPA == "":
        NOMBRE_CAMPA = "--"
    
    data = 'NOMBRE_CAMPA = "{}";\n'.format(NOMBRE_CAMPA)
    escribir(data, 'a')

    cambiar_mapa()

def validar_nombre(nombre):
    simbolos_malos = ["!", ".", ",", '"', "ç", "=", "(", ")", "/", "\\", "$", "·", "%", "&", "?", "¡", "?", "'", "|", "@", "#", "~", "¬"]
    for simbolo in simbolos_malos:
        # if simbolo in nombre:
        if nombre.find(simbolo,0,len(nombre)) >= 0:
            nombre = nombre.replace(simbolo, "")
    
    valid_dict = {
        " ": "_",
        "á": "a",
        "à": "a",
        "â": "a",
        "é": "e",
        "è": "e",
        "ê": "e",
        "í": "i",
        "ì": "i",
        "î": "i",
        "ó": "o",
        "ò": "o",
        "ô": "o",
        "ú": "u",
        "ù": "u",
        "û": "u",
        "ñ": "n"
    }
    
    for x,y in valid_dict.items():
        if x in nombre:
            nombre = nombre.replace(x,y)

    return nombre

def cambiar_mapa():
    global CARPETA_MISION
    global NOMBRE_MISION
    global EXT_MAPA
    global MPMISSIONS_DIR

    nombre_html  = validar_nombre(NOMBRE_MISION.lower())
    nuevo_nombre = MPMISSIONS_DIR + "\\" + nombre_html + EXT_MAPA

    try:
        os.rename(CARPETA_MISION, nuevo_nombre)
    except Exception as e:
        os.system('cls')
        print(str(e))
    else:
        os.system('cls')
        print('Misión creada con éxito, prueba abrirla desde el editor.')
        print('Carpeta: '  + nuevo_nombre)

    os.system('pause')

def main(carpeta_final, autor, nombre_mision, quiere_foto, foto_mision, desc_mision, ext_mapa, mpmissions_dir):
    
    
    global CARPETA_MISION
    global AUTOR
    global NOMBRE_MISION
    global QUIERE_FOTO
    global FOTO_MISION
    global DESC_MISION
    global EXT_MAPA
    global MPMISSIONS_DIR

    CARPETA_MISION = carpeta_final
    AUTOR          = autor
    NOMBRE_MISION  = nombre_mision
    QUIERE_FOTO    = quiere_foto
    FOTO_MISION    = foto_mision
    DESC_MISION    = desc_mision
    EXT_MAPA       = ext_mapa
    MPMISSIONS_DIR = mpmissions_dir

    header()

if __name__ == "__main__":
	print("Este módulo neceista main.py del paquete Zapador")