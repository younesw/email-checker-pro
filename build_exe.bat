@echo off
echo Installing dependencies...
pip install -r requirements.txt

echo.
echo Building executable...
pyinstaller --onefile --windowed --name EmailCheckerPro --icon=icon.ico main.py

echo.
echo Build completed!
echo Executable location: dist/EmailCheckerPro.exe
pause
