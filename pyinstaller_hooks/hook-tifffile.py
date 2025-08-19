"""
PyInstaller hook for tifffile
Ensures all tifffile dependencies are included
"""

from PyInstaller.utils.hooks import collect_submodules, collect_data_files

# Collect all tifffile submodules
hiddenimports = collect_submodules('tifffile')

# Collect data files
datas = collect_data_files('tifffile')

# Add specific imports that might be missed
hiddenimports += [
    'tifffile._tifffile',
    'tifffile.tifffile',
    'imagecodecs',
    'imagecodecs._imagecodecs',
]