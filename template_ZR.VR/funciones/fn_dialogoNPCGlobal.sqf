/*
    Autor: Riquelme
    Desc : Inicia diálogo en texto para todos los jugadores presentes
    
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

    Retorna:
    True <BOOL>

    Ejemplo:

    La definición de líneas de diálogo se hace de la siguiente forma: 

        linea_1 = ["NOMBRE DEL HABLANTE", "DIÁLOGO", nombre_variable_del_personaje];
        linea_2 = ["Sargento Jäger", "Usted me debe unas vueltas", jager];

    El llamado a la función se hace del siguiente modo:
    
        [[linea_1, linea_2], "BLUFOR", 0.15, true] call ZR_fnc_dialogoNPCGlobal;

    Pública: Sí
 */

 params ["_lineasDeTexto", 
 		"_tipoDeChat", 
		 ["_multiplicadorPausa", 0.15], 
		 ["_mostrarFondo", True]];

[_lineasDeTexto, _tipoDeChat, _multiplicadorPausa, _mostrarFondo] remoteExec ["ZR_fnc_dialogoNPC", 0, false]
