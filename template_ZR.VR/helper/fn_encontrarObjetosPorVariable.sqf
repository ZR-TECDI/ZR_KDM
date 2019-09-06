/*
    Autor: Riquelme
    Desc : Helper que busca todos los objetos de la misión con algo en común en su nombre de variable.

    Argumentos:
    0: Nombre de variable <STRING>

    Retorna:
    array con todos los objetos en la misión que compartan un nombre de variable <ARRAY>

    Ejemplos:
    "civil_enfermo_" call ZR_fnc_encontrarObjetosPorVariable; 
    Retornaría un array con [civil_enfermo_1, civil_enfermo_2] si existieran en la misión.

    Pública: No
 */

params ["_nombreVariable"];

private _resultado = allVariables missionNamespace select {_x find _nombreVariable == 0};
_resultado = _resultado apply {missionNameSpace getVariable _x};

_resultado;