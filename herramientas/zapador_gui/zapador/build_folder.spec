# -*- mode: python ; coding: utf-8 -*-

from kivy_deps import sdl2, glew

block_cipher = None


a = Analysis(['main.py'],
             pathex=['D:\\github\\corp-0\\ZR_KDM\\herramientas\\zapador_gui\\zapador'],
             binaries=[],
             datas=[],
             hiddenimports=['win32timezone', 'zapador'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='zapador',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False )
coll = COLLECT(exe, Tree('D:\github\corp-0\ZR_KDM\herramientas\zapador_gui\zapador\zapador', 'zapador'),
               a.binaries,
               a.zipfiles,
               a.datas,
               *[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins)],
               strip=False,
               upx=True,
               upx_exclude=[],
               name='zapador',
               icon='D:\github\corp-0\ZR_KDM\herramientas\zapador_gui\zapador\zapador\assets\img\zapador.ico')
