.PHONY: test test-visible clean

VENV_PYTHON = venv/bin/python

# Default target - runs tests in headless mode
all: test

# Runs the test suite in headless mode (default)
test: venv
	@echo "▶️ Running tests in headless mode..."
	$(VENV_PYTHON) test_app.py

# Runs the test suite with visible browser (for debugging)
test-visible: venv
	@echo "▶️ Running tests with visible browser..."
	HEADLESS=false $(VENV_PYTHON) test_app.py

# Sets up the virtual environment and installs dependencies
venv:
	@echo "🐍 Creating virtual environment..."
	python3 -m venv venv
	@echo "📦 Installing dependencies..."
	venv/bin/pip install -q playwright
	@echo "🌐 Installing browser binaries..."
	venv/bin/playwright install --with-deps > /dev/null 2>&1

# Removes the virtual environment and other temporary files
clean:
	@echo "🧹 Cleaning up..."
	rm -rf venv
