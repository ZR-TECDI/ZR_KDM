/*
    initServer.sqf
    
    Descripción:
    Este script de evento corre en el servidor cuando éste inicializa. Lo ocupamos para inicializar variables
    y transmitiras a los clientes.

    La parte de este script que indica como "espacio para variables de misión" está dedicado para que el
    editor de la misión inicie las variables que necesite para su misión en particular y luego la transmita 
    a los jugadores del mismo modo que se transmiten las variables de sistema.

    Parámetros:
    --
    Retorna:
    --
*/
desconectados = [];

//Para las desconexiones
addMissionEventHandler ["handleDisconnect", {
    params["_unit", "_id", "_uid", "_name"];
    _unit hideObjectGlobal true;
    _unit disableAI "ALL";

    _unit allowDamage false;

    true;
}];

/*
********* Variables de misión ******
*/
varEjemplo = nil;
/*
******** Variables de misión *******
*/
//Array con todas las variables que tienen que transmitirse a los jugadores cuando conectan al server
VARIABLES_PARA_TRANSMITIR = [
    "varEjemplo"
];

