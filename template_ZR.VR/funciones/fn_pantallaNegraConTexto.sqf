/*
    Autor: Riquelme
    Desc : Crea una pantalla negra y muestra el texto que se indique como argumento.

    Argumentos:
    0: Texto a mostrar <STRING>

    Retorna:
    El texto que debería aparecer <STRING>

    Ejemplos:
    ["Puente Merderet\nFrancia"] call ZR_fnc_pantallaNegraConTexto;

    Pública: Sí
    Necesita correr en la máquina local del afectado, es buena idea usar remoteExec
 */

params["_texto"];

cutText ["", "BLACK", 0];
sleep 2;
// Pantalla negra
cutText [_texto, "BLACK FADED"];
sleep 5;
// Quitar pantalla negra
cutText ["", "BLACK IN", 5];
sleep 5;

_texto;