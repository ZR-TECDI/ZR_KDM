/*
    Autor: Riquelme
    Desc : Comprueba que los jugadores tengan permiso de administrar el servidor y les permite usar el DMB.
    //TODO cambiar el modo de verificar para utilizar SteamID en lugar de nombres

    Argumentos:
    --

    Retorna:
    True si el jugador es admin, false si no lo es <BOOL>

    Ejemplos:
    ["zonaMinada", "APERSMine", 20] call ZR_fnc_campoMinado; Poblará la zona "zonaMinada" con 20 minas 
    antipersonales.

    Pública: Sí
 */

private _jugador = name player;

private _admins = ["Alf.Jaz", "Sgt1.Disluk", "Sgt.Jäger", "Cbo1.Riquelme", "Cap.Marino", "May.Daniel"];

if((_admins find _jugador) > -1 ) exitWith {true};

false;