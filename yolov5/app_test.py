import cv2
import time
import numpy as np
import matplotlib.pyplot as plt
import numpy as np
import urllib.request
# Import Yolo Modules
import argparse
import os
import sys
from pathlib import Path
import torch

# Importing Flask modules
from flask import Flask, Response

app = Flask(__name__)

# Loading the model
model = torch.hub.load('.', 'yolov5s', source='local', skip_validation=True)
model.classes = [0]

stream = urllib.request.urlopen("http://192.168.0.125:5000")

def gen_video_frames():
    total_bytes = b''
    while True:
        total_bytes += stream.read(1024)
        b = total_bytes.find(b'\xff\xd9') # JPEG end
        if not b == -1:
            a = total_bytes.find(b'\xff\xd8') # JPEG start
            jpg = total_bytes[a:b+2] # actual image
            total_bytes= total_bytes[b+2:] # other informations
            
            # decode to colored image ( another option is cv2.IMREAD_GRAYSCALE )
            img = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8), cv2.IMREAD_COLOR)
            #img=cv2.imencode('.jpg', img)
            print(type(img))
            try:
                results = model(img)
                results.render()
                _, frame = cv2.imencode('.jpg', results.imgs[0])
            except Exception as e:
                print(e)
                _, frame = cv2.imencode('.jpg', img)
            yield (b'--frame\r\nContent-Type: imageviewer/jpeg\r\n\r\n' + frame.tobytes() + b'\r\n')
            # cv2.imshow('Window name',cv2.flip(img, -1)) # display image while receiving data
            # if cv2.waitKey(1) ==27: # if user hit esc            
            #     break
# cv2.destroyWindow('Window name')

@app.route("/yolofeed")
def yolo_mjpeg():
    return Response(gen_video_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')



