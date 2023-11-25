.\venv\Scripts\activate.ps1
cd api
Start-Process powershell.exe -ArgumentList "-NoExit", "-Command", "py model_api.py"
cd ..\mood-mirror
Start-Process powershell.exe -ArgumentList '-noexit', '-command', 'npm start'
cd ..