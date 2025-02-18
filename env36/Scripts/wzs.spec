# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['C:\\Users\\ceefh\\Desktop\\wzs\\wzs.py'],
             pathex=[],
             binaries=[],
             datas=[('C:\\Users\\ceefh\\Desktop\\wzs\\resource\\datasets', 'pyecharts\\datasets\\.'), ('C:\\Users\\ceefh\\Desktop\\wzs\\resource\\templates', 'pyecharts\\render\\templates\\.')],
             hiddenimports=[],
             hookspath=['C:\\Users\\ceefh\\Desktop\\wzs\\resource\hooks'],
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
          [],
          exclude_binaries=True,
          name='wzs',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas, 
               strip=False,
               upx=True,
               upx_exclude=[],
               name='wzs')
