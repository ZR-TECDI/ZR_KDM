import zapador.constantes as cons
from kivy.uix.popup import Popup
from kivy.factory import Factory
import psutil
from os import environ as env


class Navegador(Popup):
    def encontrar_lugares(self):
        lugares = []
        escritorio = env['USERPROFILE'] + '/Desktop'
        documentos = env['USERPROFILE'] + '/Documents'
        lugares.append(escritorio)
        lugares.append(documentos)
        
        parts = psutil.disk_partitions()
        for part in parts:
            lugares.append(part[0])

        return lugares

    def abrir_popup(self):
        self.open()

    def boton_abrir(self, select):
        pass


class FotoMision(Navegador):
    def abrir_popup(self, foto_id):
        self.foto_id = foto_id
        self.open()

    def boton_abrir(self, select):
        self.foto_id.source = select[0]
        self.dismiss()


class Generador():
    DEBUG = True

    def __init__(self, autor, mision, desc, mapa, oficial, tipo, campana, nueva_campana, foto):
        if campana == "Crear Nueva":
            campana = nueva_campana

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

        if self.DEBUG:
            self.debug_valores(mapa)

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
