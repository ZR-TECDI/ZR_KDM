/*
    Autor: Riquelme
    Desc : Permite las acciones de bandera. Debe llamarse en el init de la bandera.

    Argumentos:
    0: _bandera <OBJECT>

    Retorna:
    --

    Ejemplos:
    --

    Pública: No

 */

params ["_bandera"];

x_fnc_ponerBandera = {
    params ["_bandera"];

    [_bandera, "img\banderaZR.jpg"] remoteExec ["setFlagTexture", 2];
    [_bandera, 0] remoteExec ["setFlagAnimationPhase", 0];
};

x_fnc_izarBandera = {
    params ["_bandera"];

    [_bandera, 1] call BIS_fnc_animateFlag;
};

x_fnc_mediaAsta = {
    params ["_bandera"];

    [_bandera, 0.5] call BIS_fnc_animateFlag;
};

x_fnc_bajarBandera = {
    params ["_bandera"];

    [_bandera, 0] call BIS_fnc_animateFlag;
 
};

x_fnc_recogerBandera = {
    params ["_bandera"];

    [_bandera, ""] remoteExec ["setFlagTexture", 2];
};


// Agregar acciones
_bandera addAction 
[
    "Poner bandera", 
    {
        params ["_target", "_caller", "_actionId", "_arguments"];
        _caller playAction "PutDown";
        _target call x_fnc_ponerBandera;
    },
    [],
    1.5, 
    true, 
    true, 
    "",
    "flagTexture _target == """" ",
    3,
    false,
    "",
    ""
];

_bandera addAction 
[
    "Izar bandera", 
    {
        params ["_target", "_caller", "_actionId", "_arguments"];
        _caller playAction "PutDown";
        _target call x_fnc_izarBandera;
    },
    [],
    1.5, 
    true, 
    true, 
    "",
    "((flagTexture _target != """") AND ((flagAnimationPhase _target) != 1))",
    3,
    false,
    "",
    ""
];

_bandera addAction 
[
    "A media asta", 
    {
        params ["_target", "_caller", "_actionId", "_arguments"];
        _caller playAction "PutDown";
        _target call x_fnc_mediaAsta;
    },
    [],
    1.5, 
    true, 
    true, 
    "",
    "((flagTexture _target != """") AND ((flagAnimationPhase _target) != 0.5))",
    3,
    false,
    "",
    ""
];

_bandera addAction 
[
    "Bajar bandera", 
    {
        params ["_target", "_caller", "_actionId", "_arguments"];
        _caller playAction "PutDown";
        _target call x_fnc_bajarBandera;
    },
    [],
    1.5, 
    true, 
    true, 
    "",
    "((flagTexture _target != """") AND ((flagAnimationPhase _target) != 0))",
    3,
    false,
    "",
    ""
];

_bandera addAction 
[
    "Recoger Bandera", 
    {
        params ["_target", "_caller", "_actionId", "_arguments"];
        _caller playAction "PutDown";
        _target call x_fnc_recogerBandera;
    },
    [],
    1.5, 
    true, 
    true, 
    "",
    "((flagTexture _target != """") AND ((flagAnimationPhase _target) == 0))",
    3,
    false,
    "",
    ""
];