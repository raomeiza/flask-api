#!/bin/bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
echo "Virtual environment setup complete and activated. To deactivate, run:"
echo "deactivate"
exec "$SHELL"