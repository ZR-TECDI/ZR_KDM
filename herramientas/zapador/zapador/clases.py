import zapador.constantes as cons
from zapador.metodos import pre_run
from zapador.metodos import un_zip
from kivy.uix.popup import Popup
from kivy.factory import Factory
from kivy.properties import StringProperty
from kivy.properties import NumericProperty
from kivy.properties import BooleanProperty
from kivy.clock import mainthread
import threading
import psutil
from distutils import dir_util
from shutil import copyfile
import re
from os import environ as env
import os
import requests


class ERROR(Popup):
    titulo = StringProperty('titulo')
    mensaje = StringProperty('mensaje')


class Descargando(Popup):
    titulo = StringProperty('titulo')
    mensaje = StringProperty('mensaje')
    peso_max = NumericProperty()
    peso_actual = NumericProperty()
    continuar = BooleanProperty(True)

    stop = threading.Event()

    @mainthread
    def update_gui(self, actual):
        self.peso_actual = actual

    def descargar(self, enlace, ruta_descarga, unzip=False):
        threading.Thread(target=self.descargar_threaded,
                         args=(enlace, ruta_descarga, unzip)).start()

    def descargar_threaded(self, enlace, ruta_descarga, unzip):
        enlace = enlace.format(cons.SETTINGS_ACTUALES['BRANCH'])
        response = requests.get(enlace)

        if os.path.isfile(ruta_descarga):
            os.remove(ruta_descarga)

        with open(ruta_descarga, 'wb') as f:
            response = requests.get(enlace, stream=True)
            total = int(response.headers['Content-length'])
            chunk = 1
            self.peso_max = total / chunk
            i = 0
            for chunk in response.iter_content():
                f.write(chunk)
                self.update_gui(i)
                i += 1

        if unzip:
            un_zip(ruta_descarga, cons.TEMPLATE_DIR, cons.TEMPLATE_NAME)
        self.continuar = False


class Navegador(Popup):
    def encontrar_lugares(self):
        lugares = []

        if cons.SETTINGS_ACTUALES:
            lugares.append('Misiones')

        lugares.append('Escritorio')
        lugares.append('Carpeta Usuario')

        parts = psutil.disk_partitions()
        for part in parts:
            lugares.append(part[0])

        return lugares

    def alias_lugares(self, alias):
        """Maneja la ruta del navegador, usando alias en lugar de ruta completa"""

        if alias == 'Misiones':
            self.ids['filechoose'].path = cons.SETTINGS_ACTUALES['MPMISSIONS']
            return

        if alias not in cons.LISTA_ALIAS_NOMBRES:
            self.ids['filechoose'].path = alias
            return

        self.ids['filechoose'].path = cons.LISTA_ALIAS_NOMBRES[alias]
        

    def abrir_popup(self):
        self.open()

    def boton_abrir(self, select):
        pass


class MPMissions(Navegador):
    def abrir_popup(self, text_id):
        self.text_id = text_id
        self.open()

    def boton_abrir(self, select):
        self.text_id.text = select[0]
        self.dismiss()


class FotoMision(Navegador):
    def abrir_popup(self, foto_id):
        self.foto_id = foto_id
        self.open()

    def boton_abrir(self, select):
        self.foto_id.source = select[0]
        self.dismiss()

class MapaCustom(Popup):
    def abrir_popup(self, spinner):
        self.spinner = spinner
        self.open()

    def boton_aceptar(self, mapa):
        self.spinner.text = mapa
        cons.LISTA_MAPAS['Otro'] = mapa
        self.dismiss()

