@echo off
cd /d "%~dp0"
if exist .venv\Scripts\python.exe (
    .\.venv\Scripts\python.exe app.py
) else (
    echo Virtual environment not found.
    echo Run: python -m venv .venv
    echo Then install requirements with: .\.venv\Scripts\python.exe -m pip install -r requirements.txt
    pause
)
