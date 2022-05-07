from cgitb import reset
from time import ctime
import webbrowser
import speech_recognition as sr

r = sr.Recognizer()
def record_audio(ask=False):
    with sr.Microphone()as source:
        if ask:
            print(ask)
        audio=r.listen(source)
        voice_data=''
        try: 
           voice_data=r.recognize_google(audio)
           
        except sr.UnknownValueError:
            print("Sorry,I did not get that!")
        except sr.RequestError:
            print("Sorry,My speech service down")    
        return voice_data
def respond(voice_data):
       if 'what is your name' in voice_data:
           print('My name is Afrain')
       if 'time' in voice_data:
           print(ctime())
       if 'search'  in voice_data:
           search=record_audio('What do you   search for?')
           url='https://google.com/search?q=' + search
           webbrowser.get().open(url)
           print('here is what you search for' +search)
       if 'find location'  in voice_data:
           location=record_audio('What do you locate for?')
           url='https://google.nl/maps/place/'+location+ '/&amp;'
           webbrowser.get().open(url)
           print('here is what you locate for' +location)
         
    
print("How can I help You")  
voice_data=record_audio()
respond(voice_data)