class Generador():

    def __init__(self, autor, mision, desc, mapa, oficial, tipo, campana, nueva_campana, foto):
        if campana == "Crear Nueva":
            campana = nueva_campana
        if mapa not in cons.LISTA_MAPAS.keys():
            mapa = 'Otro'

        self.autor = autor
        self.mision = mision
        self.desc = desc
        self.mapa = cons.LISTA_MAPAS[mapa]
        self.oficial = oficial
        self.tipo = cons.TIPO_MISION[tipo]
        if self.tipo == 'CAMPANA':
            self.campana = campana
        else:
            self.campana = 'NULL'
        self.foto = foto

    def debug_valores(self, mapa):
        for e in [
            "autor: " + self.autor,
            "misión: " + self.mision,
            "desc: " + self.desc,
            "mapa: " + mapa + " ({})".format(self.mapa),
            "es oficial: " + str(self.oficial),
            "tipo: " + self.tipo,
            "campaña: " + self.campana,
                "path foto: " + self.foto]:
            print(e)
    
    def nombre_seguro(self, nombre):
        valid_dict = {
            "": ["`","!", ".", ",", '"', "ç", "Ç", "=","(", ")", "/", "\\", 
                "$", "·", "%", "&", "?", "¡", "?", "'", "|", "@", "#", 
                "~", "¬", "*", "", "`", "{", "}"],
            "a": ["á", "à", "ä", "â"],
            "e": ["é", "è", "ë", "ê"],
            "i": ["í", "ì", "ï", "î"],
            "o": ["ó", "ò", "ô", "ô"],
            "u": ["ú", "ù", "ü", "û"],
            "A": ["Á", "À", "Ä", "Â"],
            "E": ["É", "È", "Ë", "Ê"],
            "I": ["Í", "Ì", "Ï", "Î"],
            "O": ["Ó", "Ò", "Ö", "Ô"],
            "U": ["Ú", "Ù", "Ü", "Û"],
            "n": ["ñ"],
            "N": ["Ñ"],
            "_": [" "]       
            }
        
        for key, value in valid_dict.items():
            for wea_fea in value:
                if wea_fea in nombre:
                    nombre = nombre.replace(wea_fea, key)

        return nombre

    def configurar_mision(self, variable, valor, modo):
        busqueda = re.compile('({} = ")(.*)";'.format(variable))

        if modo == 'a' or modo == 'w':
            pass
        else:
            raise ValueError('Sólo modo (a)ppend y (w)rite están permitidos')

        if modo == 'a':
            with open(self.ruta_mision + '/configurar_mision.hpp', 'a', encoding='UTF-8') as f:
                if type(valor) == bool:
                    linea = '\n{} = {};'.format(variable, valor)
                else: 
                    linea = '\n{} = "{}";'.format(variable, valor)

                f.write(linea) 
        else:
            with open(self.ruta_mision + '/configurar_mision.hpp', 'r', encoding='UTF-8')as f:
                texto_actual = f.read()

            nuevo_texto = busqueda.sub(r'\1{}";'.format(valor), texto_actual)
            with open(self.ruta_mision + '/configurar_mision.hpp', 'w', encoding='UTF-8') as f:
                f.write(nuevo_texto)



    def generar(self):
        nombre = self.nombre_seguro(self.mision) + self.mapa
        self.ruta_mision = cons.SETTINGS_ACTUALES['MPMISSIONS'] + '/' + nombre

        dir_util.copy_tree(cons.TEMPLATE_DIR + cons.TEMPLATE_NAME, self.ruta_mision)
        copyfile(self.foto, self.ruta_mision+ '/' + 'loadscreen.jpg')
        
        self.configurar_mision('author', self.autor, 'w')
        self.configurar_mision('OnLoadName', self.mision, 'w')
        self.configurar_mision('OnLoadMission', self.desc, 'w')
        self.configurar_mision('overviewText', self.desc, 'w')

        self.configurar_mision('TIPO_MISION', self.tipo, 'a')
        if not self.campana == 'NULL':
            self.configurar_mision('NOMBRE_CAMPA', self.campana, 'a')
        self.configurar_mision('es_oficial', self.oficial, 'a')

        pop = ERROR(
            titulo='¡Misión Generada!',
            mensaje='Tu misión fue generada.\nCompruébalo en tu carpeta de misiones: [color=#e6cd17]{}[/color].\n\n¡Ahora sólo queda abrir tu misión en el editor de Arma3!'.format(cons.SETTINGS_ACTUALES['MPMISSIONS'])
        )
        pop.open()


