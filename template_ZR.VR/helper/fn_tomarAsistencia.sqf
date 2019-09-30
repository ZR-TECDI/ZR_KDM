/*
    Autor: Riquelme
    Desc : Helper que agrega un eventHandler para cada vez que alguien se conecta o desconecta y escribe en el RPT 
    el evento.

    Argumentos:
    --

    Retorna:
    --

    Ejemplos:
    --

    Pública: No
 */

if(!isServer) exitWith {};

addMissionEventHandler ["PlayerConnected", {
    params ["_id", "_uid", "_name"];

    diag_log format["ZRASISTENCIA: %1 conectado", _name]
}];

addMissionEventHandler ["PlayerDisconnected", {
    params ["_id", "_uid", "_name"];

    diag_log format["ZRASISTENCIA: %1 desconectado", _name]
}];