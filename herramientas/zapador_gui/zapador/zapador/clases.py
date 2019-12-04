from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty

class CampoTexto(Widget): 
    etiqueta = StringProperty('Etiqueta: ')
    placeholder = StringProperty('escriba aquí...')
    laid = ObjectProperty(None)

def toggleado(wea):
    if wea.state == 'normal':
        wea.state = 'down'