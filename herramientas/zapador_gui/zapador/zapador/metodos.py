def toggleado(wea):
    if wea.state == 'normal':
        wea.state = 'down'


def mapa_custom(mapa, popup):
    cons.LISTA_MAPAS['Otro'] = mapa
    popup.dismiss()


def widget_condicional(master, child, cond):
    if master == cond:
        child.disabled = False
    else:
        child.disabled = True

def cambiar_foto(archivo, foto_wd):
    pass