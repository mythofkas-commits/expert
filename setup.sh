#!/bin/bash

# Exit immediately if a command exits with a non-zero status.
set -e

# Create virtual environment
echo "Creating virtual environment 'venv'..."
python3 -m venv venv

# Install dependencies
echo "Installing dependencies from requirements.txt..."
venv/bin/pip install -r requirements.txt

echo "Setup complete. To activate the virtual environment, run: source venv/bin/activate"
