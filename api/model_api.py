from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
from pydantic import BaseModel
import base64
import cv2
from keras.models import load_model
import numpy as np
import uvicorn

class Item(BaseModel):
    data: str | None = ""

app = FastAPI()

face_cascade = cv2.CascadeClassifier(os.path.join('dependencies','haarcascade_frontalface_alt2.xml'))
model = load_model(os.path.join('dependencies','advanced_model.h5'))
model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])
emotions = {
    0:'Anger', # correct
    1:'Fear', # correct
    2:'Happiness', # correct
    3:'Neutral', # correct
    4: 'Sadness', # correct
    5:'Surprise', # correct
}

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/send/")
async def send_data(item: Item):
    data = item.data
    b64_str = data[data.index(",") + 1:]
    img_data = b64_str.encode()
    img_bytes = base64.b64decode(img_data)
    byte_buffer = np.fromstring(img_bytes, np.uint8)
    img_arr = cv2.imdecode(byte_buffer, cv2.IMREAD_COLOR)
    img_arr = cv2.cvtColor(img_arr, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(img_arr, scaleFactor=1.1,
            minNeighbors=5,
            minSize=(15, 15),
            flags = cv2.CASCADE_SCALE_IMAGE)
    for (x, y, w, h) in faces:
        dim = max(w, h)
        img_arr = img_arr[y:y+dim, x:x+dim]
        if(img_arr.size == 0): continue
    img_arr = cv2.resize(img_arr, (48, 48), interpolation=cv2.INTER_AREA)
    img_arr = np.reshape(img_arr, (1, 48, 48, 1))
    pred = model.predict(img_arr)[0]
    max_i = 0
    max_val = pred[max_i]
    for i in range(len(pred)):
        if(pred[i] > max_val):
            max_i = i
            max_val = pred[i]
    return emotions[max_i]

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)