@echo off
python -m venv .venv
call .\.venv\Scripts\activate
pip install -r requirements.txt
echo Virtual environment setup complete and activated. To deactivate, run:
echo deactivate
cmd /k @REM keep the command prompt open
