from kivy.app import App
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition

import zapador.constantes as cons
from zapador.metodos import pre_run
from zapador.clases import *
from kivy.factory import Factory 

with open('zapador/kv/main.kv', encoding='UTF-8') as f: 
    Builder.load_string(f.read())
with open('zapador/kv/clases.kv', encoding='UTF-8') as f: 
    Builder.load_string(f.read())
with open('zapador/kv/contenido.kv', encoding='UTF-8') as f:
    Builder.load_string(f.read())

class Pantalla_Nueva(Screen):
    pass
        
class Pantalla_Importar(Screen):
    pass

class Pantalla_Opciones(Screen):
    pass

sm = ScreenManager(transition=FadeTransition())
sm.add_widget(Pantalla_Nueva(name='pantalla_nueva'))
sm.add_widget(Pantalla_Importar(name='pantalla_importar'))
sm.add_widget(Pantalla_Opciones(name='pantalla_opciones'))

def cambiar_pantalla(pantalla):
    sm.current = pantalla

class ZapadorApp(App):
    """Entry point para Zapador app"""
    def on_start(self):
        pre_run()

    def on_stop(self):
        Descargando.stop.set()

    def build(self):
        self.title = 'Zapador v'+cons.BUILD_VERSION
        self.icon  = 'zapador/assets/img/zapador.ico'
        return sm
    

