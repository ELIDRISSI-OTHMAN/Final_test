# Custom Icon Guide

## How to Add Your Own Icon

You have several options to replace the default icon with your custom one:

### Option 1: Simple Replacement (Recommended)
1. **Prepare your icon file:**
   - Name it `custom_icon.ico`
   - Place it in the project root directory (same folder as `main.py`)
   - The build system will automatically use it

2. **Icon Requirements:**
   - Format: `.ico` file
   - Recommended sizes: 16x16, 32x32, 48x48, 64x64, 128x128, 256x256
   - Background: Transparent preferred
   - Colors: Full color (32-bit) recommended

### Option 2: Direct Replacement
1. **Replace the generated icon:**
   - Create or obtain your `.ico` file
   - Rename it to `icon.ico`
   - Place it in the project root directory
   - It will be used for both the executable and installer

### Option 3: Convert from Other Formats
If you have a PNG, JPG, or other image format, you can convert it:

#### Using Online Converters:
- https://convertio.co/png-ico/
- https://www.icoconverter.com/
- https://favicon.io/favicon-converter/

#### Using Python (if you have PIL/Pillow):
```python
from PIL import Image

# Convert PNG to ICO
img = Image.open('your_image.png')
img.save('custom_icon.ico', format='ICO', sizes=[(256, 256), (128, 128), (64, 64), (32, 32), (16, 16)])
```

### Icon Design Tips:
1. **Keep it simple** - Icons look best when not too detailed
2. **High contrast** - Ensure it's visible on different backgrounds
3. **Square aspect ratio** - Icons should be square (1:1 ratio)
4. **Multiple sizes** - Include various sizes for different uses
5. **Transparent background** - Looks more professional

### Testing Your Icon:
1. **Place your `custom_icon.ico` in the project root**
2. **Rebuild the application:**
   ```cmd
   python build_windows.py
   ```
3. **Create the installer:**
   ```cmd
   create_installer.bat
   ```
4. **Check the results:**
   - Executable icon: `dist/TissueStitcher/TissueStitcher.exe`
   - Installer icon: The installer itself will use your icon
   - Desktop shortcut: Will use your icon after installation

### File Structure:
```
your_project/
├── main.py
├── custom_icon.ico          ← Your custom icon here
├── icon.ico                 ← Generated/copied automatically
├── build_windows.py
├── create_installer.bat
└── tissue_stitcher_setup.iss
```

### Troubleshooting:
- **Icon not showing:** Make sure the file is named exactly `custom_icon.ico`
- **Poor quality:** Ensure your source image is high resolution (at least 256x256)
- **Wrong format:** The file must be `.ico` format, not `.png` or `.jpg`
- **Build issues:** Delete `icon.ico` and rebuild to regenerate

The build system will automatically detect and use your custom icon throughout the application and installer.