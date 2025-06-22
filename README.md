# Screenshot Wizard 🧙‍♂️

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.6+](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/)

A magical tool for managing, organizing, and renaming your screenshots with ease.

![Screenshot Wizard Banner](docs/banner.png)

## ✨ Features

- **Quick Rename**: Instantly rename your most recent screenshot with a meaningful name
- **Batch Processing**: Rename multiple screenshots at once with sequential numbering
- **Smart Organization**: Automatically organize screenshots into categories/folders
- **Search Capabilities**: Find screenshots by name across multiple directories
- **Detailed Information**: View metadata like dimensions, size, and creation date
- **Timestamp Integration**: Automatically add timestamps to ensure unique filenames

## 🚀 Installation

### Option 1: Quick Install

```bash
# Clone the repository
git clone https://github.com/fvgm-spec/screenshot-wizard.git

# Run the setup script
cd screenshot-wizard
./setup.sh
```

### Option 2: Manual Installation

```bash
# Clone the repository
git clone https://github.com/fvgm-spec/screenshot-wizard.git

# Make scripts executable
chmod +x screenshot-wizard/bin/*
chmod +x screenshot-wizard/src/*.py

# Add to your PATH (for zsh)
echo 'export PATH="$HOME/screenshot-wizard/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

### Dependencies

- Python 3.6+
- PIL (Python Imaging Library)

## 🧙 Usage

### Basic Usage: rename-screenshot

This tool renames the most recent screenshot from your Screenshots directory and copies it to the Misc directory.

```bash
# Basic usage (renames to "my_screenshot.png")
rename-screenshot my_screenshot

# With location/category (creates a subdirectory)
rename-screenshot aws_console --location=aws

# With custom extension
rename-screenshot meeting_notes --ext=jpg

# With timestamp (renames to "my_screenshot_20250622_123456.png")
rename-screenshot my_screenshot --timestamp
```

### Advanced Usage: screenshot-manager

This tool provides more comprehensive screenshot management capabilities.

#### Renaming Screenshots

```bash
# Rename the most recent screenshot
screenshot-manager rename aws_lambda_function

# With location/category
screenshot-manager rename database_schema --location=database

# With custom extension
screenshot-manager rename ui_mockup --ext=jpg

# With timestamp
screenshot-manager rename aws_lambda_function --timestamp
```

#### Batch Renaming

```bash
# Rename the 3 most recent screenshots with a common prefix
screenshot-manager batch meeting_slides 3

# With location/category
screenshot-manager batch aws_tutorial 5 --location=tutorials

# With timestamps
screenshot-manager batch meeting_slides 3 --timestamp
```

#### Listing Screenshots

```bash
# List all screenshots
screenshot-manager list

# List screenshots from the last 7 days
screenshot-manager list --days=7
```

#### Searching Screenshots

```bash
# Search for screenshots with "aws" in the filename
screenshot-manager search aws
```

#### Viewing Screenshot Information

```bash
# View information about the most recent screenshot
screenshot-manager info --latest

# Interactive mode - choose a screenshot to view details
screenshot-manager info
```

## 📋 Common Workflows

### Workflow 1: Taking screenshots for documentation

```bash
# Take screenshots using your system's screenshot tool
# Then rename them with meaningful names
rename-screenshot login_page --location=auth
rename-screenshot dashboard --location=ui
rename-screenshot error_message --location=errors
```

### Workflow 2: Organizing screenshots from a meeting

```bash
# After taking multiple screenshots during a meeting
screenshot-manager batch meeting_20250622 5 --location=meetings
```

### Workflow 3: Finding screenshots for a project

```bash
# Search for all screenshots related to a project
screenshot-manager search aws
```

## ⚙️ Configuration

By default, Screenshot Wizard uses these directories:

- **Source directory**: `/home/felix/Pictures/Screenshots`
- **Destination directory**: `/home/felix/Pictures/Misc`

To change these directories, edit the constants at the top of the Python scripts:

```python
# In src/rename_screenshot.py and src/screenshot_manager.py
SCREENSHOTS_DIR = Path('/path/to/your/screenshots')
DESTINATION_DIR = Path('/path/to/your/destination')
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Inspired by the need to organize screenshots more efficiently
- Thanks to the Python community for the amazing libraries that make this possible
