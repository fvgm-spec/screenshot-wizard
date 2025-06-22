#!/usr/bin/env python3
"""
Screenshot Manager

A comprehensive tool for managing screenshots with features like:
- Renaming the most recent screenshot
- Batch renaming multiple screenshots
- Organizing screenshots into categories
- Viewing screenshot information
- Searching for screenshots

Usage:
    screenshot_manager.py rename <new_name> [--location=<location>] [--ext=<extension>]
    screenshot_manager.py batch <prefix> <count> [--location=<location>] [--ext=<extension>]
    screenshot_manager.py list [--days=<days>]
    screenshot_manager.py search <keyword>
    screenshot_manager.py info [--latest]

Examples:
    screenshot_manager.py rename aws_lambda_function --location=aws
    screenshot_manager.py batch meeting_slides 5 --location=presentations
    screenshot_manager.py list --days=7
    screenshot_manager.py search aws
    screenshot_manager.py info --latest
"""

import os
import sys
import shutil
import argparse
import time
from datetime import datetime, timedelta
from pathlib import Path
from PIL import Image
import subprocess

# Define constants
SCREENSHOTS_DIR = Path('/home/felix/Pictures/Screenshots')
DESTINATION_DIR = Path('/home/felix/Pictures/Misc')

def get_screenshots(days=None, count=None):
    """
    Get screenshots from the Screenshots directory.
    
    Args:
        days: Only include screenshots from the last N days
        count: Only return the N most recent screenshots
    
    Returns:
        List of screenshot paths sorted by modification time (newest first)
    """
    if not SCREENSHOTS_DIR.exists():
        print(f"Error: Screenshots directory not found at {SCREENSHOTS_DIR}")
        sys.exit(1)
    
    screenshots = list(SCREENSHOTS_DIR.glob('Screenshot from *.png'))
    
    if not screenshots:
        print("No screenshots found in the Screenshots directory.")
        sys.exit(1)
    
    # Filter by days if specified
    if days:
        cutoff_time = time.time() - (days * 86400)  # 86400 seconds in a day
        screenshots = [s for s in screenshots if s.stat().st_mtime >= cutoff_time]
    
    # Sort by modification time (newest first)
    screenshots.sort(key=lambda x: x.stat().st_mtime, reverse=True)
    
    # Limit by count if specified
    if count and count < len(screenshots):
        screenshots = screenshots[:count]
    
    return screenshots

def get_image_info(image_path):
    """Get information about an image file."""
    try:
        with Image.open(image_path) as img:
            width, height = img.size
            format = img.format
            mode = img.mode
            
            file_stat = image_path.stat()
            size_kb = file_stat.st_size / 1024
            mod_time = datetime.fromtimestamp(file_stat.st_mtime)
            
            return {
                'path': str(image_path),
                'dimensions': f"{width}x{height}",
                'format': format,
                'mode': mode,
                'size': f"{size_kb:.1f} KB",
                'modified': mod_time.strftime('%Y-%m-%d %H:%M:%S')
            }
    except Exception as e:
        return {
            'path': str(image_path),
            'error': str(e)
        }

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

def batch_rename_screenshots(screenshots, prefix, location=None, extension='png'):
    """Batch rename multiple screenshots with sequential numbering."""
    renamed_paths = []
    
    for i, screenshot in enumerate(screenshots, 1):
        new_name = f"{prefix}_{i:02d}"
        new_path = rename_screenshot(screenshot, new_name, location, extension)
        renamed_paths.append(new_path)
    
    return renamed_paths

def search_screenshots(keyword):
    """Search for screenshots in both directories by filename."""
    results = []
    
    # Search in Screenshots directory
    for path in SCREENSHOTS_DIR.glob('*'):
        if keyword.lower() in path.name.lower():
            results.append(path)
    
    # Search in Misc directory (including subdirectories)
    for path in DESTINATION_DIR.glob('**/*'):
        if path.is_file() and keyword.lower() in path.name.lower():
            results.append(path)
    
    return results

def list_screenshots(days=None):
    """List screenshots from both directories."""
    screenshots = []
    
    # Get screenshots from Screenshots directory
    for path in SCREENSHOTS_DIR.glob('Screenshot from *.png'):
        if days:
            cutoff_time = time.time() - (days * 86400)
            if path.stat().st_mtime < cutoff_time:
                continue
        screenshots.append(path)
    
    # Get screenshots from Misc directory (including subdirectories)
    for path in DESTINATION_DIR.glob('**/*'):
        if path.is_file() and path.suffix.lower() in ['.png', '.jpg', '.jpeg', '.gif']:
            if days:
                cutoff_time = time.time() - (days * 86400)
                if path.stat().st_mtime < cutoff_time:
                    continue
            screenshots.append(path)
    
    # Sort by modification time (newest first)
    screenshots.sort(key=lambda x: x.stat().st_mtime, reverse=True)
    
    return screenshots

