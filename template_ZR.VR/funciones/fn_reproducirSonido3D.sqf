params["_objeto", "_sonido"];

/*
    Autor: Riquelme
    Desc : Reproduce un sonido de formato OGG que se guarde en la carpeta "sonidos" dentro 
	de la carpeta de misión. Se utiliza un objeto como la fuente del sonido.

    Argumentos:
    0: objeto que será la fuente del sonido <OBJECT>
	1: nombre del archivo de sonido <STRING>

    Retorna:
    --

    Ejemplos:
    [megafono_1, "despertar.ogg"] call ZR_fnc_reproducirSonido3D;

    Pública: Sí
	
	Se asume que el archivo está dentro de la carpeta "sonidos" y es formato OGG.
	A pesar de lo que dice la wiki, según mis pruebas esta función tiene que correr 
	en todas las máquinas para que todos oigan el sonido.
 */

//Tocar la canción
private _soundPath = [(str missionConfigFile), 0, -15] call BIS_fnc_trimString;
private _soundToPlay = _soundPath + format["sonidos\%1", _sonido];
playSound3D [_soundToPlay, _objeto]; 