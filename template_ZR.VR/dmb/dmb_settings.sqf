/*********************************
EN Instructions:

    DMB_ENABLE_X -> Will enable/disable said button. True to enable, false to disable.
    When disabled, the button will not appear in the board.

    DMB_CODE_X -> Is the code the button will execute once clicked. 

        Example: DMB_CODE_1 = {[] execVM "myScript.sqf"};

    DMB_TEXT_X -> is the text that will be displayed on the button.
    If left as "" it will take and display the default text. 

ES Instrucciones:

    DMB_ENABLE_X -> Va a habilitar o deshabilitar un botón en particular. True para mostrar, false para ocultar.

    DMB_CODE_X -> Es el código que se ejecutará al apretar el botón.

        Ejemplo: DMB_CODE_1 = {[] execVM "mi_codigo.sqf"};

    DMB_TEXT_X -> Es el texto que aparecerá en el botón. Si se deja vacío, aparece el texto default.
    Para quitar el texto, llena con un espacio " ".

*/

// Section names
DMB_CTRL_NAME_1 = ""; // Middle section name
DMB_CTRL_NAME_2 = "Flujo de la misión"; // Left section name
DMB_CTRL_NAME_3 = "Acciones de zeus"; // Right section name

// Main board
/******************************************/
//Button 1
DMB_ENABLE_1 = true;
DMB_CODE_1 = {puntoSpawn = "ruso_spawn_1"};
DMB_TEXT_1 = "";

//Button 2
DMB_ENABLE_2 = true;
DMB_CODE_2 = {puntoSpawn = "ruso_spawn_2"};
DMB_TEXT_2 = "";

//Button 3
DMB_ENABLE_3 = true;
DMB_CODE_3 = {puntoSpawn = "ruso_spawn_3"};
DMB_TEXT_3 = "";

//Button 4
DMB_ENABLE_4 = true;
DMB_CODE_4 = {puntoSpawn = "ruso_spawn_4"};
DMB_TEXT_4 = "";

//Button 5
DMB_ENABLE_5 = false;
DMB_CODE_5 = {systemChat "5"};
DMB_TEXT_5 = "";

//Button 6
DMB_ENABLE_6 = false;
DMB_CODE_6 = {systemChat "6"};
DMB_TEXT_6 = "";

//Button 7
DMB_ENABLE_7 = false;
DMB_CODE_7 = {systemChat "7"};
DMB_TEXT_7 = "";

//Button 8
DMB_ENABLE_8 = false;
DMB_CODE_8 = {puntoSpawn = selectRandom["ruso_spawn_1", "ruso_spawn_2", "ruso_spawn_3", "ruso_spawn_4"]};
DMB_TEXT_8 = "RANDOM";

//Button 9
DMB_ENABLE_9 = false;
DMB_CODE_9 = {systemChat "9"};
DMB_TEXT_9 = "";

//Button 10
DMB_ENABLE_10 = false;
DMB_CODE_10 = {systemChat "10"};
DMB_TEXT_10 = "";

//Button 11
DMB_ENABLE_11 = false;
DMB_CODE_11 = {systemChat "11"};
DMB_TEXT_11 = "";

//Buttoin 12
DMB_ENABLE_12 = false;
DMB_CODE_12 = {systemChat "12"};
DMB_TEXT_12 = "";

//Button 13
DMB_ENABLE_13 = true;
DMB_CODE_13 = {[lata] remoteExec ["ZR_fnc_rusosMegafono",0,true]};
DMB_TEXT_13 = "megafono";

//Button 14
DMB_ENABLE_14 = true;
DMB_CODE_14 = {systemChat "14"};
DMB_TEXT_14 = "";

//Button 15
DMB_ENABLE_15 = true;
DMB_CODE_15 = {systemChat "15"};
DMB_TEXT_15 = "";

/*************************************/

// Left board
/**************************************/
//Button 1
DMB_ENABLE_AL1 = true;
DMB_CODE_AL1 = {["debil", puntoSpawn] call ZR_fnc_oleadaInf;};
DMB_TEXT_AL1 = "Oleada débil";

//Button 2
DMB_ENABLE_AL2 = true;
DMB_CODE_AL2 = {["normal", puntoSpawn] call ZR_fnc_oleadaInf;};
DMB_TEXT_AL2 = "Oleada normal";

//Button 3
DMB_ENABLE_AL3 = true;
DMB_CODE_AL3 = {["normal", puntoSpawn] call ZR_fnc_oleadaInf;};
DMB_TEXT_AL3 = "Oleada mecanizada";

//Button 4
DMB_ENABLE_AL4 = true;
DMB_CODE_AL4 = {[puntoSpawn] call ZR_fnc_oleadaTank;};
DMB_TEXT_AL4 = "Tanque";

//Button 5
DMB_ENABLE_AL5 = true;
DMB_CODE_AL5 = {};
DMB_TEXT_AL5 = "";

// Right board
/**************************************/
//Button 1
DMB_ENABLE_AR1 = true;
DMB_CODE_AR1 = {["EveryoneLost"] remoteExec ["BIS_fnc_endMissionServer", 0]; };
DMB_TEXT_AR1 = "Acabar misión";

//Button 2
DMB_ENABLE_AR2 = true;
DMB_CODE_AR2 = {[] remoteExec ["ZR_fnc_comenzarMision",0, true]};
DMB_TEXT_AR2 = "FASE 0: comenzar misión";

//Button 3
DMB_ENABLE_AR3 = true;
DMB_CODE_AR3 = {[] remoteExec ["ZR_fnc_cuartelGestapo", 0, true]};
DMB_TEXT_AR3 = "FASE 1: cuartel";

//Button 4
DMB_ENABLE_AR4 = true;
DMB_CODE_AR4 = {[] remoteExec ["ZR_fnc_asalto", 0, true]};
DMB_TEXT_AR4 = "FASE 2: asalto";

//Button 5
DMB_ENABLE_AR5 = true;
DMB_CODE_AR5 = {[] remoteExec ["ZR_fnc_captura", 0, true]};
DMB_TEXT_AR5 = "FASE 3: captura";


// FINISHED LOADING (don't change this)
dmb_settingsLoaded = true;
