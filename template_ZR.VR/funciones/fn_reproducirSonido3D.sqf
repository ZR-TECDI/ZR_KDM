params["_objeto", "_sonido", ["_volume", 0]];

/*
    Autor: Riquelme
    Desc : Reproduce un sonido de formato OGG que se guarde en la carpeta "sonidos" dentro 
    de la carpeta de misión. Se utiliza un objeto como la fuente del sonido. Todos los 
    jugadores en el área pueden oír el sonido.

    Argumentos:
    0: objeto que será la fuente del sonido <OBJECT>
    1: nombre del archivo de sonido <STRING>
    2: opcional. Intensidad extra del sonido de 0 a 5 (0 es defecto) <INTEGER>

    Retorna:
    --

    Ejemplos:
    [megafono_1, "despertar.ogg"] call ZR_fnc_reproducirSonido3D;

    Pública: Sí
    
    Se asume que el archivo está dentro de la carpeta "sonidos" y es formato OGG.
 */

private _soundPath = [(str missionConfigFile), 0, -15] call BIS_fnc_trimString;
private _soundToPlay = _soundPath + format["sonidos\%1", _sonido];
playSound3D [_soundToPlay, _objeto, False, getPosATL _objeto, _volume]; 