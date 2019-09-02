/*
    Autor original: Revo y Thomas Ryan.
    Desc          : Muestra texto a modo de subtítulos, centrados y en la parte inferior de la pantalla. Si se especifica
    un personaje con su nombre variable, dicho personaje moverá los labios de forma aleatoria para simular el habla.

    Nótese que cada línea de diálogo debe ser definida (mirar ejemplo abajo) y luego llamar con todas las líneas juntas en
    un array a esta función.

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
    true

    Ejemplo:

    La definición de líneas de diálogo se hace de la siguiente forma: 

        linea_1 = ["NOMBRE DEL HABLANTE", "DIÁLOGO", nombre_variable_del_personaje];
        linea_2 = ["Sargento Jäger", "Usted me debe unas vueltas", jager];

    El llamado a la función se hace del siguiente modo:
    
        [[linea_1, linea_2], "BLUFOR", 0.15, true] call ZR_fnc_dialogoNPC;


    Pública: Sí

*/

#define FADE_DURATION 0.5
#define BACKGROUND_COLOUR [0,0,0,0.4]
#define BACKGROUND_H_COEF 0.0008

waitUntil {isNil "Revo_fnc_simpleConversation_running"};
Revo_fnc_simpleConversation_running = true;

private _lines = param [0,[["Speaker","Subtitle"]],[[]]];
private _colour = param [1,"SIDE",[""]];
private _breakMultiplier = param [2,0.1,[0]];
private _showBackground = param [3,false,[false]];


//Select HEX colour from given string
private _colourHTML = switch (toUpper _colour) do
{
    case "SIDE":     {"#00ccff"};
    case "GLOBAL":     {"#d7d7d9"};
    case "VEHICLE": {"#fbd40b"};
    case "COMMAND": {"#e5e760"};
    case "GROUP":     {"#beee7e"};
    case "DIRECT":     {"#fffffb"};
    case "CUSTOM":    {"#ec5a29"};
    case "SYSTEM":    {"#8a8a88"};
    case "BLUFOR":     {([WEST,false] call BIS_fnc_sideColor) call BIS_fnc_colorRGBtoHTML};
    case "OPFOR":     {([EAST,false] call BIS_fnc_sideColor) call BIS_fnc_colorRGBtoHTML};
    case "GUER":     {([INDEPENDENT,false] call BIS_fnc_sideColor) call BIS_fnc_colorRGBtoHTML};
    case "CIV":     {([CIVILIAN,false] call BIS_fnc_sideColor) call BIS_fnc_colorRGBtoHTML};
};

private _fnc_showSubtitles =
{
    params ["_from", "_text","_colourHTML","_break","_showBackground"];

    // Create display and control
    disableSerialization;
    titleRsc ["RscDynamicText", "PLAIN"];
    private "_display";
    waitUntil {_display = uiNamespace getVariable "BIS_dynamicText"; !(isNull _display)};
    private _ctrl = _display displayCtrl 9999;
    uiNamespace setVariable ["BIS_dynamicText", displayNull];
    private _ctrlBackground = _display ctrlCreate ["RscText",99999];

    // Position control
    private _w = 0.4 * safeZoneW;
    private _x = safeZoneX + (0.5 * safeZoneW - (_w / 2));
    private _y = safeZoneY + (0.73 * safeZoneH);
    private _h = safeZoneH;

    _ctrl ctrlSetPosition [_x,_y,_w,_h];

    // Hide control
    _ctrl ctrlSetFade 1;
    _ctrl ctrlCommit 0;
    if (_showBackground) then
    {
        _ctrlBackground ctrlSetPosition [_x,_y,_w,((count _text) / 2000) max 0.035];
        _ctrlBackground ctrlSetBackgroundColor BACKGROUND_COLOUR;
        _ctrlBackground ctrlSetFade 1;
        _ctrlBackground ctrlCommit 0;
    };
    // Show subtitle
    _text = parseText format ["<t align = 'center' shadow = '2' size = '0.52'><t color = '%1'>" + _from + ":</t> <t color = '#d0d0d0'>" + _text + "</t></t>",_colourHTML];
    _ctrl ctrlSetStructuredText _text;
    _ctrl ctrlSetFade 0;
    _ctrl ctrlCommit FADE_DURATION;
    if (_showBackground) then
    {
        _ctrlBackground ctrlSetFade 0;
        _ctrlBackground ctrlCommit FADE_DURATION;
    };
    sleep _break;

    // Hide subtitle
    _ctrl ctrlSetFade 1;
    _ctrl ctrlCommit FADE_DURATION;

    if (_showBackground) then
    {
        _ctrlBackground ctrlSetFade 1;
        _ctrlBackground ctrlCommit FADE_DURATION;
    };
};

//Loop through all given lines
for "_i" from 0 to (count _lines) - 1 do
{
    private _nameSpeaker = (_lines select _i) select 0;
    private _currentLine = (_lines select _i) select 1;
    private _speaker = (_lines select _i) param [2,objNull,[objNull]];
    private _break = count _currentLine * _breakMultiplier;

    if !(isNull _speaker) then {_speaker setRandomLip true};
    private _handle = [_nameSpeaker,_currentLine,_colourHTML,_break,_showBackground] spawn _fnc_showSubtitles;
    waitUntil {scriptDone _handle};

    if !(isNull _speaker) then {_speaker setRandomLip false};

    sleep FADE_DURATION + 0.5;
};

Revo_fnc_simpleConversation_running = nil;

true