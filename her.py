import os
import speech_recognition as sr
import pyttsx3
import pyaudio
import wolframalpha
import datetime as dt
import wikipedia
import webbrowser


#voice engine
engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour = int(dt.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning Vinay")
    elif hour>=12 and hour<=18:
         speak("good afternoon vinay")
    else:
        speak("good evening")     
         
    speak("Hey vinay,it's been so long how may i help you")  
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening..") 
        r.pause_threshold = 1   
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')
        print("Vinay : ",query)
    except Exception as e:
         speak("vinay, i'm not getting anything from you")
         return "None"
    return query

if __name__ == '__main__':
   # while True: 
         wishMe()
         query = takeCommand().lower()

         if 'wikipedia' in query:
             speak('Searching Wikipedia')
             query=query.replace("wikipedia", "")
             r = wikipedia.summary(query, sentences=2)
             speak("According to wikipedia")
             print(r)
             speak(r)
             
         elif 'the time' in query: 
             strTime=dt.datetime.now().strftime("%H:%M")
             speak(f"sir, the time is {strTime}")

         elif 'open youtube' in query: 
             webbrowser.open("youtube.com") 

         elif 'open google' in query: 
             webbrowser.open("google.com") 

         elif 'open udemy' in query: 
             webbrowser.open("udemy.com")

         elif 'open geeks for geeks' in query: 
             webbrowser.open("https://www.geeksforgeeks.org/python-programming-language/")
         elif 'i want to work' in query: 
              ide = "set the path of your vs code "
              os.startfile(ide)
    
