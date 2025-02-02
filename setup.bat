@echo off
echo Setting up the project...

REM Check if Python is installed
python --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo Python is not installed. Please install Python from https://www.python.org/downloads/ and add it to your PATH.
    exit /b 1
)

REM Check if pip is installed
pip --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo pip is not installed. Please ensure pip is installed correctly.
    exit /b 1
)

REM Create requirements.txt file
echo arabic-reshaper > requirements.txt
echo python-bidi >> requirements.txt
echo pandas >> requirements.txt
echo openpyxl >> requirements.txt
echo emoji >> requirements.txt
echo joblib >> requirements.txt

REM Install required libraries
echo Installing required libraries...
pip install -r requirements.txt

REM Run the project
echo Running the project...
python main.py

echo Setup complete.
pause