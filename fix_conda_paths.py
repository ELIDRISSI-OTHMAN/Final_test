#!/usr/bin/env python3
"""
Fix conda environment paths for PyInstaller
This script helps resolve DLL and library path issues
"""

import os
import sys
import shutil
from pathlib import Path

def fix_conda_paths():
    """Fix common conda environment path issues"""
    conda_prefix = os.environ.get('CONDA_PREFIX')
    if not conda_prefix:
        print("ERROR: CONDA_PREFIX not set. Please activate your conda environment.")
        return False
    
    conda_path = Path(conda_prefix)
    print(f"Conda environment: {conda_path}")
    
    # Check for common DLL locations
    dll_locations = [
        conda_path / "Library" / "bin",
        conda_path / "DLLs",
        conda_path / "Scripts",
        conda_path / "bin"
    ]
    
    print("\nChecking DLL locations:")
    for location in dll_locations:
        if location.exists():
            dll_count = len(list(location.glob("*.dll")))
            print(f"  ✓ {location}: {dll_count} DLLs found")
        else:
            print(f"  ✗ {location}: Not found")
    
    # Check for PyQt6
    try:
        import PyQt6
        print(f"\n✓ PyQt6 found at: {PyQt6.__file__}")
        
        # Check for PyQt6 DLLs
        pyqt6_path = Path(PyQt6.__file__).parent
        qt_dlls = list(pyqt6_path.glob("**/Qt6*.dll"))
        print(f"  PyQt6 DLLs found: {len(qt_dlls)}")
        
    except ImportError:
        print("\n✗ PyQt6 not found!")
        return False
    
    # Check for OpenSlide
    try:
        import openslide
        print(f"✓ OpenSlide found at: {openslide.__file__}")
        
        # Try to create a test slide to verify DLLs
        try:
            # This will fail if DLLs are missing
            openslide.OpenSlide.__new__(openslide.OpenSlide)
        except Exception as e:
            print(f"  ⚠ OpenSlide DLL issue: {e}")
            
    except ImportError:
        print("✗ OpenSlide not found!")
    
    # Check for other critical libraries
    critical_libs = ['cv2', 'numpy', 'PIL', 'tifffile', 'scipy', 'matplotlib']
    print(f"\nChecking critical libraries:")
    
    for lib in critical_libs:
        try:
            module = __import__(lib)
            print(f"  ✓ {lib}: {module.__file__}")
        except ImportError:
            print(f"  ✗ {lib}: Not found!")
    
    return True

def create_path_file():
    """Create a paths file for PyInstaller"""
    conda_prefix = os.environ.get('CONDA_PREFIX')
    if not conda_prefix:
        return
    
    conda_path = Path(conda_prefix)
    
    # Create pathex list for PyInstaller
    pathex = [
        str(conda_path / "Library" / "bin"),
        str(conda_path / "DLLs"),
        str(conda_path / "Scripts"),
        str(conda_path / "Lib" / "site-packages"),
    ]
    
    # Filter existing paths
    pathex = [p for p in pathex if Path(p).exists()]
    
    # Write to file
    with open('conda_paths.txt', 'w') as f:
        for path in pathex:
            f.write(f"{path}\n")
    
    print(f"\n✓ Created conda_paths.txt with {len(pathex)} paths")

if __name__ == "__main__":
    print("=== Conda Environment Path Checker ===")
    
    if fix_conda_paths():
        create_path_file()
        print("\n✓ Environment check completed")
    else:
        print("\n✗ Environment check failed")
        sys.exit(1)