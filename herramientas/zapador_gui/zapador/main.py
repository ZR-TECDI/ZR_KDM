#!/usr/bin/env python
# -*- coding: utf-8 -*-

import kivy
kivy.require('1.8.0')

from zapador.zapadorapp import ZapadorApp
import zapador.iconfonts as iconfonts

iconfonts.create_fontdict_file('zapador/assets/fonts/fontello.css', 'zapador/assets/fonts/fontello.fontd')
# iconfonts.register('fontello', 'zapador/assets/fonts/fontello.ttf', 'zapador/assets/fonts/fontello.fontd')

if __name__ == "__main__":
    ZapadorApp().run()
