/*
    Autor: Riquelme
    Desc : Hace visibles a los jugadores luego de una desconexión.

    Argumentos:
    0: Jugador <OBJECT>

    Retorna:
    --

    Ejemplos:
    --

    Pública: No

 */

params ["_jugador"];

//Esperando que el jugador esté definido en el mundo.
waitUntil { not isNull player };

[_jugador, false] remoteExec ["hideObjectGlobal", 2];
player allowDamage true;
diag_log format["%1 es ahora visible y perece al daño", name player];