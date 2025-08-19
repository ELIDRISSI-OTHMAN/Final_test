# Distribution Guide - Tissue Fragment Stitching Tool

## Creating the Installer

### Prerequisites
1. **Inno Setup** - Download from [https://jrsoftware.org/isinfo.php](https://jrsoftware.org/isinfo.php)
2. **Built executable** - Run `python build_windows.py` first

### Create Installer
```cmd
create_installer.bat
```

This will create: `installer/TissueStitcher-Setup-v1.0.1.exe`

## System Requirements for End Users

### Minimum Requirements
- **OS**: Windows 10 (64-bit) or Windows 11
- **RAM**: 8 GB (16 GB recommended)
- **Storage**: 2 GB free space
- **Graphics**: DirectX 11 compatible with OpenGL 2.1
- **Display**: 1920x1080 minimum

### Recommended Requirements
- **RAM**: 32 GB for large images
- **Storage**: SSD with 10+ GB free space
- **Graphics**: Dedicated GPU with 2GB+ VRAM
- **Display**: 2560x1440 or higher

## What's Included in the Installer

### Application Files
- `TissueStitcher.exe` - Main application
- All required DLLs (OpenSlide, Qt6, OpenCV, etc.)
- Python runtime and libraries
- Image processing libraries

### Documentation
- `USER_GUIDE.txt` - Complete user manual
- `SYSTEM_REQUIREMENTS.txt` - Detailed system requirements
- `README.md` - Project overview
- `LICENSE` - Software license

### Installation Features
- **No admin rights required** - Installs to user directory
- **Desktop shortcut** - Optional during installation
- **Start Menu entries** - Application and documentation
- **Uninstaller** - Clean removal of all files
- **File associations** - Optional TIFF file association

## Distribution Checklist

### Before Distribution
- [ ] Test installer on clean Windows 10/11 machine
- [ ] Verify all features work without Python/conda installed
- [ ] Test with sample TIFF files
- [ ] Check all documentation is up to date
- [ ] Verify uninstaller removes all files

### Installer Testing
```cmd
# Test on clean VM or machine without Python
TissueStitcher-Setup-v1.0.1.exe

# Test basic functionality
1. Load sample TIFF files
2. Manipulate fragments
3. Export composite image
4. Check all menu items work
```

### Distribution Methods

#### Direct Download
- Upload installer to file sharing service
- Provide download link with system requirements
- Include quick start guide

#### Enterprise Distribution
- Test with corporate antivirus software
- Provide IT deployment scripts if needed
- Document any firewall requirements

#### Academic Distribution
- Include citation information
- Provide sample datasets
- Create tutorial materials

## Troubleshooting for End Users

### Installation Issues
- **"Windows protected your PC"**: Click "More info" → "Run anyway"
- **Antivirus blocking**: Add exception for installer and install directory
- **Insufficient space**: Free up disk space (2GB minimum)

### Runtime Issues
- **Application won't start**: Update graphics drivers
- **Missing DLL errors**: Reinstall Microsoft Visual C++ Redistributable
- **Performance issues**: Check system requirements, close other applications

### File Format Issues
- **Can't load images**: Ensure TIFF files are properly formatted
- **Export fails**: Check available disk space and write permissions
- **Slow loading**: Use SSD storage, reduce image sizes

## Support Information

### User Support
- **Documentation**: Included USER_GUIDE.txt
- **System Requirements**: SYSTEM_REQUIREMENTS.txt
- **GitHub Issues**: For bug reports and feature requests

### Developer Support
- **Source Code**: Available on GitHub
- **Build Instructions**: See README_BUILD.md
- **API Documentation**: In source code comments

## Version Information

- **Current Version**: 1.0.1
- **Target Platform**: Windows 10/11 (64-bit)
- **Installer Size**: ~200-300 MB
- **Installation Size**: ~500-800 MB
- **Dependencies**: All included (no external requirements)

## Legal Considerations

### License
- Software distributed under MIT License
- Include license file with distribution
- Respect third-party library licenses

### Liability
- Software provided "as is"
- No warranty for specific use cases
- Users responsible for data backup

---

**Note**: Always test the installer on a clean machine before distribution to ensure all dependencies are properly included.