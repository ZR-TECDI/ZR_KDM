class rc_pos
{
	idd = -1;
	
	class ControlsBackground
	{
		
	};
	class Controls
	{
		class ct_bg
		{
			type = 0;
			idc = -1;
			x = safeZoneX + safeZoneW * 0.36237189;
			y = safeZoneY + safeZoneH * 0.22395834;
			w = safeZoneW * 0.27525623;
			h = safeZoneH * 0.57552084;
			style = 2;
			text = "";
			colorBackground[] = {0,0,0,1};
			colorText[] = {1,1,1,1};
			font = "PuristaMedium";
			sizeEx = (((((safezoneW / safezoneH) min 1.2) / 1.2) / 25) * 1);
			
		};
		class ct_texto
		{
			type = 0;
			idc = -1;
			x = safeZoneX + safeZoneW * 0.38726208;
			y = safeZoneY + safeZoneH * 0.22395834;
			w = safeZoneW * 0.22547585;
			h = safeZoneH * 0.10546875;
			style = 2;
			text = "Reaparecer en:";
			colorBackground[] = {0,0,0,0};
			colorText[] = {1,1,1,1};
			font = "PuristaMedium";
			sizeEx = (((((safezoneW / safezoneH) min 1.2) / 1.2) / 25) * 1);
			
		};
		class BT_here_pos
		{
			type = 1;
			idc = -1;
			x = safeZoneX + safeZoneW * 0.38726208;
			y = safeZoneY + safeZoneH * 0.37239584;
			w = safeZoneW * 0.22547585;
			h = safeZoneH * 0.08072917;
			style = 0+2;
			text = "Quedarse aquí";
			borderSize = 0;
			colorBackground[] = {0.0902,0.1412,0.0196,1};
			colorBackgroundActive[] = {0,0.2,0,1};
			colorBackgroundDisabled[] = {0.2,0.2,0.2,1};
			colorBorder[] = {0,0,0,0};
			colorDisabled[] = {0.2,0.2,0.2,1};
			colorFocused[] = {0.2,0.2,0.2,1};
			colorShadow[] = {0,0,0,1};
			colorText[] = {0.9098,0.8588,0.9804,1};
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
            onMouseButtonDown = "[0] execVM 'rc_pos\reposicionar.sqf'";
			
		};
		class BT_rp_pos
		{
			type = 1;
			idc = -1;
			x = safeZoneX + safeZoneW * 0.38726208;
			y = safeZoneY + safeZoneH * 0.49609375;
			w = safeZoneW * 0.22547585;
			h = safeZoneH * 0.08072917;
			style = 0+2;
			text = "Posición de reunión";
			borderSize = 0;
			colorBackground[] = {0.0902,0.1412,0.0196,1};
			colorBackgroundActive[] = {0,0.2,0,1};
			colorBackgroundDisabled[] = {0.2,0.2,0.2,1};
			colorBorder[] = {0,0,0,0};
			colorDisabled[] = {0.2,0.2,0.2,1};
			colorFocused[] = {0.2,0.2,0.2,1};
			colorShadow[] = {0,0,0,1};
			colorText[] = {0.9098,0.8588,0.9804,1};
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
            onMouseButtonDown = "[1] execVM 'rc_pos\reposicionar.sqf'";
			
		};
		class BT_leader_pos
		{
			type = 1;
			idc = -1;
			x = safeZoneX + safeZoneW * 0.38726208;
			y = safeZoneY + safeZoneH * 0.61979167;
			w = safeZoneW * 0.22547585;
			h = safeZoneH * 0.08072917;
			style = 0+2;
			text = "Posición de comandante";
			borderSize = 0;
			colorBackground[] = {0.0902,0.1412,0.0196,1};
			colorBackgroundActive[] = {0,0.2,0,1};
			colorBackgroundDisabled[] = {0.2,0.2,0.2,1};
			colorBorder[] = {0,0,0,0};
			colorDisabled[] = {0.2,0.2,0.2,1};
			colorFocused[] = {0.2,0.2,0.2,1};
			colorShadow[] = {0,0,0,1};
			colorText[] = {0.9098,0.8588,0.9804,1};
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
            onMouseButtonDown = "[2] execVM 'rc_pos\reposicionar.sqf'";
			
		};
		
	};
	
};
