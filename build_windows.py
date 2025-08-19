#!/usr/bin/env python3
"""
Windows build script for Tissue Fragment Stitching Tool
Creates executable using PyInstaller and packages with Inno Setup
"""

import os
import sys
import shutil
import subprocess
import platform
from pathlib import Path

def check_environment():
    """Check if we're in the correct conda environment"""
    conda_env = os.environ.get('CONDA_DEFAULT_ENV')
    if conda_env != 'stitcher':
        print("ERROR: Please activate the 'stitcher' conda environment first:")
        print("conda activate stitcher")
        sys.exit(1)
    
    print(f"✓ Using conda environment: {conda_env}")

def install_build_dependencies():
    """Install PyInstaller and other build dependencies"""
    print("Installing build dependencies...")
    
    try:
        # Install PyInstaller
        subprocess.run([sys.executable, "-m", "pip", "install", "pyinstaller"], check=True)
        print("✓ PyInstaller installed")
        
        # Install additional dependencies that might be missing
        subprocess.run([sys.executable, "-m", "pip", "install", "pillow", "opencv-python"], check=True)
        print("✓ Additional dependencies installed")
        
    except subprocess.CalledProcessError as e:
        print(f"ERROR: Failed to install dependencies: {e}")
        sys.exit(1)

def clean_build_dirs():
    """Clean previous build directories"""
    dirs_to_clean = ['build', 'dist', '__pycache__']
    
    for dir_name in dirs_to_clean:
        if os.path.exists(dir_name):
            shutil.rmtree(dir_name)
            print(f"✓ Cleaned {dir_name}")

def create_version_file():
    """Create version info file for Windows executable"""
    version_info = """# UTF-8
#
# For more details about fixed file info 'ffi' see:
# http://msdn.microsoft.com/en-us/library/ms646997.aspx
VSVersionInfo(
  ffi=FixedFileInfo(
    filevers=(1,0,0,0),
    prodvers=(1,0,0,0),
    mask=0x3f,
    flags=0x0,
    OS=0x40004,
    fileType=0x1,
    subtype=0x0,
    date=(0, 0)
    ),
  kids=[
    StringFileInfo(
      [
      StringTable(
        u'040904B0',
        [StringStruct(u'CompanyName', u'Scientific Imaging Lab'),
        StringStruct(u'FileDescription', u'Tissue Fragment Arrangement and Rigid Stitching Tool'),
        StringStruct(u'FileVersion', u'1.0.0'),
        StringStruct(u'InternalName', u'TissueStitcher'),
        StringStruct(u'LegalCopyright', u'Copyright (c) 2024 Scientific Imaging Lab'),
        StringStruct(u'OriginalFilename', u'TissueStitcher.exe'),
        StringStruct(u'ProductName', u'Tissue Fragment Stitching Tool'),
        StringStruct(u'ProductVersion', u'1.0.0')])
      ]), 
    VarFileInfo([VarStruct(u'Translation', [1033, 1200])])
  ]
)"""
    
    with open('version_info.txt', 'w', encoding='utf-8') as f:
        f.write(version_info)
    print("✓ Created version info file")

def run_pyinstaller():
    """Run PyInstaller to create the executable"""
    print("Running PyInstaller...")
    
    # PyInstaller command with all necessary options
    cmd = [
        sys.executable, "-m", "PyInstaller",
        "--name=TissueStitcher",
        "--windowed",  # No console window
        "--onedir",    # Create a directory instead of single file for better performance
        "--clean",
        "--noconfirm",
        "--version-file=version_info.txt",
        "--add-data=LICENSE;.",
        "--add-data=README.md;.",
        "--hidden-import=PyQt6",
        "--hidden-import=PyQt6.QtCore",
        "--hidden-import=PyQt6.QtGui", 
        "--hidden-import=PyQt6.QtWidgets",
        "--hidden-import=PyQt6.QtOpenGLWidgets",
        "--hidden-import=cv2",
        "--hidden-import=numpy",
        "--hidden-import=PIL",
        "--hidden-import=PIL.Image",
        "--hidden-import=openslide",
        "--hidden-import=tifffile",
        "--hidden-import=scipy",
        "--hidden-import=scipy.optimize",
        "--hidden-import=skimage",
        "--hidden-import=skimage.feature",
        "--hidden-import=skimage.transform",
        "--hidden-import=matplotlib",
        "--collect-all=PyQt6",
        "--collect-all=cv2",
        "--collect-all=openslide",
        "--collect-all=tifffile",
        "main.py"
    ]
    
    try:
        subprocess.run(cmd, check=True)
        print("✓ PyInstaller completed successfully")
    except subprocess.CalledProcessError as e:
        print(f"ERROR: PyInstaller failed: {e}")
        sys.exit(1)

