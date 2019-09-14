import os
import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import random
import wikipedia

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")  
        return "None"
    return query

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
        speak("Good Morning")
    elif hour>= 12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")

    speak(" I am Jarvis! How may I help you?")
    

if __name__ == "__main__":
    wishMe()
    if 1:
        query=takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query)
            try:
                while True:
                    speak("According to Wikipedia:")
                    speak(results)
                    break
            except KeyboardInterrupt:
                pass
        elif 'open youtube' in query:
            webbrowser.open("www.youtube.com")
        elif 'open google' in query:
            webbrowser.open("www.google.com")
        elif 'open facebook' in query:
            webbrowser.open("www.facebook.com")
        elif 'play music' in query:
            music_dir = 'D:\\ytd'
            songs=os.listdir(music_dir)
            song_no =random.randint(1,len(songs))
            os.startfile(os.path.join(music_dir, songs[song_no]))
        elif 'time' in query:
            timestr=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir,the time is {timestr}")
        elif 'open whatsapp' in query:
            w_path="C:\\Users\\Naman\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
            os.startfile(w_path)
        elif 'games' in query:
            os.startfile("D:\\Games")
