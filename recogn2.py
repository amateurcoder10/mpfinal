#!/usr/bin/python

# Import the required modules
import cv2, os
import numpy as np
from PIL import Image
import pyttsx

# For face detection we will use the Haar Cascade provided by OpenCV.
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath)

# For face recognition we will the the LBPH Face Recognizer 
recognizer = cv2.face.createLBPHFaceRecognizer()
recognizer.load('model.xml')

path = './thirdeye'
# Append the images with the extension .sad into image_paths
#image_paths = [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.sad')]


predict_image_pil = Image.open("neha.jpeg").convert('L')
predict_image = np.array(predict_image_pil, 'uint8')
faces = faceCascade.detectMultiScale(predict_image)
#print(len(faces))
for (x, y, w, h) in faces:
    print(w,h)
    if((h<200) | (w<200)):
       continue
    nbr_predicted,conf = recognizer.predict(predict_image[y: y + h, x: x + w])
    print "Label is ",nbr_predicted
    if(conf<=23):
        if(nbr_predicted==1):
            nbr_actual="bala"
        elif(nbr_predicted==2):
            nbr_actual="neha"
        elif(nbr_predicted==3):
            nbr_actual="deepika"
        else:
            nbr_actual="prashanthi"
    else:
        nbr_actual="Stranger"

    print(nbr_actual)
    cv2.imshow("Recognizing Face", predict_image[y: y + h, x: x + w])
    cv2.waitKey(1000)
            
engine = pyttsx.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-75)
voices=engine.getProperty('voices')
for voice in voices:
	if(voice.gender=="female"):
		engine.setProperty('voice',voice.id)
		break;
engine.say(nbr_actual)
engine.runAndWait()
engine.say('Found')
engine.runAndWait()   
    
