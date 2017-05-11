import speech_recognition as sr
from time import ctime
import time
import os
import pygame
#import pyttsx
from gtts import gTTS
import sys

import warnings
warnings.filterwarnings('ignore')
old=sys.stdout
f=open(os.devnull,'w')
sys.stderr=f


def speak(audioString):
    print(audioString)

    tts = gTTS(text=audioString, lang='en')
    tts.save("output.mp3")
    pygame.mixer.init()
    pygame.mixer.music.load("output.mp3")
    pygame.mixer.music.play()
    
    while pygame.mixer.music.get_busy() == True:
        continue

	    
def recordAudio():
#    sys.stdout=old
    # Record Audio
    r = sr.Recognizer()
   
    with sr.Microphone(sample_rate = 16000,chunk_size = 1024) as source:
        r.adjust_for_ambient_noise(source)
        print("Say something!")
        
        audio = r.record(source,duration=10)
    #with open("mic.wav","wb") as f:
     #   f.write(audio.get_wav_data())
        
    # Speech recognition using Google Speech Recognition
    data = ""
    try:
        # Uses the default API key
        # To use another API key: `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        data = r.recognize_google(audio)
        print("You said: " + data)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
 
    return data
'''
def listen():
	with sr.Microphone() as source:
                print("Say something!")
		r.adjust_for_ambient_noise(source)
		audio = r.listen(source)

	try:
		return r.recognize_sphinx(audio)
		# or: return recognizer.recognize_google(audio)
	except speech_recognition.UnknownValueError:
		print("Could not understand audio")
	except speech_recognition.RequestError as e:
		print("Recog Error; {0}".format(e))

	return " "
'''

def jarvis(data):

    if ("how are you" in data):
        speak("I am fine")
        
    if ("what time is it" in data) or ("time" in data):
        speak(ctime())
 
    if "where is" in data:
        data = data.split(" ")
        location = data[2]
        speak("Hold on, I will show you where " + location + " is.")
        os.system("chromium-browser https://www.google.nl/maps/place/" + location + "/&amp;")

    if ("take a picture" in data) or ("picture" in data):
        speak("Point  your camera")
        os.system("fswebcam -r 160x120 --no-banner image.jpeg")#("fswebcam -r 160x120 --no-banner image.jpeg")

    if ("colour" in data) or ("color" in data) or ("what is my dress colour" in data):
        speak("Point  your camera")
        os.system("fswebcam -r 160x120 --no-banner image.jpeg")
        speak("Give me a second.. will tell u the color")
        os.system("python color.py image.jpeg")
    
    if ("pattern" in data) or ("patan" in data)or("Patan" in data)  or ("pattern of dress" in data) or ("titan" in data) or ("cartoon" in data) or ("what is my dress pattern" in data):
        speak("Point  your camera")
        os.system("fswebcam -r 160x120 --no-banner image.jpeg")
        speak("Give me a second.. will tell u the pattern")
        os.system("python classifier.py -i image.jpeg")

    if ("card" in data) or ("visiting card" in data) or ("business card" in data) or ("Read me the card" in data):
        speak("Point  your camera")
        os.system("fswebcam -r 1020x720 --no-banner image.jpg")#"fswebcam -r 1020x720 --no-banner image.jpeg")
        speak("Give me a second.. will read out the card for you")
        os.system("python extract.py card1.jpg ")

    if("who is it" in data) or ("friend" in data) or ("Who is this" in data) or ("face" in data) :
        speak("Point  your camera")
        os.system("fswebcam -r 1020x720 --no-banner face.jpg")
        speak("Give me a second..I will tell you if it is a friend")
        os.system("python recogn2.py")

    if("how many" in data) or ("people" in data) or ("number of people" in data) or ("tell me the count" in data):
        speak("Point  your camera")
        os.system("fswebcam -r 1020x720 --no-banner people.jpeg")
        speak("Give me a second..I will tell you the number of people")
        os.system("python facemul.py")

    

    elif "sleep" in data:
        speak("Bye Bye..!")
        #os.system("exit(0)")

# initialization
time.sleep(2)
speak("Hello, This is 'Third Eye'. What can I do for you?")
#engine.runAndWait()
while 1:
    data = recordAudio()
    jarvis(data)
