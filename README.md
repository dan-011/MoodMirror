# MoodMirror

[Progress Report Link](https://docs.google.com/document/d/1zcvJ6YbKLEyoJ-yDF_jfcapHDL3DqDEnxSkEmOHma9w/edit?usp=sharing)

[Proposal Link](https://docs.google.com/document/d/1SZxvgO6slOHLQc_zVqJpW-hWD_TaRWTL0fOREhcHuAI/edit?usp=sharing)

## Usage
It may be advantageous to run this locally and not in colab. If so, it's best to do that with a virtual environment because of all the required dependencies. These are the steps I used for easy setup.

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