# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(['quizapp.py'],
             pathex=[],
             binaries=[],
             datas=[('mathquizapp.kv', '.'), ('STHeiti Medium.ttc', '.'), ('bg.png','.')], # 添加资源文件
             hiddenimports=['kivy','kivy_garden.graph'],
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
          name='quizapp',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='quizapp')