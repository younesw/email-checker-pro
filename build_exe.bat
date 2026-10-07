# Build script for Windows exe packaging
@echo off
pip install -r requirements.txt
pyinstaller --onefile --noconsole --name EmailCheckerPro main.py
pause
