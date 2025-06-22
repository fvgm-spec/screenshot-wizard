#!/usr/bin/env python3
"""
Basic tests for Screenshot Wizard
"""

import os
import sys
import unittest
from pathlib import Path

# Add the src directory to the path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from rename_screenshot import get_most_recent_screenshot
from screenshot_manager import get_screenshots, get_image_info

class TestScreenshotWizard(unittest.TestCase):
    """Basic tests for Screenshot Wizard"""
    
    def test_import(self):
        """Test that modules can be imported"""
        import rename_screenshot
        import screenshot_manager
        self.assertTrue(True)
    
    def test_screenshot_dir_exists(self):
        """Test that the screenshots directory exists"""
        from rename_screenshot import SCREENSHOTS_DIR
        self.assertTrue(SCREENSHOTS_DIR.exists() or SCREENSHOTS_DIR.is_dir())
    
    def test_destination_dir_exists_or_can_be_created(self):
        """Test that the destination directory exists or can be created"""
        from rename_screenshot import DESTINATION_DIR
        if not DESTINATION_DIR.exists():
            DESTINATION_DIR.mkdir(parents=True, exist_ok=True)
        self.assertTrue(DESTINATION_DIR.exists() and DESTINATION_DIR.is_dir())
        
    def test_get_image_info_handles_nonexistent_file(self):
        """Test that get_image_info handles nonexistent files gracefully"""
        result = get_image_info(Path('/nonexistent/file.png'))
        self.assertIn('error', result)

if __name__ == '__main__':
    unittest.main()
