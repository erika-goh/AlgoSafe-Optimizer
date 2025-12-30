VENV = venv

PYTHON = $(VENV)/bin/python
PIP = $(VENV)/bin/pip

.PHONY: all
all: run

$(VENV)/bin/activate: 
	python3 -m venv $(VENV)
	@echo "Virtual environment created."

.PHONY: install
install: $(VENV)/bin/activate
	$(PIP) install numpy
	@echo "Dependencies installed."

.PHONY: upgrade-pip
upgrade-pip: $(VENV)/bin/activate
	$(PIP) install --upgrade pip

.PHONY: run
run: install
	$(PYTHON) algosafe-optimizer.py

.PHONY: clean
clean:
	rm -rf $(VENV)
	rm -rf __pycache__
	rm -rf *.pyc
	@echo "Cleaned up virtual environment and cache."

.PHONY: rebuild
rebuild: clean all

.PHONY: help
help:
	@echo "Available commands:"
	@echo "  make           - Install dependencies and run the script"
	@echo "  make install   - Create venv and install numpy"
	@echo "  make run       - Run the script (auto-installs if needed)"
	@echo "  make clean     - Remove virtual environment and cache"
	@echo "  make rebuild   - Clean and run fresh"
	@echo "  make help      - Show this help message"
