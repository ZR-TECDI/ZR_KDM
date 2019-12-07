import zapador.constantes as cons
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.spinner import Spinner
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty


class CampoTexto(BoxLayout):
    etiqueta = StringProperty('Etiqueta: ')
    placeholder = StringProperty('escriba aquí...')


class ListaMapas(Spinner):
    pass


def toggleado(wea):
    if wea.state == 'normal':
        wea.state = 'down'


def mapa_custom(mapa, popup):
    cons.LISTA_MAPAS['Otro'] = mapa
    popup.dismiss()


def generar(cls, mision_oficial):
    for element in cls.children[1].children:
        if hasattr(element, 'nombre_autor') and not element.nombre_autor == None:
            cls.nombre_autor = element.nombre_autor
        if hasattr(element, 'nombre_mision') and not element.nombre_mision == None:
            cls.nombre_mision = element.nombre_mision
        if hasattr(element, 'desc_mision') and not element.desc_mision == None:
            cls.desc_mision = element.desc_mision

    cls.mapa_seleccionado = cls.listamapa.text
    cls.tipo_mision = cls.tipomision.text

    cls.mision_oficial = mision_oficial

    for e in [
            "Autor: " + cls.nombre_autor,
            "Misión: " + cls.nombre_mision,
            "Descripción: " + cls.desc_mision,
            "Mapa: " + cls.mapa_seleccionado +
        ": ({})".format(cons.LISTA_MAPAS[cls.mapa_seleccionado]),
            "Misión oficial: "+str(cls.mision_oficial),
            "Tipo misión: " + cls.tipo_mision]:

        print(e)
