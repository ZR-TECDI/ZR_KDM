/*
    Autor: Riquelme
    Desc : Hace una descarga de morteros en posiciones aleatorias definidas en el editor utilizando
    marcadores (para varios puntos específicos) o un activador para definir un área entera. 

    Argumentos:
    0: Tiempo en segundos que durará el bombardeo <INTEGER>
    1: Nombre variable de los marcadores/Nombre variable del activador <STRING><OBJECT>

    Retorna:
    True al finalizar el bombardeo, false si no encontró posición válida <BOOL>

    Ejemplos:
    [10, nombreTrigger] call ZR_fnc_ataqueMorteros; Bombardeará zonas aleatorias dentro de el área
    del activador nombreTrigger por 10 segundos.

    [60, "mortero_"] call ZR_fnc_ataqueMorteros; Buscará todos los marcadores que contengan "mortero_"
    en su nombre variable y los utilizará como posición aleatoria para bombardear durante 60 segundos.

    Pública: Sí
 */

params["_tiempo", "_nombreMarcador"];

// Bucle para realizar la misma acción durante el tiempo designado
private _tiempoInicio = time;
private _tiempoFinal = time + _tiempo;


// Encontrar todas las posibles posiciones de mortero
if(typeName _nombreMarcador isEqualTo "STRING") then{
    private _marcadoresDeMortero = allMapMarkers select {_x find _nombreMarcador == 0};
    
    if (_marcadoresDeMortero isEqualTo [] ) exitWith {false};

    while {_tiempoFinal > time} do {
    // 3 rondas cada vez
    private _i = 0;
    while {_i < 4} do{
        // Elegir posición al azar
        private _pos = getMarkerPos selectRandom _marcadoresDeMortero;

        //crear el mortero
        // createVehicle ["M_Mo_82mm_AT_LG", _pos, [], 0, "NONE"];
        createVehicle ["R_60mm_HE", _pos, [], 0, "NONE"];

        //Esperar un tiempo al azar entre 0,25 y 1 segundo
        sleep (random [0.25,0.5,1]);
        _i = _i + 1;
    };
    //Esperar entre 1 y 3 segundos entre cada barrido
    sleep (random [1,2,3]);
};

} else{
    while {_tiempoFinal > time} do {
        // 3 rondas cada vez
        private _i = 0;
        while {_i < 4} do{
            // Elegir posición al azar
            private _pos = [_nombreMarcador] call BIS_fnc_randomPosTrigger;
            if (_pos isEqualTo []) exitWith {false};
            
            //crear el mortero
            // createVehicle ["M_Mo_82mm_AT_LG", _pos, [], 0, "NONE"];
            createVehicle ["R_60mm_HE", _pos, [], 0, "NONE"];

            //Esperar un tiempo al azar entre 0,25 y 1 segundo
            sleep (random [0.25,0.5,1]);
            _i = _i + 1;
        };
        //Esperar entre 1 y 3 segundos entre cada barrido
        sleep (random [1,2,3]);
};


};

true;

//TODO REFACTOR PARA UTILIZAR EL WHILE UNA SOLA VEZ EN EL CÓDIGO