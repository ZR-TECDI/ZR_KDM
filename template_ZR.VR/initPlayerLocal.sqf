[] execVM "dmb\dmb_addAction.sqf";

//Esperar a que el jugador exista
waitUntil {not isNull player};
//Poner arma al hombro
player action ["SWITCHWEAPON",player,player,-1];
//Hacer visible al jugador (en caso que se haya desconectado)
[player] execVM "scripts\hacerVisible.sqf";