def display_screenshot_info(screenshot_path):
    """Display detailed information about a screenshot."""
    info = get_image_info(screenshot_path)
    
    print(f"\nScreenshot Information:")
    print(f"  Path:       {info['path']}")
    print(f"  Dimensions: {info.get('dimensions', 'N/A')}")
    print(f"  Format:     {info.get('format', 'N/A')}")
    print(f"  Size:       {info.get('size', 'N/A')}")
    print(f"  Modified:   {info.get('modified', 'N/A')}")
    
    # Try to get creation date from EXIF data if available
    try:
        with Image.open(screenshot_path) as img:
            if hasattr(img, '_getexif') and img._getexif():
                exif = img._getexif()
                if exif and 306 in exif:  # 306 is the tag for DateTime
                    print(f"  Created:    {exif[306]}")
    except:
        pass

def cmd_rename(args):
    """Handle the rename command."""
    screenshot = get_screenshots(count=1)[0]
    new_path = rename_screenshot(screenshot, args.new_name, args.location, args.ext)
    return new_path

def cmd_batch(args):
    """Handle the batch command."""
    screenshots = get_screenshots(count=args.count)
    if len(screenshots) < args.count:
        print(f"Warning: Only found {len(screenshots)} screenshots, but {args.count} were requested.")
    
    renamed_paths = batch_rename_screenshots(screenshots, args.prefix, args.location, args.ext)
    return renamed_paths

def cmd_list(args):
    """Handle the list command."""
    screenshots = list_screenshots(args.days)
    
    if not screenshots:
        print("No screenshots found.")
        return
    
    print(f"\nFound {len(screenshots)} screenshots:")
    for i, path in enumerate(screenshots, 1):
        size_kb = path.stat().st_size / 1024
        mod_time = datetime.fromtimestamp(path.stat().st_mtime).strftime('%Y-%m-%d %H:%M:%S')
        print(f"{i:3d}. {path.name:<40} {size_kb:6.1f} KB  {mod_time}")
    
    return screenshots

def cmd_search(args):
    """Handle the search command."""
    results = search_screenshots(args.keyword)
    
    if not results:
        print(f"No screenshots found matching '{args.keyword}'.")
        return
    
    print(f"\nFound {len(results)} screenshots matching '{args.keyword}':")
    for i, path in enumerate(results, 1):
        size_kb = path.stat().st_size / 1024
        mod_time = datetime.fromtimestamp(path.stat().st_mtime).strftime('%Y-%m-%d %H:%M:%S')
        print(f"{i:3d}. {path.name:<40} {size_kb:6.1f} KB  {mod_time}")
    
    return results

def cmd_info(args):
    """Handle the info command."""
    if args.latest:
        screenshot = get_screenshots(count=1)[0]
        display_screenshot_info(screenshot)
    else:
        # Interactive mode - list screenshots and let user choose
        screenshots = list_screenshots(args.days)
        
        if not screenshots:
            print("No screenshots found.")
            return
        
        print("\nEnter the number of the screenshot to view details (or 'q' to quit):")
        choice = input("> ")
        
        if choice.lower() == 'q':
            return
        
        try:
            index = int(choice) - 1
            if 0 <= index < len(screenshots):
                display_screenshot_info(screenshots[index])
            else:
                print("Invalid selection.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    parser = argparse.ArgumentParser(description='Screenshot Manager')
    subparsers = parser.add_subparsers(dest='command', help='Command to execute')
    
    # Rename command
    rename_parser = subparsers.add_parser('rename', help='Rename the most recent screenshot')
    rename_parser.add_argument('new_name', help='New name for the screenshot (without extension)')
    rename_parser.add_argument('--location', help='Optional location/category for organizing screenshots')
    rename_parser.add_argument('--ext', default='png', help='File extension (default: png)')
    
    # Batch command
    batch_parser = subparsers.add_parser('batch', help='Batch rename multiple screenshots')
    batch_parser.add_argument('prefix', help='Prefix for the new filenames')
    batch_parser.add_argument('count', type=int, help='Number of recent screenshots to rename')
    batch_parser.add_argument('--location', help='Optional location/category for organizing screenshots')
    batch_parser.add_argument('--ext', default='png', help='File extension (default: png)')
    
    # List command
    list_parser = subparsers.add_parser('list', help='List screenshots')
    list_parser.add_argument('--days', type=int, help='Only show screenshots from the last N days')
    
    # Search command
    search_parser = subparsers.add_parser('search', help='Search for screenshots by name')
    search_parser.add_argument('keyword', help='Keyword to search for in filenames')
    
    # Info command
    info_parser = subparsers.add_parser('info', help='Display information about screenshots')
    info_parser.add_argument('--latest', action='store_true', help='Show info for the most recent screenshot')
    info_parser.add_argument('--days', type=int, help='Only consider screenshots from the last N days')
    
    args = parser.parse_args()
    
    if args.command == 'rename':
        cmd_rename(args)
    elif args.command == 'batch':
        cmd_batch(args)
    elif args.command == 'list':
        cmd_list(args)
    elif args.command == 'search':
        cmd_search(args)
    elif args.command == 'info':
        cmd_info(args)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
