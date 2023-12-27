# MoodMirror

MoodMirror is a web application that predicts the user's emotion through images from their webcam. This is comprised of 3 main components:
- A convolutional neural network (CNN) model trained to predict between happy, sad, angry, disgusted, fearful, surprised, and neutral
    > Final model is located under final_model.ipynb
- An API written in Python that supports POSTS of the webcam image and returns the predicted emotion from the CNN
    > API is located under model_api.py
- A React.js front end that provides the user with an interface to take images of their webcam and displays the predicted emotion
    > Front end is located under mood-mirror

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

#### Contributors
[Daniel Paliulis](https://github.com/dan-011)

[Tyler Hinrichs](https://github.com/tylernh10)

[Vihaan Shah](https://github.com/ShahhhVihaan)