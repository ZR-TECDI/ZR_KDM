/*
    Autor: Riquelme
    Desc : Devuelve el ID del jugador pasado en parámetro para usar luego con 
	remoteExec.

    Argumentos:
    0: _jugador

    Retorna:
    - ID del jugador <INTEGER>

    Ejemplos:
    --

    Pública: No
 */

params["_jugador"];

private _id = [_jugador] remoteExec ["owner", 2];

_id;