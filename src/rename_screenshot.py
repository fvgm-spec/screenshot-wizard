#!/usr/bin/env python3
"""
Screenshot Renamer

This script renames the most recent screenshot in the Screenshots directory
to a more meaningful name and moves it to the Misc directory.

Usage:
    rename_screenshot.py <new_name> [--location=<location>] [--ext=<extension>]

Arguments:
    new_name            New name for the screenshot (without extension)
    --location=<loc>    Optional location/category for organizing screenshots
    --ext=<extension>   Optional file extension (default: png)

Example:
    rename_screenshot.py aws_lambda_function --location=aws --ext=jpg
"""

import os
import sys
import shutil
import argparse
from datetime import datetime
from pathlib import Path

# Define constants
SCREENSHOTS_DIR = Path('/home/felix/Pictures/Screenshots')
DESTINATION_DIR = Path('/home/felix/Pictures/Misc')

def get_most_recent_screenshot():
    """Get the most recent screenshot from the Screenshots directory."""
    if not SCREENSHOTS_DIR.exists():
        print(f"Error: Screenshots directory not found at {SCREENSHOTS_DIR}")
        sys.exit(1)
    
    screenshots = list(SCREENSHOTS_DIR.glob('Screenshot from *.png'))
    
    if not screenshots:
        print("No screenshots found in the Screenshots directory.")
        sys.exit(1)
    
    # Sort by modification time (most recent last)
    screenshots.sort(key=lambda x: x.stat().st_mtime)
    return screenshots[-1]

def rename_screenshot(screenshot_path, new_name, location=None, extension='png'):
    """Rename and move the screenshot to the destination directory."""
    # Create destination directory if it doesn't exist
    DESTINATION_DIR.mkdir(parents=True, exist_ok=True)
    
    # Add location subdirectory if specified
    if location:
        dest_dir = DESTINATION_DIR / location
        dest_dir.mkdir(exist_ok=True)
    else:
        dest_dir = DESTINATION_DIR
    
    # Format the new filename with timestamp
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    new_filename = f"{new_name}_{timestamp}.{extension}"
    
    # Create the destination path
    destination_path = dest_dir / new_filename
    
    # Copy the file to the new location with the new name
    shutil.copy2(screenshot_path, destination_path)
    
    print(f"Screenshot renamed and copied:")
    print(f"  From: {screenshot_path}")
    print(f"  To:   {destination_path}")
    
    return destination_path

def main():
    parser = argparse.ArgumentParser(description='Rename and organize screenshots')
    parser.add_argument('new_name', help='New name for the screenshot (without extension)')
    parser.add_argument('--location', help='Optional location/category for organizing screenshots')
    parser.add_argument('--ext', default='png', help='File extension (default: png)')
    
    args = parser.parse_args()
    
    # Get the most recent screenshot
    screenshot_path = get_most_recent_screenshot()
    
    # Rename and move the screenshot
    new_path = rename_screenshot(
        screenshot_path, 
        args.new_name, 
        args.location, 
        args.ext
    )
    
    # Print the new path for potential use in other scripts
    print(f"\nNew path: {new_path}")

if __name__ == '__main__':
    main()
