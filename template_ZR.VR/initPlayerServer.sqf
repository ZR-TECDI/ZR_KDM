/*
	initPlayerServer.sqf
	
	Descripción:
	Este script de evento corre en el servidor cada vez que un cliente se conecta al mismo (antes de inicializar y 
	tener personaje).

	Parámetros:
		0:
			OBJETO - Representa el objeto con que se define el cliente que conecta.
		1:
			BOOLEAN - Es true si el cliente que conecta es JIP (conectó después de la pantalla de briefing).

	Retorna:
	--
*/

params["_player", "_didJip"];

private _idPlayer = owner _player;

//Transmitir variables de misión al jugador cuando conecta
VARIABLES_PARA_TRANSMITIR apply {_idPlayer publicVariableClient _x};

