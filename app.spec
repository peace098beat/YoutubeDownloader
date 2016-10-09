# -*- mode: python -*-

block_cipher = None


a = Analysis(['app.py'],
             pathex=['C:\\Users\\FiFi\\Desktop\\PyYtDonwloaderApp'],
             binaries=None,
             datas=[('./logging.conf','.'),],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)

pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

my_project_tree = Tree('./')

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          my_project_tree,
          name='app',
          debug=False,
          strip=False,
          upx=False,
          console=False )
