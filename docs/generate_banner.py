#!/usr/bin/env python3
"""
Generate a banner image for Screenshot Wizard
"""

from PIL import Image, ImageDraw, ImageFont
import os

# Create a new image with a white background
width, height = 800, 200
image = Image.new('RGB', (width, height), color=(255, 255, 255))
draw = ImageDraw.Draw(image)

# Try to load a font, fall back to default if not available
try:
    font_large = ImageFont.truetype('DejaVuSans-Bold.ttf', 36)
    font_small = ImageFont.truetype('DejaVuSans.ttf', 18)
except IOError:
    font_large = ImageFont.load_default()
    font_small = font_large

# Draw the title
draw.text((50, 50), 'Screenshot Wizard', fill=(41, 128, 185), font=font_large)

# Draw the tagline
draw.text((50, 100), 'Organize and rename your screenshots with ease!', fill=(52, 73, 94), font=font_small)

# Draw a wizard hat icon (simplified)
draw.polygon([(700, 150), (650, 150), (675, 80)], fill=(155, 89, 182))
draw.ellipse((640, 140, 710, 160), fill=(155, 89, 182))

# Save the image
script_dir = os.path.dirname(os.path.abspath(__file__))
image.save(os.path.join(script_dir, 'banner.png'))
print(f"Banner saved to {os.path.join(script_dir, 'banner.png')}")
