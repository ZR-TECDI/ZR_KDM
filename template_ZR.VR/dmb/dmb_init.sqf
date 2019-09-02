if(isNil "dmb_settingsLoaded") then{
    // loading user settings
    [] execVM "dmb\dmb_settings.sqf";
};

waitUntil {not isNil "dmb_settingsLoaded"};

////////////////////////////////////////////////////////////////////////////////
// category text
DMB_CAT_TXT_1 = 10181;
DMB_CAT_TXT_2 = 10182;
DMB_CAT_TXT_3 = 10183;

// main board buttons
DMB_CTRL_BT_1 = 101811;
DMB_CTRL_BT_2 = 101812;
DMB_CTRL_BT_3 = 101813;
DMB_CTRL_BT_4 = 101814;
DMB_CTRL_BT_5 = 101815;
DMB_CTRL_BT_6 = 101816;
DMB_CTRL_BT_7 = 101817;
DMB_CTRL_BT_8 = 101818;
DMB_CTRL_BT_9 = 101819;
DMB_CTRL_BT_10 = 101820;
DMB_CTRL_BT_11 = 101821;
DMB_CTRL_BT_12 = 101822;
DMB_CTRL_BT_13 = 101823;
DMB_CTRL_BT_14 = 101824;
DMB_CTRL_BT_15 = 101825;

// aux board left
DMB_CTRL_AUX_L_1 = 101830;
DMB_CTRL_AUX_L_2 = 101831;
DMB_CTRL_AUX_L_3 = 101833;
DMB_CTRL_AUX_L_4 = 101834;
DMB_CTRL_AUX_L_5 = 101835;

// aux board right
DMB_CTRL_AUX_R_1 = 101841;
DMB_CTRL_AUX_R_2 = 101842;
DMB_CTRL_AUX_R_3 = 101843;
DMB_CTRL_AUX_R_4 = 101844;
DMB_CTRL_AUX_R_5 = 101845;

////////////////////////////////////////////////////////////////////////////////////


DMB_allCatNames        = [DMB_CTRL_NAME_1,DMB_CTRL_NAME_2,DMB_CTRL_NAME_3];
DMB_AllCatIDC          = [DMB_CAT_TXT_1,DMB_CAT_TXT_2,DMB_CAT_TXT_3];

DMB_AllButEnables     = [DMB_ENABLE_1,
                        DMB_ENABLE_2,
                        DMB_ENABLE_3,
                        DMB_ENABLE_4,
                        DMB_ENABLE_5,
                        DMB_ENABLE_6,
                        DMB_ENABLE_7,
                        DMB_ENABLE_8,
                        DMB_ENABLE_9,
                        DMB_ENABLE_10,
                        DMB_ENABLE_11,
                        DMB_ENABLE_12,
                        DMB_ENABLE_13,
                        DMB_ENABLE_14,
                        DMB_ENABLE_15,
                        DMB_ENABLE_AL1,
                        DMB_ENABLE_AL2,
                        DMB_ENABLE_AL3,
                        DMB_ENABLE_AL4,
                        DMB_ENABLE_AL5,
                        DMB_ENABLE_AR1,
                        DMB_ENABLE_AR2,
                        DMB_ENABLE_AR3,
                        DMB_ENABLE_AR4,
                        DMB_ENABLE_AR5];

DMB_allButText =       [DMB_TEXT_1,
                        DMB_TEXT_2,
                        DMB_TEXT_3,
                        DMB_TEXT_4,
                        DMB_TEXT_5,
                        DMB_TEXT_6,
                        DMB_TEXT_7,
                        DMB_TEXT_8,
                        DMB_TEXT_9,
                        DMB_TEXT_10,
                        DMB_TEXT_11,
                        DMB_TEXT_12,
                        DMB_TEXT_13,
                        DMB_TEXT_14,
                        DMB_TEXT_15,
                        DMB_TEXT_AL1,
                        DMB_TEXT_AL2,
                        DMB_TEXT_AL3,
                        DMB_TEXT_AL4,
                        DMB_TEXT_AL5,
                        DMB_TEXT_AR1,
                        DMB_TEXT_AR2,
                        DMB_TEXT_AR3,
                        DMB_TEXT_AR4,
                        DMB_TEXT_AR5];

DMB_allButIDC   =       [DMB_CTRL_BT_1,
                        DMB_CTRL_BT_2,
                        DMB_CTRL_BT_3,
                        DMB_CTRL_BT_4,
                        DMB_CTRL_BT_5,
                        DMB_CTRL_BT_6,
                        DMB_CTRL_BT_7,
                        DMB_CTRL_BT_8,
                        DMB_CTRL_BT_9,
                        DMB_CTRL_BT_10,
                        DMB_CTRL_BT_11,
                        DMB_CTRL_BT_12,
                        DMB_CTRL_BT_13,
                        DMB_CTRL_BT_14,
                        DMB_CTRL_BT_15,
                        DMB_CTRL_AUX_L_1,
                        DMB_CTRL_AUX_L_2,
                        DMB_CTRL_AUX_L_3,
                        DMB_CTRL_AUX_L_4,
                        DMB_CTRL_AUX_L_5,
                        DMB_CTRL_AUX_R_1,
                        DMB_CTRL_AUX_R_2,
                        DMB_CTRL_AUX_R_3,
                        DMB_CTRL_AUX_R_4,
                        DMB_CTRL_AUX_R_5];

// changing category texts 
dmb_fnc_changeCategoryNames = {
    params["_name"];

    if(!(_name isEqualTo "")) then{
        private _index = DMB_allCatNames find _name;
        private _idc = DMB_AllCatIDC select _index;
        ctrlSetText [_idc, format["%1", _name]];
    };
};

// Disabling buttons
dmb_fnc_hideDisabledButtons = {
    for "_index" from 0 to 24 do{
        private _enable = DMB_AllButEnables select _index;

        if(!_enable) then{
            private _idc = DMB_allButIDC select _index;
            ctrlShow [_idc, false];
        };
    };
};

// Changing buttons text
dmb_fnc_changeButtonsText = {
    params["_text"];

    if(!(_text isEqualTo "")) then {
        private _index = DMB_allButText find _text;
        private _idc = DMB_allButIDC select _index;
        ctrlSetText [_idc, format["%1", _text]];
    };
};

// creating the dialog and verying
private _ok = createDialog "dungeonMasterBoard";
if(!_ok) exitWith{
    systemChat "ERROR: Couldn't open DM Board interface!";
    diag_log "DMB_DEBUG: ERROR! Couldn't initiate Dungeon master board, is the script properly installed in your mission?";
};

call dmb_fnc_hideDisabledButtons;

DMB_allCatNames apply {
    [_x] spawn dmb_fnc_changeCategoryNames;
    };
DMB_allButText apply {
    [_x] spawn dmb_fnc_changeButtonsText
    };