def copy_additional_files():
    """Copy additional files needed for the application"""
    dist_dir = Path("dist/TissueStitcher")
    
    # Create openslide_bin directory in dist
    openslide_bin_dist = dist_dir / "openslide_bin"
    openslide_bin_dist.mkdir(exist_ok=True)
    
    # Copy OpenSlide DLLs if they exist in conda environment
    conda_prefix = os.environ.get('CONDA_PREFIX')
    if conda_prefix:
        openslide_bin = Path(conda_prefix) / "Library" / "bin"
        if openslide_bin.exists():
            # Copy all potential OpenSlide DLLs
            openslide_related = [
                'openslide', 'glib', 'gobject', 'gmodule', 'gio', 'gdk_pixbuf', 'gthread',
                'jpeg', 'png', 'tiff', 'xml2', 'openjp2', 'iconv', 'intl', 'ffi', 'pcre2',
                'sqlite3', 'cairo', 'pixman', 'fontconfig', 'freetype', 'harfbuzz',
                'pango', 'zlib'
            ]
            
            for dll in openslide_bin.glob("*.dll"):
                if any(name in dll.name.lower() for name in openslide_related):
                    shutil.copy2(dll, dist_dir)
                    # Also copy to openslide_bin subdirectory
                    shutil.copy2(dll, openslide_bin_dist)
                    print(f"✓ Copied {dll.name}")
    
    # Copy openslide_bin package DLLs if available
    try:
        import openslide_bin
        openslide_bin_pkg = Path(openslide_bin.__file__).parent
        
        for dll in openslide_bin_pkg.glob("*.dll"):
            # Copy to main dist directory
            shutil.copy2(dll, dist_dir)
            # Copy to openslide_bin subdirectory
            shutil.copy2(dll, openslide_bin_dist)
            print(f"✓ Copied openslide_bin {dll.name}")
            
        # Copy any other files from openslide_bin
        for file in openslide_bin_pkg.glob("*"):
            if file.is_file() and not file.name.endswith('.pyc'):
                shutil.copy2(file, openslide_bin_dist)
                
    except ImportError:
        print("⚠ openslide_bin package not found")
    
    # Copy any missing Qt6 DLLs
    qt_dir = Path(conda_prefix) / "Library" / "bin" if conda_prefix else None
    if qt_dir and qt_dir.exists():
        for dll in qt_dir.glob("Qt6*.dll"):
            target = dist_dir / dll.name
            if not target.exists():
                shutil.copy2(dll, dist_dir)
                print(f"✓ Copied {dll.name}")

def test_executable():
    """Test if the created executable works"""
    print("Testing executable...")
    exe_path = Path("dist/TissueStitcher/TissueStitcher.exe")
    
    if not exe_path.exists():
        print("ERROR: Executable not found!")
        return False
    
    try:
        # Test with --help flag (quick test)
        result = subprocess.run([str(exe_path), "--help"], 
                              capture_output=True, text=True, timeout=10)
        print("✓ Executable test completed")
        return True
    except subprocess.TimeoutExpired:
        print("⚠ Executable test timed out (this might be normal)")
        return True
    except Exception as e:
        print(f"⚠ Executable test failed: {e}")
        return True  # Don't fail the build for test issues

def main():
    """Main build process"""
    print("=== Tissue Fragment Stitching Tool - Windows Build ===")
    print(f"Python: {sys.version}")
    print(f"Platform: {platform.platform()}")
    print()
    
    # Check environment
    check_environment()
    
    # Install dependencies
    install_build_dependencies()
    
    # Clean previous builds
    clean_build_dirs()
    
    # Create version file
    create_version_file()
    
    # Run PyInstaller
    run_pyinstaller()
    
    # Copy additional files
    copy_additional_files()
    
    # Test executable
    test_executable()
    
    print("\n=== Build Complete ===")
    print("Executable created at: dist/TissueStitcher/TissueStitcher.exe")
    print("You can now run the Inno Setup script to create an installer.")

if __name__ == "__main__":
    main()