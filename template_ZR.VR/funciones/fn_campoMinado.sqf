/*
    Autor: Riquelme
    Desc : Crea un campo minado utilizando un área designada en el editor.

    Argumentos:
    0: Área que se pretende minar <OBJECT/STRING/ARRAY>
    1: Nombre clase de la mina a colocar <STRING>
    2: Cantidad de minas para poblar el área <INTEGER>
    3: Opcional, rotación en la que deberían quedar mirando las minas (útil para minas de cable) <INTEGER>

    Retorna:
    True al finalizar el bombardeo, false si no encontró posición válida <BOOL>

    Ejemplos:
    ["zonaMinada", "APERSMine", 20] call ZR_fnc_campoMinado; Poblará la zona "zonaMinada" con 20 minas 
    antipersonales.

    Pública: Sí
 */

params ["_area", "_mina", "_cantidad", ["_rotacion", nil]];

private _contador = _cantidad;

while{_contador > 1} do{
    private _pos = _area call BIS_fnc_randomPosTrigger;
    private _mineColocada = createVehicle [_mina, [_pos select 0, _pos select 1, 0], [], 0, "NONE"];
    if(!isNil "_rotacion") then {
        _mineColocada setdir _rotacion;
    };
    _mineColocada enableDynamicSimulation true;
    _contador = _contador - 1;
};