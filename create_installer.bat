@echo off
echo ===== Creating Tissue Fragment Stitching Tool Installer =====
echo.

REM Check if the executable exists
if not exist "dist\TissueStitcher\TissueStitcher.exe" (
    echo ERROR: Executable not found!
    echo Please run build_windows.py first to create the executable.
    pause
    exit /b 1
)

REM Create icon if it doesn't exist
if not exist "icon.ico" (
    echo Creating application icon...
    python create_icon.py
)

REM Create installer directory
if not exist "installer" mkdir installer

REM Try to run Inno Setup
echo Creating installer with Inno Setup...
iscc tissue_stitcher_setup.iss

if %errorlevel% neq 0 (
    echo.
    echo ERROR: Inno Setup failed or not found
    echo.
    echo Please install Inno Setup from: https://jrsoftware.org/isinfo.php
    echo After installation, you can run this command manually:
    echo   iscc tissue_stitcher_setup.iss
    echo.
    pause
    exit /b 1
)

echo.
echo ===== Installer Created Successfully =====
echo.
echo Installer location: installer\TissueStitcher-Setup-v1.0.1.exe
echo.
echo The installer includes:
echo - Main application executable
echo - All required DLLs and dependencies
echo - Documentation and user guide
echo - Desktop and Start Menu shortcuts
echo - Uninstaller
echo.
echo You can now distribute this installer to end users.
echo No additional software installation required on target machines.
echo.
pause