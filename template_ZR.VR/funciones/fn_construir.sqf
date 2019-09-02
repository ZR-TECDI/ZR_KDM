/*
    Autor: Riquelme
    Desc : //TODO función en estado WIP
 */

params ["_estructura", "_tiempo"];

private _pos = getPosATL _estructura;
private _porte = boundingBoxReal _estructura;
private _p1 = _porte select 0;
private _p2 = _porte select 1;
private _alturaObjeto = abs ((_p2 select 2) - (_p1 select 2));
_tiempoActual = time;
_tiempoFinal = _tiempoActual + _tiempo;
_alturaASubir = _alturaObjeto / _tiempo;


//Cambiar posición de la estructura para estar bajo tierra.
_estructura enableSimulationGlobal false;
// _estructura setPosATL [_pos select 0, _pos select 1, _pos select 2 -_alturaObjeto];
_estructura hideObject true;
estructura = _estructura;
tiempo = _tiempo;
pos = _pos;
alturaASubir = _alturaASubir;

//Actualizar posición de la estructura
// [_estructura, _pos, _alturaASubir, _tiempo, _tiempoActual, _tiempoFinal] spawn ZR_fnc_actualizarPosEstructura;
player playMove "AinvPknlMstpSnonWrflDr_medic5_old";

// Barra de tiempo
[_tiempo, [], {
    systemChat "Construcción finalizada con éxito.";
    estructura enableSimulationGlobal true;
    estructura hideObject false;
    // [estructura, pos, alturaASubir, tiempo] spawn ZR_fnc_actualizarPosEstructura;
    estructura = nil;
    pos = nil;
    alturaASubir = nil;
    tiempo = nil;
    player switchMove "";
    }, 
    {
    systemChat "Se ha interrumpido la construcción.";
    deleteVehicle estructura;
    estructura = nil;
    pos = nil;
    alturaASubir = nil;
    tiempo = nil;
    player switchMove "";
    }, 
    "Construyendo..."
] call ace_common_fnc_progressBar;
