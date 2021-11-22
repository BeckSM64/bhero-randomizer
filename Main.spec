# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['Main.py'],
             pathex=['D:\\github\\bhero-randomizer'],
             binaries=[],
             datas=[ ('./Assets/BomberMad.ico', './Assets') ],
             hiddenimports=[],
             hookspath=[],
             hooksconfig={},
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
          a.binaries + [('BomberMad.ico', './Assets/BomberMad.ico', 'DATA')],
          a.zipfiles,
          a.datas,  
          [],
          name='BombermanHeroRandomizer',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None , icon='./Assets/BomberMad.ico')
