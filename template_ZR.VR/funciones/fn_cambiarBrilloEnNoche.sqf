/*
    Autor: Riquelme
    Desc : Comprueba si es de día o noche, aplicando un ligero retoque al brillo y color de pantalla
    cuando es de noche, para hacer viable misiones nocturnas sin NVG. 

    Argumentos:
    --

    Retorna:
    1 cuando es día, 2 cuando es noche <INTEGER>

    Ejemplos:
    player call ZR_fnc_cambiarBrilloEnNoche

    Pública: Sí

    Debe ejecutarse en la máquina local del afectado.
 */

x_fnc_esDeNoche = {
    if(sunOrMoon isEqualTo 1) then{
        CHBN_adjustBrightness = 0;
        CHBN_adjustColor = [0,0,0];
    }else{
        CHBN_adjustBrightness = 0.5;
        CHBN_adjustColor = [0.5,0.7,1];
    };
};

["brilloEnNoche", "onEachFrame", {call x_fnc_esDeNoche}] call BIS_fnc_addStackedEventHandler;

round(sunOrMoon);