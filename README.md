# MoodMirror

[Progress Report Link](https://docs.google.com/document/d/1zcvJ6YbKLEyoJ-yDF_jfcapHDL3DqDEnxSkEmOHma9w/edit?usp=sharing)

[Proposal Link](https://docs.google.com/document/d/1SZxvgO6slOHLQc_zVqJpW-hWD_TaRWTL0fOREhcHuAI/edit?usp=sharing)

## Usage
For windows, launch the "launch-for-windows.ps1" powershell script. The application should open in a web browser. Be sure to allow webcam access, then press "Predict Emotion" to predict the emotion of the person on the webcam.

#### Install virtualenv
```powershell
py -m pip install virtualenv
```

#### Installing virtual environment
Install virtual environment in venv folder in directory.
```powershell
virtualenv venv
```

#### Activating venv
```powershell
.\venv\Scripts\activate.ps1
```

#### Installing dependencies
```
py -m pip install -r requirements.in
```

#### Deactivating venv
```powershell
deactivate
```