"""
PyInstaller hook for openslide-python
Ensures OpenSlide DLLs are included in the build
"""

from PyInstaller.utils.hooks import collect_dynamic_libs, collect_data_files
import os

# Collect OpenSlide DLLs
binaries = collect_dynamic_libs('openslide')

# Try to find OpenSlide DLLs in conda environment
conda_prefix = os.environ.get('CONDA_PREFIX')
if conda_prefix:
    openslide_bin = os.path.join(conda_prefix, 'Library', 'bin')
    if os.path.exists(openslide_bin):
        for dll_name in ['libopenslide-0.dll', 'libglib-2.0-0.dll', 'libgobject-2.0-0.dll',
                        'libjpeg-8.dll', 'libpng16-16.dll', 'libtiff-5.dll', 'libxml2-2.dll',
                        'zlib1.dll', 'libopenjp2-7.dll']:
            dll_path = os.path.join(openslide_bin, dll_name)
            if os.path.exists(dll_path):
                binaries.append((dll_path, '.'))

# Collect any data files
datas = collect_data_files('openslide')