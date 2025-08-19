"""
PyInstaller hook for openslide-python
Ensures OpenSlide DLLs are included in the build
"""

from PyInstaller.utils.hooks import collect_dynamic_libs, collect_data_files, collect_submodules
import os
import glob

# Collect OpenSlide DLLs
binaries = collect_dynamic_libs('openslide')

# Collect openslide_bin package
hiddenimports = collect_submodules('openslide_bin')

# Try to find OpenSlide DLLs in conda environment
conda_prefix = os.environ.get('CONDA_PREFIX')
if conda_prefix:
    openslide_bin = os.path.join(conda_prefix, 'Library', 'bin')
    if os.path.exists(openslide_bin):
        # Look for all OpenSlide related DLLs (both version 0 and 1)
        openslide_dlls = [
            'libopenslide-0.dll', 'libopenslide-1.dll',  # Both versions
            'libglib-2.0-0.dll', 'libgobject-2.0-0.dll', 'libgmodule-2.0-0.dll',
            'libgio-2.0-0.dll', 'libgdk_pixbuf-2.0-0.dll', 'libgthread-2.0-0.dll',
            'libjpeg-8.dll', 'libpng16-16.dll', 'libtiff-5.dll', 'libxml2-2.dll',
            'zlib1.dll', 'libopenjp2-7.dll', 'libiconv-2.dll', 'libintl-8.dll',
            'libffi-8.dll', 'libpcre2-8-0.dll', 'libsqlite3-0.dll',
            'libcairo-2.dll', 'libpixman-1-0.dll', 'libfontconfig-1.dll',
            'libfreetype-6.dll', 'libharfbuzz-0.dll', 'libpango-1.0-0.dll',
            'libpangocairo-1.0-0.dll', 'libpangoft2-1.0-0.dll', 'libpangowin32-1.0-0.dll'
        ]
        
        for dll_name in openslide_dlls:
            dll_path = os.path.join(openslide_bin, dll_name)
            if os.path.exists(dll_path):
                binaries.append((dll_path, '.'))
        
        # Also look for any openslide*.dll files using glob
        openslide_pattern = os.path.join(openslide_bin, '*openslide*.dll')
        for dll_path in glob.glob(openslide_pattern):
            binaries.append((dll_path, '.'))

# Also try to find openslide-bin package DLLs
try:
    import openslide_bin
    openslide_bin_path = os.path.dirname(openslide_bin.__file__)
    
    # Look for DLLs in the openslide_bin package
    for dll_file in glob.glob(os.path.join(openslide_bin_path, '*.dll')):
        binaries.append((dll_file, 'openslide_bin'))
        
    # Also collect the entire openslide_bin package
    datas += collect_data_files('openslide_bin')
    
except ImportError:
    pass

# Collect any data files
datas = collect_data_files('openslide')