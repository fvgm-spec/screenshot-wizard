# Screenshot Wizard Usage Guide

This document provides detailed usage instructions for Screenshot Wizard.

## Command Reference

### rename-screenshot

```
rename-screenshot <new_name> [--location=<location>] [--ext=<extension>]
```

#### Arguments:

- `new_name`: New name for the screenshot (without extension)
- `--location`: Optional location/category for organizing screenshots
- `--ext`: Optional file extension (default: png)

#### Examples:

```bash
# Basic usage
rename-screenshot aws_lambda_console

# With a category/location
rename-screenshot database_diagram --location=database

# With a different file extension
rename-screenshot meeting_notes --ext=jpg
```

### screenshot-manager

```
screenshot-manager <command> [options]
```

#### Commands:

1. **rename**: Rename the most recent screenshot
   ```
   screenshot-manager rename <new_name> [--location=<location>] [--ext=<extension>]
   ```

2. **batch**: Batch rename multiple screenshots
   ```
   screenshot-manager batch <prefix> <count> [--location=<location>] [--ext=<extension>]
   ```

3. **list**: List screenshots
   ```
   screenshot-manager list [--days=<days>]
   ```

4. **search**: Search for screenshots by name
   ```
   screenshot-manager search <keyword>
   ```

5. **info**: Display information about screenshots
   ```
   screenshot-manager info [--latest] [--days=<days>]
   ```

## Directory Structure

By default, Screenshot Wizard uses these directories:

- **Source directory**: `/home/felix/Pictures/Screenshots`
- **Destination directory**: `/home/felix/Pictures/Misc`

When you use the `--location` option, it creates a subdirectory under the destination directory.

## File Naming

When renaming screenshots, Screenshot Wizard uses this naming pattern:

```
<new_name>_<timestamp>.<extension>
```

For example:
```
aws_lambda_function_20250622_123456.png
```

The timestamp ensures that filenames are unique, even if you use the same name multiple times.

## Batch Renaming

When batch renaming screenshots, Screenshot Wizard adds sequential numbers to the filenames:

```
<prefix>_01_<timestamp>.<extension>
<prefix>_02_<timestamp>.<extension>
<prefix>_03_<timestamp>.<extension>
...
```

For example:
```
meeting_slides_01_20250622_123456.png
meeting_slides_02_20250622_123457.png
meeting_slides_03_20250622_123458.png
```

## Tips and Tricks

1. **Use descriptive names**: Choose names that will help you find the screenshots later.

2. **Use the location option**: Organize screenshots into categories for easier browsing.

3. **Search regularly**: Use the search command to find screenshots when you need them.

4. **List recent screenshots**: Use `screenshot-manager list --days=7` to see screenshots from the last week.

5. **Check screenshot info**: Use `screenshot-manager info --latest` to see details about your most recent screenshot.
