
@echo off
echo Building HyCAN Windows binary...

python -m venv venv
call venv\Scripts\activate
pip install --upgrade pip
pip install -r requirements.txt pyinstaller

pyinstaller --onefile hycan_cli.py --name HyCAN
rename dist\HyCAN.exe HyCAN-Setup.exe
