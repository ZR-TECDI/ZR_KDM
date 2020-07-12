/*
    Autor: Riquelme
    Desc : Registra una caja y su contenido para ser replicada y usada como caja de suministros
    durante las misiones. Esta función está diseñada para ser usada con un módulo en 3DEN editor.

    La forma de uso es crear una caja cualquiera en 3DEN, llenarla con lo que sea que uno quiera y
    enlazarle una entidad lógica que llama a esta función para registrar dicha caja. Luego se pueden sincronizar
    objetos a dicha entidad lógica para registrarlos como origen de la acción de empaquetar cajas.

    Ejemplo:

    ["Suministros médicos", this] call ZR_fnc_registrarCajaSuministros;

    Argumentos:
    0: Texto a mostrar en la acción de solicitud <STRING>
    1: Objeto que representa al módulo. De aquí obtendrémos la lista de sincronizados <OBJECT>

    Retorna:
    --

    Pública: Sí
 */

params ["_nombre", "_sincronizados"];

//Tomar objetos sincronizados al módulo
_sincronizados = synchronizedObjects _sincronizados;

//No se admiten registros sin cajas
if (count _sincronizados < 1) exitWith {};

private _caja = _sincronizados select 0;

//Si no hay objetos para agregar acción, agrégalo a la misma caja
if (count _sincronizados == 1) then {
    _sincronizados = [_caja, _caja];
};

private _className = typeOf _caja;
private _cargo = [getItemCargo _caja, getWeaponCargo _caja, getMagazineCargo _caja, getBackpackCargo _caja];

//Función privada para agregar la acción
private _x_fnc_agregarAccion = {
    params["_objeto", "_nombre", "_className", "_cargo"];

    _objeto addAction
    [
        format ["Empaquetar caja de suministros (%1)", _nombre],
        {
            params ["_target", "_caller", "_actionId", "_arguments"];

            private _className = _arguments select 0;
            private _cargo = _arguments select 1;
            private _pos = objnull;
            
            // if (count ("ZonaCarga" call ZR_fnc_encontrarObjetosPorVariable) > 0) then {
            //     _pos = getPos (("ZonaCarga" call ZR_fnc_encontrarObjetosPorVariable) select 0);
            // } else {
            //     _pos = position _caller;
            // };

            if (!isNil "ZonaCarga") then {
                _pos = getPos ZonaCarga;
            } else {
                _pos = getPos _caller;
            };

            private _cajita = _className createVehicle _pos;
            systemChat "Empaquetando...";
            clearItemCargoGlobal _cajita;
            clearWeaponCargoGlobal _cajita;
            clearMagazineCargoGlobal _cajita;
            clearBackpackCargoGlobal _cajita;

            x_fnc_agregadoTxt = {
                params ["_class", "_cantidad"];
                
                private _name = "";
                private _config = "";

                switch true do
                {
                    case(isClass(configFile >> "CfgMagazines" >> _class)): {_config = "CfgMagazines"};
                    case(isClass(configFile >> "CfgWeapons" >> _class)): {_config = "CfgWeapons"};
                    case(isClass(configFile >> "CfgVehicles" >> _class)): {_config = "CfgVehicles"};
                    case(isClass(configFile >> "CfgGlasses" >> _class)): {_config = "CfgGlasses"};
                };

                _name = [configFile >> _config >> _class] call BIS_fnc_displayName;
                systemChat format ["Agregado: %1 (%2)", _name, _cantidad];
            };

            _cargo apply {
                for "_i" from 0 to (count (_x select 0) -1) do {

                    private _objeto = _x select 0 select _i;
                    private _cantidad = _x select 1 select _i;

                    switch (_x) do {
                        case (_cargo select 0): {
                            _cajita addItemCargoGlobal [_objeto, _cantidad];
                            [_objeto, _cantidad] call x_fnc_agregadoTxt;
                        };
                        case (_cargo select 1): {
                            _cajita addWeaponCargoGlobal [_objeto, _cantidad];
                            [_objeto, _cantidad] call x_fnc_agregadoTxt;
                        };
                        case (_cargo select 2): {
                            _cajita addMagazineCargoGlobal [_objeto, _cantidad];
                            [_objeto, _cantidad] call x_fnc_agregadoTxt;
                        };
                        case (_cargo select 3): {
                            _cajita addBackpackCargoGlobal [_objeto, _cantidad];
                            [_objeto, _cantidad] call x_fnc_agregadoTxt;
                        };
                    };
                };
            };

            systemChat "Caja empaquetada";
        },
        [_className, _cargo],
        1.5,    
        true,    
        true,    
        "",        
        "true", 
        3,        
        false,    
        "",        
        ""        
    ];
};

for "_i" from 0 to (count (_sincronizados) - 1) do {
    if (_i != 0) then {
        [_sincronizados select _i, _nombre, _className, _cargo] call _x_fnc_agregarAccion;
    };
};

