#!/usr/bin/env bash

set -e # exit immediately if error with non-zero return value

# get into repo directory if not run from there
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO_ROOT="$(dirname "$SCRIPT_DIR")"

cd "$REPO_ROOT"

echo "Creating virtual environment..."
python3 -m venv .venv

echo "Upgrading pip..."
.venv/bin/python -m pip install --upgrade pip

echo "Installing requirements..."
if [ ! -f requirements.txt ]; then
   echo
   echo "ERROR: requirements.txt not found!"
   exit 1
fi

.venv/bin/python -m pip install -r requirements.txt

echo
echo "Setup complete"
echo
echo "To activate venv in your terminal instance, run:"
echo "   source .venv/bin/activate"
echo
echo "To run your python script, run:"
echo "   python <your-file-name>.py"