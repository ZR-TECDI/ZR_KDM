# -*- mode: python ; coding: utf-8 -*-

from kivy_deps import sdl2, glew

block_cipher = None

a = Analysis(['main.py'],
             pathex=['D:\\github\\corp-0\\ZR_KDM\\herramientas\\zapador'],
             binaries=[],
             datas=[],
             hiddenimports=['win32timezone', 'zapador', 'distutils'],
             hookspath=[],
             runtime_hooks=[],
             excludes=['audio', 'video', 'camera', 'spelling', 'audio_sdl2', 'cv2'],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz, Tree('D://github/corp-0/ZR_KDM/herramientas/zapador/zapador', 'zapador'),
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          *[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins)],
          name='zapador',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True,
          icon='D:\\github\\corp-0\\ZR_KDM\\herramientas\\zapador\\zapador\\assets\\img\\zapador.ico')
