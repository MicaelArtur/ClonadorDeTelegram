@echo off
cd /d "%~dp0"
call venv\Scripts\activate
python clonador.py
pause
