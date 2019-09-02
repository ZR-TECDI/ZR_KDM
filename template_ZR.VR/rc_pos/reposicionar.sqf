/*
Este script reposiciona al jugador en caso de desconexión durante una operación.

Parámetros:
    0 -- _eleccion -> Integer, 0 = posición de deconexión, 1 = posición de PR, 2 = posición del líder.

*/
params ["_eleccion"];

fn_teleport = {
    params["_pos"];

    cutText ["", "BLACK", 2];
    sleep 2;
    player setPos _pos;
    cutText ["", "BLACK IN", 2];
};

switch _eleccion do{
    case 0:{
        //Posicion de desconexión, no hacer nada
        closeDialog 0;
    };

    case 1:{
        //Posición de PR
        systemChat "No hay punto de reunión establecido para esta misión.";
    };
    case 2:{
        //Posición del líder
        private _lider = leader player;
        //Comprobar si el líder está en un vehículo
        if (not (isNull objectParent _lider) ) then{
            private _vehiculo = objectParent _lider;
            //Comprobar si el vehículo tiene asientos libres
            private _asientosLibres = ([(typeOf _vehiculo), true] call BIS_fnc_crewCount ) - fullCrew _vehiculo;
            if(_asientosLibres > 0) then{
                //Mover al jugador al vehículo en el primer asiento libre
                systemChat "Líder en vehículo, intentaremos ponerte dentro";
                //Comprobar si el jugador está en un vehículo
                player moveInAny _vehiculo;
                if(isNull objectParent player) then {systemChat "Fallamos en intentar ponerte dentro del vehículo."};
            } else {
                systemChat "Líder en vehículo, pero no hay asientos libres."};

        }else{
            //Mover al jugador a una posición segura cerca del líder.
            private _pos = getPosATL _lider;
            _pos = [_pos, 1, 10] call BIS_fnc_findSafePos;
            [_pos] call fn_teleport;
        };
        //Cerrar la pantalla
        closeDialog 0;
    };
};