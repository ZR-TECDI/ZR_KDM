#!/usr/bin/env python
# -*- coding: utf-8 -*-

import kivy
kivy.require('1.11.0')

import os
import sys
from zapador.zapadorapp import ZapadorApp
# import zapador.iconfonts as iconfonts

# iconfonts.create_fontdict_file('zapador/assets/fonts/fontello.css', 'zapador/assets/fonts/fontello.fontd')
# iconfonts.register('fontello', 'zapador/assets/fonts/fontello.ttf', 'zapador/assets/fonts/fontello.fontd')

def resourcePath():
    '''Returns path containing content - either locally or in pyinstaller tmp file'''
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS)

    return os.path.join(os.path.abspath("."))

if __name__ == "__main__":
    kivy.resources.resource_add_path(resourcePath())
    ZapadorApp().run()
