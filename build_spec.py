#!/usr/bin/env python3
"""
Generate PyInstaller spec file with proper conda environment support
"""

import os
import sys
from pathlib import Path

def generate_spec_file():
    """Generate a comprehensive PyInstaller spec file"""
    
    conda_prefix = os.environ.get('CONDA_PREFIX', '')
    conda_path = Path(conda_prefix) if conda_prefix else Path()
    
    # Build pathex (additional paths for PyInstaller)
    pathex = [
        str(Path.cwd()),  # Current directory
    ]
    
    if conda_prefix:
        potential_paths = [
            conda_path / "Library" / "bin",
            conda_path / "DLLs", 
            conda_path / "Scripts",
            conda_path / "Lib" / "site-packages",
        ]
        pathex.extend([str(p) for p in potential_paths if p.exists()])
    
    # Build binaries list
    binaries = []
    
    if conda_prefix:
        # Add OpenSlide DLLs
        openslide_bin = conda_path / "Library" / "bin"
        if openslide_bin.exists():
            openslide_dlls = [
                'libopenslide-0.dll', 'libglib-2.0-0.dll', 'libgobject-2.0-0.dll',
                'libjpeg-8.dll', 'libpng16-16.dll', 'libtiff-5.dll', 'libxml2-2.dll',
                'zlib1.dll', 'libopenjp2-7.dll', 'libgdk_pixbuf-2.0-0.dll',
                'libgio-2.0-0.dll', 'libgmodule-2.0-0.dll'
            ]
            
            for dll in openslide_dlls:
                dll_path = openslide_bin / dll
                if dll_path.exists():
                    binaries.append(f"(r'{dll_path}', '.')")
    
    # Hidden imports
    hidden_imports = [
        'PyQt6', 'PyQt6.QtCore', 'PyQt6.QtGui', 'PyQt6.QtWidgets',
        'PyQt6.QtOpenGLWidgets', 'cv2', 'numpy', 'PIL', 'PIL.Image',
        'openslide', 'tifffile', 'scipy', 'scipy.optimize', 'skimage',
        'skimage.feature', 'skimage.transform', 'matplotlib',
        'imagecodecs', 'imagecodecs._imagecodecs'
    ]
    
    # Data files
    datas = [
        "('LICENSE', '.')",
        "('README.md', '.')",
    ]
    
    # Generate spec file content
    spec_content = f'''# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['main.py'],
    pathex={pathex},
    binaries=[
        {','.join(binaries) if binaries else ''}
    ],
    datas=[
        {','.join(datas)}
    ],
    hiddenimports={hidden_imports},
    hookspath=['pyinstaller_hooks'],
    hooksconfig={{}},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='TissueStitcher',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    version='version_info.txt',
    icon='icon.ico'
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='TissueStitcher',
)
'''
    
    # Write spec file
    with open('TissueStitcher.spec', 'w') as f:
        f.write(spec_content)
    
    print("✓ Generated TissueStitcher.spec")
    print(f"  Pathex entries: {len(pathex)}")
    print(f"  Binary entries: {len(binaries)}")
    print(f"  Hidden imports: {len(hidden_imports)}")

if __name__ == "__main__":
    generate_spec_file()