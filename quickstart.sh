#!/bin/bash
# Quickstart script for Screenshot Wizard

echo "Screenshot Wizard Quickstart"
echo "==========================="
echo ""
echo "This script will help you get started with Screenshot Wizard."
echo ""

# Check if the setup script has been run
if ! command -v rename-screenshot &> /dev/null; then
    echo "It looks like Screenshot Wizard is not in your PATH."
    echo "Running setup script..."
    ./setup.sh
    echo ""
    echo "Please restart your terminal or run 'source ~/.zshrc' to apply changes."
    echo "Then run this quickstart script again."
    exit 0
fi

echo "Great! Screenshot Wizard is installed and in your PATH."
echo ""
echo "Let's take a quick tour of the features:"
echo ""
echo "1. Basic screenshot renaming"
echo "   Command: rename-screenshot my_first_screenshot"
echo "   This will rename your most recent screenshot to 'my_first_screenshot_TIMESTAMP.png'"
echo ""
echo "2. Advanced screenshot management"
echo "   Command: screenshot-manager list"
echo "   This will list all your screenshots"
echo ""
echo "3. Searching for screenshots"
echo "   Command: screenshot-manager search keyword"
echo "   This will find screenshots with 'keyword' in the filename"
echo ""
echo "4. Viewing screenshot information"
echo "   Command: screenshot-manager info --latest"
echo "   This will show information about your most recent screenshot"
echo ""
echo "5. Batch renaming screenshots"
echo "   Command: screenshot-manager batch meeting 3"
echo "   This will rename your 3 most recent screenshots with the prefix 'meeting'"
echo ""
echo "For more information, see the documentation:"
echo "  - README.md: Overview of the project"
echo "  - docs/USAGE.md: Detailed usage instructions"
echo ""
echo "Project repository: https://github.com/fvgm-spec/screenshot-wizard"
echo ""
echo "Happy screenshot managing!"
