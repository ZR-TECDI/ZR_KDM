/*
    Autor: Riquelme
    Desc : Inicia diálogo en texto para los jugadores en un área particular
    
    Argumentos:
    0: Array con el nombre variable que contiene cada línea de diálogo. <ARRAY>
    1: tipo de chat (usado para definir el color de texto). <STRING>
        Posibles valores: 
                - "SIDE"    => Toma el color del bando del hablante
                - "GLOBAL"  => Blanco
                - "VEHICLE" => Dorado
                - "COMMAND" => Amarillo 
                - "GROUP"   => Verde brillante 
                - "DIRECT"  => Blanco 
                - "CUSTOM"  => Naranja
                - "SYSTEM"  => Gris
                - "BLUFOR"  => Azul
                - "OPFOR"   => Rojo
                - "GUER"    => Verde 
                - "CIV"     => Rosa  
    2: Multiplicador de pausa, usado para calcular el tiempo entre cada línea. Default 0.15 <FLOAT>
    3: Mostrar fondo. <BOOL>
	4: origen. <OBJECT>
	5: radio en metros desde origen. <INTEGER>

    Retorna:
    True <BOOL>

    Ejemplo:

    La definición de líneas de diálogo se hace de la siguiente forma: 

        linea_1 = ["NOMBRE DEL HABLANTE", "DIÁLOGO", nombre_variable_del_personaje];
        linea_2 = ["Sargento Jäger", "Usted me debe unas vueltas", jager];

    El llamado a la función se hace del siguiente modo:
    
        [[linea_1, linea_2], "BLUFOR", 0.15, true, npc_hablante, 10] call ZR_fnc_dialogoNPCGlobal;

    Pública: Sí
 */

 params ["_lineasDeTexto", 
 		"_tipoDeChat", 
		 ["_multiplicadorPausa", 0.15], 
		 ["_mostrarFondo", True],
		 "_origen", "_radio"];


allPlayers - entities "HeadlessClient_F" apply {
    if (_x distance _origen =< _radio) then {
		private _id = _x call zr_fnc_getIDJugador;
		[_lineasDeTexto, 
		_tipoDeChat, 
		_multiplicadorPausa, 
		_mostrarFondo] remoteExec ["ZR_fnc_dialogoNPC", _id]
	};
};