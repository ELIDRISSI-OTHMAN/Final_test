# Windows Build Instructions

This document provides step-by-step instructions for building the Tissue Fragment Stitching Tool for Windows.

## Prerequisites

1. **Anaconda/Miniconda** installed and added to PATH
2. **Inno Setup** (download from https://jrsoftware.org/isinfo.php)
3. **Visual Studio Build Tools** (for some Python packages)

## Quick Build (Automated)

1. Open Command Prompt as Administrator
2. Navigate to the project directory
3. Run the automated build script:
   ```cmd
   build_installer.bat
   ```

This will:
- Activate the conda environment
- Install build dependencies
- Create the executable with PyInstaller
- Generate the installer with Inno Setup

## Manual Build Process

### Step 1: Environment Setup

```cmd
# Activate the conda environment
conda activate stitcher

# Verify environment
python fix_conda_paths.py
```

### Step 2: Install Build Dependencies

```cmd
pip install -r requirements-build.txt
```

### Step 3: Create Application Icon

```cmd
python create_icon.py
```

### Step 4: Generate PyInstaller Spec

```cmd
python build_spec.py
```

### Step 5: Build Executable

```cmd
python build_windows.py
```

Or manually with PyInstaller:
```cmd
pyinstaller TissueStitcher.spec
```

### Step 6: Create Installer

```cmd
iscc tissue_stitcher_setup.iss
```

## Troubleshooting

### Common Issues

1. **PyQt6 not found**
   - Ensure PyQt6 is installed in the conda environment
   - Check that the environment is properly activated

2. **Missing DLLs**
   - Run `fix_conda_paths.py` to diagnose
   - Manually copy missing DLLs to the dist folder

3. **OpenSlide errors**
   - Ensure openslide-python is installed via conda
   - Check that OpenSlide DLLs are in the conda environment

4. **Import errors**
   - Add missing modules to hidden imports in the spec file
   - Use `--collect-all` flag for problematic packages

### Manual DLL Copying

If automatic DLL detection fails, manually copy these DLLs from your conda environment to the `dist/TissueStitcher/` folder:

From `%CONDA_PREFIX%\Library\bin\`:
- `libopenslide-0.dll`
- `libglib-2.0-0.dll`
- `libgobject-2.0-0.dll`
- `libjpeg-8.dll`
- `libpng16-16.dll`
- `libtiff-5.dll`
- `libxml2-2.dll`
- `zlib1.dll`

From `%CONDA_PREFIX%\DLLs\`:
- Any missing Python DLLs

### Testing the Build

1. Test the executable directly:
   ```cmd
   dist\TissueStitcher\TissueStitcher.exe
   ```

2. Test on a clean Windows machine without Python/conda installed

3. Check Windows Event Viewer for any runtime errors

## Build Output

- **Executable**: `dist/TissueStitcher/TissueStitcher.exe`
- **Installer**: `installer/TissueStitcher-Setup-v1.0.0.exe`

## Distribution

The installer (`TissueStitcher-Setup-v1.0.0.exe`) is a self-contained package that can be distributed to end users. It includes:

- The main application
- All required DLLs and dependencies
- Documentation (README, LICENSE)
- Desktop and Start Menu shortcuts
- Uninstaller

## Advanced Configuration

### Custom Icon
Replace `icon.ico` with your custom icon file (256x256 recommended).

### Version Information
Edit `version_info.txt` to update version numbers and company information.

### Installer Customization
Modify `tissue_stitcher_setup.iss` to customize:
- Installation directory
- File associations
- Registry entries
- Custom actions

### Performance Optimization

For smaller executable size:
- Use `--onefile` instead of `--onedir` in PyInstaller
- Remove unused packages from hidden imports
- Use UPX compression (already enabled)

For faster startup:
- Keep `--onedir` mode
- Exclude unnecessary modules
- Use lazy imports in the code