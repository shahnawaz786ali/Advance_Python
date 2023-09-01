import pyttsx3
import time
import datetime as dt
import speech_recognition as sr

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def wishme():
    hour=dt.datetime.now().hour
    if hour >=0 and hour < 12:
        speak("Good morning!")
        
    elif hour >= 12 and hour < 16:
        speak("Good afternoon!")
        
    else:
        speak("Good evening!")
        
    speak("How may I help you Sir!")
    
def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold=1
        audio=r.listen(source)
        
    try:
        print("Recognizing...")
        query=r.recognize_google(audio)
        
    except Exception as e:
        print("Say that again please..")
        return "None"
    return query
    

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
if __name__=="__main__":
    wishme()
    takecommand()
