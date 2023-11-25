cd api
Start-Process powershell.exe -ArgumentList "-NoExit", "-Command", "python3 model_api.py"
cd ..\mood-mirror
Start-Process powershell.exe -ArgumentList '-noexit', '-command', 'npm start'
cd ..