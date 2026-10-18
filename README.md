# Phishing Site Lab

This project is a simple, authorized educational demo for a phishing-site lab exercise. It runs locally and captures dummy credentials entered into a fake login form. It is intended only for classroom demonstration and must be used with dummy accounts in a controlled lab environment.

## Features
- Realistic fake login page
- Credential capture on submit
- Terminal output for demonstration
- CSV/text log file for evidence
- Simple local setup using Flask

## Requirements
- Python 3.10+
- A local network between the server laptop and a victim laptop or emulator

## Setup
1. Open a terminal in this folder.
2. Create a virtual environment:
   ```bash
   python -m venv .venv
   ```
3. Activate it:
   - Windows PowerShell:
     ```powershell
     .\.venv\Scripts\Activate.ps1
     ```
   - Command Prompt:
     ```bat
     .\.venv\Scripts\activate.bat
     ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Start the server in either of these ways:
   ```bash
   python app.py
   ```
   or simply:
   ```bat
   start_demo.bat
   ```
6. Note the server IP address shown in the terminal, for example:
   ```text
   http://192.168.1.10:5000/
   ```
   The app is configured to listen on all interfaces, so a second laptop can open the server machine's local IP in the browser.

## Classroom Use
- Server laptop: run the app and leave it open.
- Victim laptop: open the IP address in a browser.
- Enter dummy credentials such as `student123` and `Password123!`.
- The server terminal will print the captured values.
- The values are also written to `captured_credentials.txt`.

## Important Safety Notes
- Never use real credentials.
- Never send the link outside the lab environment.
- Use only for authorized classroom demonstration.
- Do not host this publicly or share it online.

## Files
- `app.py` — Flask web application
- `templates/login.html` — fake login page
- `templates/thank_you.html` — redirect/confirmation page
- `static/styles.css` — styling for the fake page
- `captured_credentials.txt` — captured demo credentials
