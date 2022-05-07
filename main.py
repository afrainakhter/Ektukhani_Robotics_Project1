from time import ctime
import time
import webbrowser
import playsound
import pywhatkit
import os
import random
import datetime
from gtts import gTTS
import wikipedia
import speech_recognition as sr


r = sr.Recognizer()




def record_audio(ask=False):
    with sr.Microphone()as source:
        if ask:
             robot_speak(ask)
        audio=r.listen(source)
        voice_data=''
        try: 
           voice_data=r.recognize_google(audio)
           
        except sr.UnknownValueError:
            robot_speak("Sorry,I did not get that!")
        except sr.RequestError:
             robot_speak("Sorry,My speech service down")    
        return voice_data
    
    
    
def robot_speak(audio_string):
    tts=gTTS(text=audio_string,lang='en')
    r=random.randint(1,10000000)
    audio_file='audio-' +str(r)+'.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)






    
def respond(voice_data):
       if 'what is your name' in voice_data:
           robot_speak('My name is Afrain')
       if 'time' in voice_data:
           robot_speak(ctime())
       if 'search'  in voice_data:
           search=record_audio('What do you   search for?')
           url='https://google.com/search?q=' + search
           webbrowser.get().open(url)
           robot_speak('here is what you search for' +search)
       if 'find location'  in voice_data:
           location=record_audio('What do you locate for?')
           url='https://google.nl/maps/place/'+location+ '/&amp;'
           webbrowser.get().open(url)
           robot_speak('here is what you locate for' +location)
       if 'play' in voice_data:
           song=voice_data.replace('play','')
           robot_speak('playing'+song)  
           pywhatkit.playonyt(song) 
       if 'what' in voice_data:
          object =voice_data.replace('what','')
          info=wikipedia.summary(object,5)
          print(info)
          robot_speak(info)  
                
           
       if 'exit' in voice_data:
            exit() 
            
            
time.sleep(1)
currentTime = datetime.datetime.now()   
currentTime.hour
if currentTime.hour < 12 :
     robot_speak('Good morning')
elif 12 <= currentTime.hour < 18:
     robot_speak('Good afternoon')
else :
     robot_speak('Good evening')
robot_speak("How can I help You") 


while 1: 
   voice_data=record_audio()
   respond(voice_data)