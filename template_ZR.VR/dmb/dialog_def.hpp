///////////////////////////
// DIALOG DEFINITION
//////////////////////////

class dungeonMasterBoard
{
	idd = -1;
	movingEnable = true;
	
	class ControlsBackground
	{
		class ctrl_dmb_bg
		{
			type = 0;
			idc = -1;
			x = safeZoneX + safeZoneW * 0.24375;
			y = safeZoneY + safeZoneH * 0.225;
			w = safeZoneW * 0.5125;
			h = safeZoneH * 0.55;
			style = 48+2048;
			text = "dmb\resources\img\bg.jpg";
			colorBackground[] = {0,0,0,0.7778};
			colorText[] = {1,1,1,1};
			font = "PuristaMedium";
			sizeEx = (((((safezoneW / safezoneH) min 1.2) / 1.2) / 25) * 1);
			
		};
		class ctrl_dmb_limiter_1
		{
			type = 0;
			idc = -1;
			x = safeZoneX + safeZoneW * 0.61875;
			y = safeZoneY + safeZoneH * 0.225;
			w = safeZoneW * 0.0125;
			h = safeZoneH * 0.55;
			style = 0;
			text = "";
			colorBackground[] = {0.102,0.102,0.102,0.7222};
			colorText[] = {1,1,1,1};
			font = "PuristaMedium";
			sizeEx = (((((safezoneW / safezoneH) min 1.2) / 1.2) / 25) * 1);
			
		};
		class ctrl_dmb_limiter_1_copy1
		{
			type = 0;
			idc = -1;
			x = safeZoneX + safeZoneW * 0.36875;
			y = safeZoneY + safeZoneH * 0.225;
			w = safeZoneW * 0.0125;
			h = safeZoneH * 0.55;
			style = 0;
			text = "";
			colorBackground[] = {0.102,0.102,0.102,0.7222};
			colorText[] = {1,1,1,1};
			font = "PuristaMedium";
			sizeEx = (((((safezoneW / safezoneH) min 1.2) / 1.2) / 25) * 1);
			
		};
		
	};
	class Controls
	{
		class ctr_text_main
		{
			type = 0;
			idc = 10181;
			x = safeZoneX + safeZoneW * 0.45416667;
			y = safeZoneY + safeZoneH * 0.25;
			w = safeZoneW * 0.0875;
			h = safeZoneH * 0.025;
			style = 2;
			text = "MAIN";
			colorBackground[] = {0.3686,0.2549,0.0863,0};
			colorText[] = {1,1,1,1};
			font = "PuristaMedium";
			sizeEx = (((((safezoneW / safezoneH) min 1.2) / 1.2) / 25) * 1);
			
		};
		class ctrl_text_aux_l
		{
			type = 0;
			idc = 10182;
			x = safeZoneX + safeZoneW * 0.26875;
			y = safeZoneY + safeZoneH * 0.25;
			w = safeZoneW * 0.0875;
			h = safeZoneH * 0.025;
			style = 2;
			text = "AUX LEFT";
			colorBackground[] = {0.3686,0.2549,0.0863,0};
			colorText[] = {1,1,1,1};
			font = "PuristaMedium";
			sizeEx = (((((safezoneW / safezoneH) min 1.2) / 1.2) / 25) * 1);
			
		};
		class ctrl_txt_aux_r
		{
			type = 0;
			idc = 10183;
			x = safeZoneX + safeZoneW * 0.64375;
			y = safeZoneY + safeZoneH * 0.25;
			w = safeZoneW * 0.0875;
			h = safeZoneH * 0.025;
			style = 2;
			text = "AUX RIGHT";
			colorBackground[] = {0.3686,0.2549,0.0863,0};
			colorText[] = {1,1,1,1};
			font = "PuristaMedium";
			sizeEx = (((((safezoneW / safezoneH) min 1.2) / 1.2) / 25) * 1);
			
		};
		
