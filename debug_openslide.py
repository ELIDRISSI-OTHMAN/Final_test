#!/usr/bin/env python3
"""
Debug script to check OpenSlide installation and DLL dependencies
"""

import os
import sys
from pathlib import Path

def check_openslide_installation():
    """Check OpenSlide installation and dependencies"""
    print("=== OpenSlide Installation Debug ===\n")
    
    # Check conda environment
    conda_prefix = os.environ.get('CONDA_PREFIX')
    print(f"Conda environment: {conda_prefix}")
    
    # Check openslide package
    try:
        import openslide
        print(f"✓ openslide package: {openslide.__file__}")
        print(f"  Version: {openslide.__version__}")
    except ImportError as e:
        print(f"✗ openslide package not found: {e}")
        return False
    
    # Check openslide_bin package
    try:
        import openslide_bin
        print(f"✓ openslide_bin package: {openslide_bin.__file__}")
        
        # List contents of openslide_bin directory
        openslide_bin_path = Path(openslide_bin.__file__).parent
        print(f"  Contents of {openslide_bin_path}:")
        for item in sorted(openslide_bin_path.iterdir()):
            if item.is_file():
                print(f"    {item.name} ({item.stat().st_size} bytes)")
                
    except ImportError as e:
        print(f"✗ openslide_bin package not found: {e}")
        print("  This is likely the cause of your DLL issues!")
        return False
    
    # Check low-level library loading
    try:
        import openslide.lowlevel
        print("✓ openslide.lowlevel imported successfully")
        
        # Try to access the library
        lib = openslide.lowlevel._lib
        print(f"✓ OpenSlide library loaded: {lib}")
        
    except Exception as e:
        print(f"✗ Failed to load OpenSlide low-level library: {e}")
        return False
    
    # Check conda Library/bin directory
    if conda_prefix:
        lib_bin = Path(conda_prefix) / "Library" / "bin"
        if lib_bin.exists():
            print(f"\n✓ Conda Library/bin: {lib_bin}")
            openslide_dlls = [f for f in lib_bin.glob("*openslide*.dll")]
            if openslide_dlls:
                print("  OpenSlide DLLs found:")
                for dll in openslide_dlls:
                    print(f"    {dll.name}")
            else:
                print("  ⚠ No OpenSlide DLLs found in Library/bin")
        else:
            print(f"✗ Conda Library/bin not found: {lib_bin}")
    
    print("\n=== Recommendations ===")
    print("If openslide_bin is missing, try:")
    print("  conda install -c conda-forge openslide-python")
    print("  pip install openslide-bin")
    
    return True

if __name__ == "__main__":
    success = check_openslide_installation()
    if not success:
        sys.exit(1)
    print("\n✓ OpenSlide installation appears to be working correctly")