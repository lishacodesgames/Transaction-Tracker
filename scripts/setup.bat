@echo off

REM get into repo directory if not run from there
cd /d "%~dp0\.."

echo Creating virtual environment...
python -m venv .venv

echo Upgrading pip...
.venv\Scripts\python.exe -m pip install --upgrade pip

echo Installing requirements...
if not exist requirements.txt (
   echo.
   echo ERROR: requirements.txt not found!
   exit /b 1
)
.venv\Scripts\python.exe -m pip install -r requirements.txt

REM batch doesn't let you escape characters
set "TAB=   "  

echo.
echo Setup complete
echo.
echo To activate venv in your terminal instance, run:
echo %TAB%.venv\Scripts\activate.bat
echo %TAB%(.bat works in cmd, use .ps1 for Powershell)
echo To run your python script, run:
echo %TAB%python <your-file-name>.py