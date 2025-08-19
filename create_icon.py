#!/usr/bin/env python3
"""
Create an icon file for the application
"""

from PIL import Image, ImageDraw
import os

def create_icon():
    """Create a simple icon for the application"""
    # Create a 256x256 image with transparent background
    size = 256
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Draw a simple microscope-like icon
    # Base color scheme: blue and white
    primary_color = (74, 144, 226, 255)  # Blue
    secondary_color = (255, 255, 255, 255)  # White
    accent_color = (220, 53, 69, 255)  # Red accent
    
    # Draw microscope base
    base_rect = [size//4, size*3//4, size*3//4, size*7//8]
    draw.rectangle(base_rect, fill=primary_color)
    
    # Draw microscope body
    body_rect = [size*3//8, size//4, size*5//8, size*3//4]
    draw.rectangle(body_rect, fill=primary_color)
    
    # Draw eyepiece
    eyepiece_rect = [size*7//16, size//8, size*9//16, size//4]
    draw.rectangle(eyepiece_rect, fill=secondary_color)
    
    # Draw objective lens
    lens_center = (size//2, size*5//8)
    lens_radius = size//16
    draw.ellipse([lens_center[0]-lens_radius, lens_center[1]-lens_radius,
                  lens_center[0]+lens_radius, lens_center[1]+lens_radius], 
                 fill=accent_color)
    
    # Draw sample fragments (small rectangles)
    fragment_size = size//20
    fragments = [
        (size//3, size*2//3),
        (size*2//3, size*2//3),
        (size//2, size*3//4)
    ]
    
    for fx, fy in fragments:
        draw.rectangle([fx-fragment_size, fy-fragment_size,
                       fx+fragment_size, fy+fragment_size], 
                      fill=accent_color)
    
    # Save as ICO file with multiple sizes
    icon_sizes = [(16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)]
    
    # Create images for each size
    images = []
    for icon_size in icon_sizes:
        resized = img.resize(icon_size, Image.Resampling.LANCZOS)
        images.append(resized)
    
    # Save as ICO
    img.save('icon.ico', format='ICO', sizes=[(img.width, img.height) for img in images])
    print("✓ Created icon.ico")

if __name__ == "__main__":
    create_icon()