params ["_toque"];

speakers = [speaker_1, speaker_2, speaker_3, speaker_4, speaker_5, speaker_6, speaker_7, speaker_8];

switch _toque do
{
	case 1:
	{
		speakers apply{
			[_x, "toque1.ogg"] call ZR_fnc_reproducirSonido3D;
		};
	};
	case 2:
	{
		speakers apply{
			[_x, "toque2.ogg"] call ZR_fnc_reproducirSonido3D;
		};
	};
	case 3:
	{
		speakers apply{
			[_x, "toque3.ogg"] call ZR_fnc_reproducirSonido3D;
		};
	};
	case 4:
	{
		speakers apply{
			[_x, "toque4.ogg"] call ZR_fnc_reproducirSonido3D;
		};
	};

};

