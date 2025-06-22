.PHONY: install test clean docs

# Default target
all: install

# Install the package
install:
	@echo "Installing Screenshot Wizard..."
	@./setup.sh

# Run tests
test:
	@echo "Running tests..."
	@python -m unittest discover -s tests

# Generate documentation
docs:
	@echo "Generating documentation..."
	@cd docs && python generate_banner.py

# Clean up temporary files
clean:
	@echo "Cleaning up..."
	@find . -name "__pycache__" -type d -exec rm -rf {} +
	@find . -name "*.pyc" -delete
	@find . -name "*.pyo" -delete
	@find . -name "*.pyd" -delete
	@find . -name ".pytest_cache" -type d -exec rm -rf {} +
	@find . -name ".coverage" -delete
	@find . -name "htmlcov" -type d -exec rm -rf {} +
	@find . -name "*.egg-info" -type d -exec rm -rf {} +
	@find . -name "dist" -type d -exec rm -rf {} +
	@find . -name "build" -type d -exec rm -rf {} +

# Help target
help:
	@echo "Screenshot Wizard Makefile"
	@echo ""
	@echo "Available targets:"
	@echo "  install  - Install Screenshot Wizard"
	@echo "  test     - Run tests"
	@echo "  docs     - Generate documentation"
	@echo "  clean    - Clean up temporary files"
	@echo "  help     - Show this help message"
