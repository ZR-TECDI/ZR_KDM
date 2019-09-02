waitUntil {not isNull player};

// private _isDM = player getVariable ["esMando", false];

private _isDM =  call ZR_fnc_checkPlayerAdmins;

if (!_isDM) exitWith{
    diag_log "DMB_DEBUG: Player is not DM";
};

player addAction ["Dungeon Master Board", {
    [] execVM "dmb\dmb_init.sqf";
}, [], 0, false, true, "", "call ZR_fnc_checkPlayerAdmins", -1];

player addEventHandler[
    "Respawn", {
        params["_unit", "_corpse"];

        _unit setVariable ["esMando", true];

        [] execVM "dmb\dmb_Addaction.sqf";
    }
];