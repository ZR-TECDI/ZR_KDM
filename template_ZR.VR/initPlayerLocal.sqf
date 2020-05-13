//Esperar a que el jugador exista
waitUntil {not isNull player};
//Poner arma al hombro
player action ["SWITCHWEAPON",player,player,-1];

