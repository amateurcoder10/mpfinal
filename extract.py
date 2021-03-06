#OCR Tesseract program that works on pre-processed images.

from PIL import Image
import sys
import pytesseract
import pygame
from gtts import gTTS
import os

#audio output
def speak(audioString):
    print(audioString)
    tts = gTTS(text=audioString, lang='en')
    tts.save("output.mp3")
    os.system("mpg321 output.mp3 -quiet")
    
#out=[]    

#extract text
if len(sys.argv) != 2:
    print ("%s input_file output_file" % (sys.argv[0]))
    sys.exit()
else:
    text=pytesseract.image_to_string(Image.open(sys.argv[1]))
    '''   for ch in text:
        if ch in "abcdefghijklmnopqrstuvwxyz" or "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or "1234567890" or '@':
            out.append(ch)
    '''     
    #print (text)
    #print (out)
    speak(text)
