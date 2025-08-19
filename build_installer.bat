@echo off
echo ===== Tissue Fragment Stitching Tool - Windows Build Script =====
echo.

REM Check if conda is available
where conda >nul 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo ERROR: Conda is not available in PATH
    echo Please install Anaconda/Miniconda and add it to PATH
    pause
    exit /b 1
)

REM Activate conda environment
echo Activating conda environment 'stitcher'...
call conda activate stitcher
if %ERRORLEVEL% NEQ 0 (
    echo ERROR: Failed to activate conda environment 'stitcher'
    echo Please make sure the environment exists: conda env list
    pause
    exit /b 1
)

REM Run the Python build script
echo Running Python build script...
python build_windows.py
if %ERRORLEVEL% NEQ 0 (
    echo ERROR: Python build script failed
    pause
    exit /b 1
)

REM Check if Inno Setup is available
where iscc >nul 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo.
    echo WARNING: Inno Setup Compiler (iscc) not found in PATH
    echo Please install Inno Setup from: https://jrsoftware.org/isinfo.php
    echo Then run: iscc tissue_stitcher_setup.iss
    echo.
    pause
    exit /b 0
)

REM Create installer directory
if not exist "installer" mkdir installer

REM Run Inno Setup
echo Creating installer with Inno Setup...
iscc tissue_stitcher_setup.iss
if %ERRORLEVEL% NEQ 0 (
    echo ERROR: Inno Setup failed
    pause
    exit /b 1
)

echo.
echo ===== Build Complete =====
echo Executable: dist\TissueStitcher\TissueStitcher.exe
echo Installer: installer\TissueStitcher-Setup-v1.0.0.exe
echo.
pause