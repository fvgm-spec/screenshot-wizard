#!/bin/bash
# Setup script for Screenshot Wizard

# Get the directory where this script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

# Make scripts executable
chmod +x "$SCRIPT_DIR/bin/rename-screenshot"
chmod +x "$SCRIPT_DIR/bin/screenshot-manager"
chmod +x "$SCRIPT_DIR/src/rename_screenshot.py"
chmod +x "$SCRIPT_DIR/src/screenshot_manager.py"

# Check if zsh is installed
if command -v zsh &> /dev/null; then
    # Check if .zshrc exists
    if [ -f "$HOME/.zshrc" ]; then
        # Check if PATH already includes the bin directory
        if ! grep -q "PATH=\"$SCRIPT_DIR/bin:\$PATH\"" "$HOME/.zshrc"; then
            echo "Adding Screenshot Wizard to PATH in .zshrc..."
            echo "" >> "$HOME/.zshrc"
            echo "# Screenshot Wizard" >> "$HOME/.zshrc"
            echo "export PATH=\"$SCRIPT_DIR/bin:\$PATH\"" >> "$HOME/.zshrc"
            echo "Screenshot Wizard added to PATH in .zshrc"
            echo "Please run 'source ~/.zshrc' or restart your terminal to apply changes."
        else
            echo "Screenshot Wizard is already in PATH in .zshrc"
        fi
    else
        echo "Warning: .zshrc not found. Creating it..."
        echo "# Screenshot Wizard" > "$HOME/.zshrc"
        echo "export PATH=\"$SCRIPT_DIR/bin:\$PATH\"" >> "$HOME/.zshrc"
        echo ".zshrc created with Screenshot Wizard in PATH"
        echo "Please run 'source ~/.zshrc' or restart your terminal to apply changes."
    fi
else
    echo "zsh not found. Adding to .bashrc instead..."
    # Check if .bashrc exists
    if [ -f "$HOME/.bashrc" ]; then
        # Check if PATH already includes the bin directory
        if ! grep -q "PATH=\"$SCRIPT_DIR/bin:\$PATH\"" "$HOME/.bashrc"; then
            echo "Adding Screenshot Wizard to PATH in .bashrc..."
            echo "" >> "$HOME/.bashrc"
            echo "# Screenshot Wizard" >> "$HOME/.bashrc"
            echo "export PATH=\"$SCRIPT_DIR/bin:\$PATH\"" >> "$HOME/.bashrc"
            echo "Screenshot Wizard added to PATH in .bashrc"
            echo "Please run 'source ~/.bashrc' or restart your terminal to apply changes."
        else
            echo "Screenshot Wizard is already in PATH in .bashrc"
        fi
    else
        echo "Warning: .bashrc not found. Creating it..."
        echo "# Screenshot Wizard" > "$HOME/.bashrc"
        echo "export PATH=\"$SCRIPT_DIR/bin:\$PATH\"" >> "$HOME/.bashrc"
        echo ".bashrc created with Screenshot Wizard in PATH"
        echo "Please run 'source ~/.bashrc' or restart your terminal to apply changes."
    fi
fi

# Check for required Python packages
echo "Checking for required Python packages..."
if ! python3 -c "import PIL" &> /dev/null; then
    echo "PIL (Pillow) not found. Installing..."
    pip install pillow
else
    echo "PIL (Pillow) is already installed."
fi

echo ""
echo "Screenshot Wizard setup complete!"
echo "You can now use the following commands:"
echo "  rename-screenshot - Quickly rename the most recent screenshot"
echo "  screenshot-manager - Advanced screenshot management"
echo ""
echo "For more information, run:"
echo "  rename-screenshot --help"
echo "  screenshot-manager --help"
echo ""
echo "Project repository: https://github.com/fvgm-spec/screenshot-wizard"