		class ctrl_bt_1
		{
			type = 1;
			idc = 101811;
			x = 0.26742425;
			y = 0.18636365;
			w = 0.0909091;
			h = 0.0909091;
			style = 0+2;
			text = "1";
			borderSize = 0;
			colorBackground[] = {0.302,0.302,0.302,0.5714};
			colorBackgroundActive[] = {1,1,1,1};
			colorBackgroundDisabled[] = {0.2,0.2,0.2,1};
			colorBorder[] = {0,0,0,0};
			colorDisabled[] = {0.2,0.2,0.2,1};
			colorFocused[] = {0.2,0.2,0.2,1};
			colorShadow[] = {0,0,0,0};
			colorText[] = {0.3569,0.6627,0.4275,1};
			font = "PuristaMedium";
			offsetPressedX = 0.01;
			offsetPressedY = 0.01;
			offsetX = 0.01;
			offsetY = 0.01;
			sizeEx = (((((safezoneW / safezoneH) min 1.2) / 1.2) / 25) * 1);
			soundClick[] = {"\A3\ui_f\data\sound\RscButton\soundClick",0.09,1.0};
			soundEnter[] = {"\A3\ui_f\data\sound\RscButton\soundEnter",0.09,1.0};
			soundEscape[] = {"\A3\ui_f\data\sound\RscButton\soundEscape",0.09,1.0};
			soundPush[] = {"\A3\ui_f\data\sound\RscButton\soundPush",0.09,1.0};
            onMouseButtonDown = "call DMB_CODE_1";

		};
		class ctrl_bt_2
		{
			type = 1;
			idc = 101812;
			x = 0.44823234;
			y = 0.1868687;
			w = 0.0909091;
			h = 0.0909091;
			style = 0+2;
			text = "2";
			borderSize = 0;
			colorBackground[] = {0.302,0.302,0.302,0.5714};
			colorBackgroundActive[] = {1,1,1,1};
			colorBackgroundDisabled[] = {0.2,0.2,0.2,1};
			colorBorder[] = {0,0,0,0};
			colorDisabled[] = {0.2,0.2,0.2,1};
			colorFocused[] = {0.2,0.2,0.2,1};
			colorShadow[] = {0,0,0,0};
			colorText[] = {0.3569,0.6627,0.4275,1};
			font = "PuristaMedium";
			offsetPressedX = 0.01;
			offsetPressedY = 0.01;
			offsetX = 0.01;
			offsetY = 0.01;
			sizeEx = (((((safezoneW / safezoneH) min 1.2) / 1.2) / 25) * 1);
			soundClick[] = {"\A3\ui_f\data\sound\RscButton\soundClick",0.09,1.0};
			soundEnter[] = {"\A3\ui_f\data\sound\RscButton\soundEnter",0.09,1.0};
			soundEscape[] = {"\A3\ui_f\data\sound\RscButton\soundEscape",0.09,1.0};
			soundPush[] = {"\A3\ui_f\data\sound\RscButton\soundPush",0.09,1.0};
            onMouseButtonDown = "call DMB_CODE_2";
			
		};
		class ctrl_bt_3
		{
			type = 1;
			idc = 101813;
			x = 0.63005053;
			y = 0.18636364;
			w = 0.0909091;
			h = 0.0909091;
			style = 0+2;
			text = "3";
			borderSize = 0;
			colorBackground[] = {0.302,0.302,0.302,0.5714};
			colorBackgroundActive[] = {1,1,1,1};
			colorBackgroundDisabled[] = {0.2,0.2,0.2,1};
			colorBorder[] = {0,0,0,0};
			colorDisabled[] = {0.2,0.2,0.2,1};
			colorFocused[] = {0.2,0.2,0.2,1};
			colorShadow[] = {0,0,0,0};
			colorText[] = {0.3569,0.6627,0.4275,1};
			font = "PuristaMedium";
			offsetPressedX = 0.01;
			offsetPressedY = 0.01;
			offsetX = 0.01;
			offsetY = 0.01;
			sizeEx = (((((safezoneW / safezoneH) min 1.2) / 1.2) / 25) * 1);
			soundClick[] = {"\A3\ui_f\data\sound\RscButton\soundClick",0.09,1.0};
			soundEnter[] = {"\A3\ui_f\data\sound\RscButton\soundEnter",0.09,1.0};
			soundEscape[] = {"\A3\ui_f\data\sound\RscButton\soundEscape",0.09,1.0};
			soundPush[] = {"\A3\ui_f\data\sound\RscButton\soundPush",0.09,1.0};
            onMouseButtonDown = "call DMB_CODE_3";
			
		};
		class ctrl_bt_4
		{
			type = 1;
			idc = 101814;
			x = 0.26742425;
			y = 0.33636366;
			w = 0.0909091;
			h = 0.0909091;
			style = 0+2;
			text = "4";
			borderSize = 0;
			colorBackground[] = {0.302,0.302,0.302,0.5714};
			colorBackgroundActive[] = {1,1,1,1};
			colorBackgroundDisabled[] = {0.2,0.2,0.2,1};
			colorBorder[] = {0,0,0,0};
			colorDisabled[] = {0.2,0.2,0.2,1};
			colorFocused[] = {0.2,0.2,0.2,1};
			colorShadow[] = {0,0,0,0};
			colorText[] = {0.3569,0.6627,0.4275,1};
			font = "PuristaMedium";
			offsetPressedX = 0.01;
			offsetPressedY = 0.01;
			offsetX = 0.01;
			offsetY = 0.01;
			sizeEx = (((((safezoneW / safezoneH) min 1.2) / 1.2) / 25) * 1);
			soundClick[] = {"\A3\ui_f\data\sound\RscButton\soundClick",0.09,1.0};
			soundEnter[] = {"\A3\ui_f\data\sound\RscButton\soundEnter",0.09,1.0};
			soundEscape[] = {"\A3\ui_f\data\sound\RscButton\soundEscape",0.09,1.0};
			soundPush[] = {"\A3\ui_f\data\sound\RscButton\soundPush",0.09,1.0};
            onMouseButtonDown = "call DMB_CODE_4";
			
		};
		class ctrl_bt_5
		{
			type = 1;
			idc = 101815;
			x = 0.4469697;
			y = 0.33670035;
			w = 0.0909091;
			h = 0.0909091;
			style = 0+2;
			text = "5";
			borderSize = 0;
			colorBackground[] = {0.302,0.302,0.302,0.5714};
			colorBackgroundActive[] = {1,1,1,1};
			colorBackgroundDisabled[] = {0.2,0.2,0.2,1};
			colorBorder[] = {0,0,0,0};
			colorDisabled[] = {0.2,0.2,0.2,1};
			colorFocused[] = {0.2,0.2,0.2,1};
			colorShadow[] = {0,0,0,0};
			colorText[] = {0.3569,0.6627,0.4275,1};
			font = "PuristaMedium";
			offsetPressedX = 0.01;
			offsetPressedY = 0.01;
			offsetX = 0.01;
			offsetY = 0.01;
			sizeEx = (((((safezoneW / safezoneH) min 1.2) / 1.2) / 25) * 1);
			soundClick[] = {"\A3\ui_f\data\sound\RscButton\soundClick",0.09,1.0};
			soundEnter[] = {"\A3\ui_f\data\sound\RscButton\soundEnter",0.09,1.0};
			soundEscape[] = {"\A3\ui_f\data\sound\RscButton\soundEscape",0.09,1.0};
			soundPush[] = {"\A3\ui_f\data\sound\RscButton\soundPush",0.09,1.0};
            onMouseButtonDown = "call DMB_CODE_5";
			
		};
		class ctrl_bt_6
		{
			type = 1;
			idc = 101816;
			x = 0.63005053;
			y = 0.33644782;
			w = 0.0909091;
			h = 0.0909091;
			style = 0+2;
			text = "6";
			borderSize = 0;
			colorBackground[] = {0.302,0.302,0.302,0.5714};
			colorBackgroundActive[] = {1,1,1,1};
			colorBackgroundDisabled[] = {0.2,0.2,0.2,1};
			colorBorder[] = {0,0,0,0};
			colorDisabled[] = {0.2,0.2,0.2,1};
			colorFocused[] = {0.2,0.2,0.2,1};
			colorShadow[] = {0,0,0,0};
			colorText[] = {0.3569,0.6627,0.4275,1};
			font = "PuristaMedium";
			offsetPressedX = 0.01;
			offsetPressedY = 0.01;
			offsetX = 0.01;
			offsetY = 0.01;
			sizeEx = (((((safezoneW / safezoneH) min 1.2) / 1.2) / 25) * 1);
			soundClick[] = {"\A3\ui_f\data\sound\RscButton\soundClick",0.09,1.0};
			soundEnter[] = {"\A3\ui_f\data\sound\RscButton\soundEnter",0.09,1.0};
			soundEscape[] = {"\A3\ui_f\data\sound\RscButton\soundEscape",0.09,1.0};
			soundPush[] = {"\A3\ui_f\data\sound\RscButton\soundPush",0.09,1.0};
            onMouseButtonDown = "call DMB_CODE_6";
			
		};
		class ctrl_bt_7
		{
			type = 1;
			idc = 101817;
			x = 0.26742425;
			y = 0.4863637;
			w = 0.0909091;
			h = 0.0909091;
			style = 0+2;
			text = "7";
			borderSize = 0;
			colorBackground[] = {0.302,0.302,0.302,0.5714};
			colorBackgroundActive[] = {1,1,1,1};
			colorBackgroundDisabled[] = {0.2,0.2,0.2,1};
			colorBorder[] = {0,0,0,0};
			colorDisabled[] = {0.2,0.2,0.2,1};
			colorFocused[] = {0.2,0.2,0.2,1};
			colorShadow[] = {0,0,0,0};
			colorText[] = {0.3569,0.6627,0.4275,1};
			font = "PuristaMedium";
			offsetPressedX = 0.01;
			offsetPressedY = 0.01;
			offsetX = 0.01;
			offsetY = 0.01;
			sizeEx = (((((safezoneW / safezoneH) min 1.2) / 1.2) / 25) * 1);
			soundClick[] = {"\A3\ui_f\data\sound\RscButton\soundClick",0.09,1.0};
			soundEnter[] = {"\A3\ui_f\data\sound\RscButton\soundEnter",0.09,1.0};
			soundEscape[] = {"\A3\ui_f\data\sound\RscButton\soundEscape",0.09,1.0};
			soundPush[] = {"\A3\ui_f\data\sound\RscButton\soundPush",0.09,1.0};
            onMouseButtonDown = "call DMB_CODE_7";
			
		};
		class ctrl_bt_8
		{
			type = 1;
			idc = 101818;
			x = 0.4469697;
			y = 0.486532;
			w = 0.0909091;
			h = 0.0909091;
			style = 0+2;
			text = "8";
			borderSize = 0;
			colorBackground[] = {0.302,0.302,0.302,0.5714};
			colorBackgroundActive[] = {1,1,1,1};
			colorBackgroundDisabled[] = {0.2,0.2,0.2,1};
			colorBorder[] = {0,0,0,0};
			colorDisabled[] = {0.2,0.2,0.2,1};
			colorFocused[] = {0.2,0.2,0.2,1};
			colorShadow[] = {0,0,0,0};
			colorText[] = {0.3569,0.6627,0.4275,1};
			font = "PuristaMedium";
			offsetPressedX = 0.01;
			offsetPressedY = 0.01;
			offsetX = 0.01;
			offsetY = 0.01;
			sizeEx = (((((safezoneW / safezoneH) min 1.2) / 1.2) / 25) * 1);
			soundClick[] = {"\A3\ui_f\data\sound\RscButton\soundClick",0.09,1.0};
			soundEnter[] = {"\A3\ui_f\data\sound\RscButton\soundEnter",0.09,1.0};
			soundEscape[] = {"\A3\ui_f\data\sound\RscButton\soundEscape",0.09,1.0};
			soundPush[] = {"\A3\ui_f\data\sound\RscButton\soundPush",0.09,1.0};
            onMouseButtonDown = "call DMB_CODE_8";
			
		};
		class ctrl_bt_9
		{
			type = 1;
			idc = 101819;
			x = 0.63131314;
			y = 0.486532;
			w = 0.0909091;
			h = 0.0909091;
			style = 0+2;
			text = "9";
			borderSize = 0;
			colorBackground[] = {0.302,0.302,0.302,0.5714};
			colorBackgroundActive[] = {1,1,1,1};
			colorBackgroundDisabled[] = {0.2,0.2,0.2,1};
			colorBorder[] = {0,0,0,0};
			colorDisabled[] = {0.2,0.2,0.2,1};
			colorFocused[] = {0.2,0.2,0.2,1};
			colorShadow[] = {0,0,0,0};
			colorText[] = {0.3569,0.6627,0.4275,1};
			font = "PuristaMedium";
			offsetPressedX = 0.01;
			offsetPressedY = 0.01;
			offsetX = 0.01;
			offsetY = 0.01;
			sizeEx = (((((safezoneW / safezoneH) min 1.2) / 1.2) / 25) * 1);
			soundClick[] = {"\A3\ui_f\data\sound\RscButton\soundClick",0.09,1.0};
			soundEnter[] = {"\A3\ui_f\data\sound\RscButton\soundEnter",0.09,1.0};
			soundEscape[] = {"\A3\ui_f\data\sound\RscButton\soundEscape",0.09,1.0};
			soundPush[] = {"\A3\ui_f\data\sound\RscButton\soundPush",0.09,1.0};
            onMouseButtonDown = "call DMB_CODE_9";
			
		};
		class ctrl_bt_10
		{
			type = 1;
			idc = 101820;
			x = 0.26742425;
			y = 0.63636371;
			w = 0.0909091;
			h = 0.0909091;
			style = 0+2;
			text = "10";
			borderSize = 0;
			colorBackground[] = {0.302,0.302,0.302,0.5714};
			colorBackgroundActive[] = {1,1,1,1};
			colorBackgroundDisabled[] = {0.2,0.2,0.2,1};
			colorBorder[] = {0,0,0,0};
			colorDisabled[] = {0.2,0.2,0.2,1};
			colorFocused[] = {0.2,0.2,0.2,1};
			colorShadow[] = {0,0,0,0};
			colorText[] = {0.3569,0.6627,0.4275,1};
			font = "PuristaMedium";
			offsetPressedX = 0.01;
			offsetPressedY = 0.01;
			offsetX = 0.01;
			offsetY = 0.01;
			sizeEx = (((((safezoneW / safezoneH) min 1.2) / 1.2) / 25) * 1);
			soundClick[] = {"\A3\ui_f\data\sound\RscButton\soundClick",0.09,1.0};
			soundEnter[] = {"\A3\ui_f\data\sound\RscButton\soundEnter",0.09,1.0};
			soundEscape[] = {"\A3\ui_f\data\sound\RscButton\soundEscape",0.09,1.0};
			soundPush[] = {"\A3\ui_f\data\sound\RscButton\soundPush",0.09,1.0};
            onMouseButtonDown = "call DMB_CODE_10";
			
		};
		class ctrl_bt_11
		{
			type = 1;
			idc = 101821;
			x = 0.4469697;
			y = 0.63636364;
			w = 0.0909091;
			h = 0.0909091;
			style = 0+2;
			text = "11";
			borderSize = 0;
			colorBackground[] = {0.302,0.302,0.302,0.5714};
			colorBackgroundActive[] = {1,1,1,1};
			colorBackgroundDisabled[] = {0.2,0.2,0.2,1};
			colorBorder[] = {0,0,0,0};
			colorDisabled[] = {0.2,0.2,0.2,1};
			colorFocused[] = {0.2,0.2,0.2,1};
			colorShadow[] = {0,0,0,0};
			colorText[] = {0.3569,0.6627,0.4275,1};
			font = "PuristaMedium";
			offsetPressedX = 0.01;
			offsetPressedY = 0.01;
			offsetX = 0.01;
			offsetY = 0.01;
			sizeEx = (((((safezoneW / safezoneH) min 1.2) / 1.2) / 25) * 1);
			soundClick[] = {"\A3\ui_f\data\sound\RscButton\soundClick",0.09,1.0};
			soundEnter[] = {"\A3\ui_f\data\sound\RscButton\soundEnter",0.09,1.0};
			soundEscape[] = {"\A3\ui_f\data\sound\RscButton\soundEscape",0.09,1.0};
			soundPush[] = {"\A3\ui_f\data\sound\RscButton\soundPush",0.09,1.0};
            onMouseButtonDown = "call DMB_CODE_11";
			
		};
		class ctrl_bt_12
		{
			type = 1;
			idc = 101822;
			x = 0.63131314;
			y = 0.63653202;
			w = 0.0909091;
			h = 0.0909091;
			style = 0+2;
			text = "12";
			borderSize = 0;
			colorBackground[] = {0.302,0.302,0.302,0.5714};
			colorBackgroundActive[] = {1,1,1,1};
			colorBackgroundDisabled[] = {0.2,0.2,0.2,1};
			colorBorder[] = {0,0,0,0};
			colorDisabled[] = {0.2,0.2,0.2,1};
			colorFocused[] = {0.2,0.2,0.2,1};
			colorShadow[] = {0,0,0,0};
			colorText[] = {0.3569,0.6627,0.4275,1};
			font = "PuristaMedium";
			offsetPressedX = 0.01;
			offsetPressedY = 0.01;
			offsetX = 0.01;
			offsetY = 0.01;
			sizeEx = (((((safezoneW / safezoneH) min 1.2) / 1.2) / 25) * 1);
			soundClick[] = {"\A3\ui_f\data\sound\RscButton\soundClick",0.09,1.0};
			soundEnter[] = {"\A3\ui_f\data\sound\RscButton\soundEnter",0.09,1.0};
			soundEscape[] = {"\A3\ui_f\data\sound\RscButton\soundEscape",0.09,1.0};
			soundPush[] = {"\A3\ui_f\data\sound\RscButton\soundPush",0.09,1.0};
            onMouseButtonDown = "call DMB_CODE_12";
			
		};
		class ctrl_bt_13
		{
			type = 1;
			idc = 101823;
			x = 0.26742425;
			y = 0.78636374;
			w = 0.0909091;
			h = 0.0909091;
			style = 0+2;
			text = "13";
			borderSize = 0;
			colorBackground[] = {0.302,0.302,0.302,0.5714};
			colorBackgroundActive[] = {1,1,1,1};
			colorBackgroundDisabled[] = {0.2,0.2,0.2,1};
			colorBorder[] = {0,0,0,0};
			colorDisabled[] = {0.2,0.2,0.2,1};
			colorFocused[] = {0.2,0.2,0.2,1};
			colorShadow[] = {0,0,0,0};
			colorText[] = {0.3569,0.6627,0.4275,1};
			font = "PuristaMedium";
			offsetPressedX = 0.01;
			offsetPressedY = 0.01;
			offsetX = 0.01;
			offsetY = 0.01;
			sizeEx = (((((safezoneW / safezoneH) min 1.2) / 1.2) / 25) * 1);
			soundClick[] = {"\A3\ui_f\data\sound\RscButton\soundClick",0.09,1.0};
			soundEnter[] = {"\A3\ui_f\data\sound\RscButton\soundEnter",0.09,1.0};
			soundEscape[] = {"\A3\ui_f\data\sound\RscButton\soundEscape",0.09,1.0};
			soundPush[] = {"\A3\ui_f\data\sound\RscButton\soundPush",0.09,1.0};
            onMouseButtonDown = "call DMB_CODE_13";
			
		};
		class ctrl_bt_14
		{
			type = 1;
			idc = 101824;
			x = 0.4469697;
			y = 0.7861953;
			w = 0.0909091;
			h = 0.0909091;
			style = 0+2;
			text = "14";
			borderSize = 0;
			colorBackground[] = {0.302,0.302,0.302,0.5714};
			colorBackgroundActive[] = {1,1,1,1};
			colorBackgroundDisabled[] = {0.2,0.2,0.2,1};
			colorBorder[] = {0,0,0,0};
			colorDisabled[] = {0.2,0.2,0.2,1};
			colorFocused[] = {0.2,0.2,0.2,1};
			colorShadow[] = {0,0,0,0};
			colorText[] = {0.3569,0.6627,0.4275,1};
			font = "PuristaMedium";
			offsetPressedX = 0.01;
			offsetPressedY = 0.01;
			offsetX = 0.01;
			offsetY = 0.01;
			sizeEx = (((((safezoneW / safezoneH) min 1.2) / 1.2) / 25) * 1);
			soundClick[] = {"\A3\ui_f\data\sound\RscButton\soundClick",0.09,1.0};
			soundEnter[] = {"\A3\ui_f\data\sound\RscButton\soundEnter",0.09,1.0};
			soundEscape[] = {"\A3\ui_f\data\sound\RscButton\soundEscape",0.09,1.0};
			soundPush[] = {"\A3\ui_f\data\sound\RscButton\soundPush",0.09,1.0};
            onMouseButtonDown = "call DMB_CODE_14";
			
		};
		class ctrl_bt_15
		{
			type = 1;
			idc = 101825;
			x = 0.63131314;
			y = 0.78653204;
			w = 0.0909091;
			h = 0.0909091;
			style = 0+2;
			text = "15";
			borderSize = 0;
			colorBackground[] = {0.302,0.302,0.302,0.5714};
			colorBackgroundActive[] = {1,1,1,1};
			colorBackgroundDisabled[] = {0.2,0.2,0.2,1};
			colorBorder[] = {0,0,0,0};
			colorDisabled[] = {0.2,0.2,0.2,1};
			colorFocused[] = {0.2,0.2,0.2,1};
			colorShadow[] = {0,0,0,0};
			colorText[] = {0.3569,0.6627,0.4275,1};
			font = "PuristaMedium";
			offsetPressedX = 0.01;
			offsetPressedY = 0.01;
			offsetX = 0.01;
			offsetY = 0.01;
			sizeEx = (((((safezoneW / safezoneH) min 1.2) / 1.2) / 25) * 1);
			soundClick[] = {"\A3\ui_f\data\sound\RscButton\soundClick",0.09,1.0};
			soundEnter[] = {"\A3\ui_f\data\sound\RscButton\soundEnter",0.09,1.0};
			soundEscape[] = {"\A3\ui_f\data\sound\RscButton\soundEscape",0.09,1.0};
			soundPush[] = {"\A3\ui_f\data\sound\RscButton\soundPush",0.09,1.0};
			onMouseButtonDown = "call DMB_CODE_15";

		};
		class ctrl_aux_1
		{
			type = 1;
			idc = 101830;
			x = -0.06868674;
			y = 0.18653208;
			w = 0.19090913;
			h = 0.0909091;
			style = 0+2;
			text = "AUX 1";
			borderSize = 0;
			colorBackground[] = {0.302,0.302,0.302,0.5714};
			colorBackgroundActive[] = {1,1,1,1};
			colorBackgroundDisabled[] = {0.2,0.2,0.2,1};
			colorBorder[] = {0,0,0,0};
			colorDisabled[] = {0.2,0.2,0.2,1};
			colorFocused[] = {0.2,0.2,0.2,1};
			colorShadow[] = {0,0,0,0};
			colorText[] = {0.3569,0.6627,0.4275,1};
			font = "PuristaMedium";
			offsetPressedX = 0.01;
			offsetPressedY = 0.01;
			offsetX = 0.01;
			offsetY = 0.01;
			sizeEx = (((((safezoneW / safezoneH) min 1.2) / 1.2) / 25) * 1);
			soundClick[] = {"\A3\ui_f\data\sound\RscButton\soundClick",0.09,1.0};
			soundEnter[] = {"\A3\ui_f\data\sound\RscButton\soundEnter",0.09,1.0};
			soundEscape[] = {"\A3\ui_f\data\sound\RscButton\soundEscape",0.09,1.0};
			soundPush[] = {"\A3\ui_f\data\sound\RscButton\soundPush",0.09,1.0};
            onMouseButtonDown = "call DMB_CODE_AL1";
			
		};
		class ctrl_aux_2
		{
			type = 1;
			idc = 101831;
			x = -0.06868674;
			y = 0.33653211;
			w = 0.19090913;
			h = 0.0909091;
			style = 0+2;
			text = "AUX 2";
			borderSize = 0;
			colorBackground[] = {0.302,0.302,0.302,0.5714};
			colorBackgroundActive[] = {1,1,1,1};
			colorBackgroundDisabled[] = {0.2,0.2,0.2,1};
			colorBorder[] = {0,0,0,0};
			colorDisabled[] = {0.2,0.2,0.2,1};
			colorFocused[] = {0.2,0.2,0.2,1};
			colorShadow[] = {0,0,0,0};
			colorText[] = {0.3569,0.6627,0.4275,1};
			font = "PuristaMedium";
			offsetPressedX = 0.01;
			offsetPressedY = 0.01;
			offsetX = 0.01;
			offsetY = 0.01;
			sizeEx = (((((safezoneW / safezoneH) min 1.2) / 1.2) / 25) * 1);
			soundClick[] = {"\A3\ui_f\data\sound\RscButton\soundClick",0.09,1.0};
			soundEnter[] = {"\A3\ui_f\data\sound\RscButton\soundEnter",0.09,1.0};
			soundEscape[] = {"\A3\ui_f\data\sound\RscButton\soundEscape",0.09,1.0};
			soundPush[] = {"\A3\ui_f\data\sound\RscButton\soundPush",0.09,1.0};
            onMouseButtonDown = "call DMB_CODE_AL2";
			
		};
		class ctrl_aux_3
		{
			type = 1;
			idc = 101833;
			x = -0.06868674;
			y = 0.48653213;
			w = 0.19090913;
			h = 0.0909091;
			style = 0+2;
			text = "AUX 3";
			borderSize = 0;
			colorBackground[] = {0.302,0.302,0.302,0.5714};
			colorBackgroundActive[] = {1,1,1,1};
			colorBackgroundDisabled[] = {0.2,0.2,0.2,1};
			colorBorder[] = {0,0,0,0};
			colorDisabled[] = {0.2,0.2,0.2,1};
			colorFocused[] = {0.2,0.2,0.2,1};
			colorShadow[] = {0,0,0,0};
			colorText[] = {0.3569,0.6627,0.4275,1};
			font = "PuristaMedium";
			offsetPressedX = 0.01;
			offsetPressedY = 0.01;
			offsetX = 0.01;
			offsetY = 0.01;
			sizeEx = (((((safezoneW / safezoneH) min 1.2) / 1.2) / 25) * 1);
			soundClick[] = {"\A3\ui_f\data\sound\RscButton\soundClick",0.09,1.0};
			soundEnter[] = {"\A3\ui_f\data\sound\RscButton\soundEnter",0.09,1.0};
			soundEscape[] = {"\A3\ui_f\data\sound\RscButton\soundEscape",0.09,1.0};
			soundPush[] = {"\A3\ui_f\data\sound\RscButton\soundPush",0.09,1.0};
            onMouseButtonDown = "call DMB_CODE_AL3";
			
		};
		class ctrl_aux_4
		{
			type = 1;
			idc = 101834;
			x = -0.06868674;
			y = 0.63653216;
			w = 0.19090913;
			h = 0.0909091;
			style = 0+2;
			text = "AUX 4";
			borderSize = 0;
			colorBackground[] = {0.302,0.302,0.302,0.5714};
			colorBackgroundActive[] = {1,1,1,1};
			colorBackgroundDisabled[] = {0.2,0.2,0.2,1};
			colorBorder[] = {0,0,0,0};
			colorDisabled[] = {0.2,0.2,0.2,1};
			colorFocused[] = {0.2,0.2,0.2,1};
			colorShadow[] = {0,0,0,0};
			colorText[] = {0.3569,0.6627,0.4275,1};
			font = "PuristaMedium";
			offsetPressedX = 0.01;
			offsetPressedY = 0.01;
			offsetX = 0.01;
			offsetY = 0.01;
			sizeEx = (((((safezoneW / safezoneH) min 1.2) / 1.2) / 25) * 1);
			soundClick[] = {"\A3\ui_f\data\sound\RscButton\soundClick",0.09,1.0};
			soundEnter[] = {"\A3\ui_f\data\sound\RscButton\soundEnter",0.09,1.0};
			soundEscape[] = {"\A3\ui_f\data\sound\RscButton\soundEscape",0.09,1.0};
			soundPush[] = {"\A3\ui_f\data\sound\RscButton\soundPush",0.09,1.0};
            onMouseButtonDown = "call DMB_CODE_AL4";
			
		};
		class ctrl_aux_5
		{
			type = 1;
			idc = 101835;
			x = -0.06868674;
			y = 0.78653219;
			w = 0.19090913;
			h = 0.0909091;
			style = 0+2;
			text = "AUX 5";
			borderSize = 0;
			colorBackground[] = {0.302,0.302,0.302,0.5714};
			colorBackgroundActive[] = {1,1,1,1};
			colorBackgroundDisabled[] = {0.2,0.2,0.2,1};
			colorBorder[] = {0,0,0,0};
			colorDisabled[] = {0.2,0.2,0.2,1};
			colorFocused[] = {0.2,0.2,0.2,1};
			colorShadow[] = {0,0,0,0};
			colorText[] = {0.3569,0.6627,0.4275,1};
			font = "PuristaMedium";
			offsetPressedX = 0.01;
			offsetPressedY = 0.01;
			offsetX = 0.01;
			offsetY = 0.01;
			sizeEx = (((((safezoneW / safezoneH) min 1.2) / 1.2) / 25) * 1);
			soundClick[] = {"\A3\ui_f\data\sound\RscButton\soundClick",0.09,1.0};
			soundEnter[] = {"\A3\ui_f\data\sound\RscButton\soundEnter",0.09,1.0};
			soundEscape[] = {"\A3\ui_f\data\sound\RscButton\soundEscape",0.09,1.0};
			soundPush[] = {"\A3\ui_f\data\sound\RscButton\soundPush",0.09,1.0};
            onMouseButtonDown = "call DMB_CODE_AL5";
			
		};
		class ctrl_aux_b1
		{
			type = 1;
			idc = 101841;
			x = 0.85631335;
			y = 0.18653208;
			w = 0.19090913;
			h = 0.0909091;
			style = 0+2;
			text = "AUX B1";
			borderSize = 0;
			colorBackground[] = {0.302,0.302,0.302,0.5714};
			colorBackgroundActive[] = {1,1,1,1};
			colorBackgroundDisabled[] = {0.2,0.2,0.2,1};
			colorBorder[] = {0,0,0,0};
			colorDisabled[] = {0.2,0.2,0.2,1};
			colorFocused[] = {0.2,0.2,0.2,1};
			colorShadow[] = {0,0,0,0};
			colorText[] = {0.3569,0.6627,0.4275,1};
			font = "PuristaMedium";
			offsetPressedX = 0.01;
			offsetPressedY = 0.01;
			offsetX = 0.01;
			offsetY = 0.01;
			sizeEx = (((((safezoneW / safezoneH) min 1.2) / 1.2) / 25) * 1);
			soundClick[] = {"\A3\ui_f\data\sound\RscButton\soundClick",0.09,1.0};
			soundEnter[] = {"\A3\ui_f\data\sound\RscButton\soundEnter",0.09,1.0};
			soundEscape[] = {"\A3\ui_f\data\sound\RscButton\soundEscape",0.09,1.0};
			soundPush[] = {"\A3\ui_f\data\sound\RscButton\soundPush",0.09,1.0};
            onMouseButtonDown = "call DMB_CODE_AR1";
			
		};
		class ctrl_aux_b2
		{
			type = 1;
			idc = 101842;
			x = 0.85631335;
			y = 0.33653209;
			w = 0.19090913;
			h = 0.0909091;
			style = 0+2;
			text = "AUX B2";
			borderSize = 0;
			colorBackground[] = {0.302,0.302,0.302,0.5714};
			colorBackgroundActive[] = {1,1,1,1};
			colorBackgroundDisabled[] = {0.2,0.2,0.2,1};
			colorBorder[] = {0,0,0,0};
			colorDisabled[] = {0.2,0.2,0.2,1};
			colorFocused[] = {0.2,0.2,0.2,1};
			colorShadow[] = {0,0,0,0};
			colorText[] = {0.3569,0.6627,0.4275,1};
			font = "PuristaMedium";
			offsetPressedX = 0.01;
			offsetPressedY = 0.01;
			offsetX = 0.01;
			offsetY = 0.01;
			sizeEx = (((((safezoneW / safezoneH) min 1.2) / 1.2) / 25) * 1);
			soundClick[] = {"\A3\ui_f\data\sound\RscButton\soundClick",0.09,1.0};
			soundEnter[] = {"\A3\ui_f\data\sound\RscButton\soundEnter",0.09,1.0};
			soundEscape[] = {"\A3\ui_f\data\sound\RscButton\soundEscape",0.09,1.0};
			soundPush[] = {"\A3\ui_f\data\sound\RscButton\soundPush",0.09,1.0};
            onMouseButtonDown = "call DMB_CODE_AR2";
			
		};
		class ctrl_aux_b3
		{
			type = 1;
			idc = 101843;
			x = 0.85631335;
			y = 0.48653213;
			w = 0.19090913;
			h = 0.0909091;
			style = 0+2;
			text = "AUX B3";
			borderSize = 0;
			colorBackground[] = {0.302,0.302,0.302,0.5714};
			colorBackgroundActive[] = {1,1,1,1};
			colorBackgroundDisabled[] = {0.2,0.2,0.2,1};
			colorBorder[] = {0,0,0,0};
			colorDisabled[] = {0.2,0.2,0.2,1};
			colorFocused[] = {0.2,0.2,0.2,1};
			colorShadow[] = {0,0,0,0};
			colorText[] = {0.3569,0.6627,0.4275,1};
			font = "PuristaMedium";
			offsetPressedX = 0.01;
			offsetPressedY = 0.01;
			offsetX = 0.01;
			offsetY = 0.01;
			sizeEx = (((((safezoneW / safezoneH) min 1.2) / 1.2) / 25) * 1);
			soundClick[] = {"\A3\ui_f\data\sound\RscButton\soundClick",0.09,1.0};
			soundEnter[] = {"\A3\ui_f\data\sound\RscButton\soundEnter",0.09,1.0};
			soundEscape[] = {"\A3\ui_f\data\sound\RscButton\soundEscape",0.09,1.0};
			soundPush[] = {"\A3\ui_f\data\sound\RscButton\soundPush",0.09,1.0};
            onMouseButtonDown = "call DMB_CODE_AR3";
			
		};
		class ctrl_aux_b4
		{
			type = 1;
			idc = 101844;
			x = 0.85631335;
			y = 0.63653214;
			w = 0.19090913;
			h = 0.0909091;
			style = 0+2;
			text = "AUX B4";
			borderSize = 0;
			colorBackground[] = {0.302,0.302,0.302,0.5714};
			colorBackgroundActive[] = {1,1,1,1};
			colorBackgroundDisabled[] = {0.2,0.2,0.2,1};
			colorBorder[] = {0,0,0,0};
			colorDisabled[] = {0.2,0.2,0.2,1};
			colorFocused[] = {0.2,0.2,0.2,1};
			colorShadow[] = {0,0,0,0};
			colorText[] = {0.3569,0.6627,0.4275,1};
			font = "PuristaMedium";
			offsetPressedX = 0.01;
			offsetPressedY = 0.01;
			offsetX = 0.01;
			offsetY = 0.01;
			sizeEx = (((((safezoneW / safezoneH) min 1.2) / 1.2) / 25) * 1);
			soundClick[] = {"\A3\ui_f\data\sound\RscButton\soundClick",0.09,1.0};
			soundEnter[] = {"\A3\ui_f\data\sound\RscButton\soundEnter",0.09,1.0};
			soundEscape[] = {"\A3\ui_f\data\sound\RscButton\soundEscape",0.09,1.0};
			soundPush[] = {"\A3\ui_f\data\sound\RscButton\soundPush",0.09,1.0};
            onMouseButtonDown = "call DMB_CODE_AR4";
			
		};
		class ctrl_aux_b5
		{
			type = 1;
			idc = 101845;
			x = 0.85631335;
			y = 0.78653216;
			w = 0.19090913;
			h = 0.0909091;
			style = 0+2;
			text = "AUX B5";
			borderSize = 0;
			colorBackground[] = {0.302,0.302,0.302,0.5714};
			colorBackgroundActive[] = {1,1,1,1};
			colorBackgroundDisabled[] = {0.2,0.2,0.2,1};
			colorBorder[] = {0,0,0,0};
			colorDisabled[] = {0.2,0.2,0.2,1};
			colorFocused[] = {0.2,0.2,0.2,1};
			colorShadow[] = {0,0,0,0};
			colorText[] = {0.3569,0.6627,0.4275,1};
			font = "PuristaMedium";
			offsetPressedX = 0.01;
			offsetPressedY = 0.01;
			offsetX = 0.01;
			offsetY = 0.01;
			sizeEx = (((((safezoneW / safezoneH) min 1.2) / 1.2) / 25) * 1);
			soundClick[] = {"\A3\ui_f\data\sound\RscButton\soundClick",0.09,1.0};
			soundEnter[] = {"\A3\ui_f\data\sound\RscButton\soundEnter",0.09,1.0};
			soundEscape[] = {"\A3\ui_f\data\sound\RscButton\soundEscape",0.09,1.0};
			soundPush[] = {"\A3\ui_f\data\sound\RscButton\soundPush",0.09,1.0};
            onMouseButtonDown = "call DMB_CODE_AR5";
			
		};

		class move_handler
		{
			type = 0;
			moving = 1;
			idc = -1;
			x = -0.125;
			y = 0;
			w = 1.25;
			h = 1.00000019;
			style = 0;
			text = "";
			colorBackground[] = {0.9098,0.302,0.0824,0};
			colorText[] = {0.0902,0.698,0.9176,0};
			font = "PuristaMedium";
			sizeEx = (((((safezoneW / safezoneH) min 1.2) / 1.2) / 25) * 1);
			
		};
		
	};
	
};
