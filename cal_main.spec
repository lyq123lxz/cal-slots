# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['D:\\Users\\Administrator\\PycharmProjects\\PythonProject9\\cal_main.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('data/1.jpg', 'data'),
        ('data/2.jpg', 'data'),
        ('data/3.jpg', 'data'),
        ('data/4.jpg', 'data'),
        ('data/5.jpg', 'data'),
        ('data/6.jpg', 'data'),
        ('data/7.jpg', 'data'),
        ('data/8.jpg', 'data'),
        ('data/9.jpg', 'data'),
        ('data/10.jpg', 'data'),
        ('data/11.jpg', 'data'),
        ('data/12.jpg', 'data'),
    ],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    a.binaries,
    a.datas,
    [],
    name='cal_main',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    onefile=True,  # 添加这一行以启用单文件模式
)