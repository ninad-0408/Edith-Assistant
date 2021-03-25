
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import smtplib


# Resources Start
chromepath = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
codepath = 'C:/Users/91942/AppData/Local/Programs/Microsoft VS Code/Code.exe'
spotifypath = 'C:/Users/91942/AppData/Roaming/Spotify/Spotify.exe'

email_dictonary_name = ['pankaj', 'niketan', 'jay']
email_dictonary_email = ['pksmks1999@gmail.com', 'niketanmangulley@gmail.com', 'jayraikhere@gmail.com']
# Resources End

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = (datetime.datetime.now().hour)
    if hour>=6 and hour<12:
        speak("Good Morning Ninad...")
        print("Good Morning Ninad...")
    
    elif hour>=12 and hour<16:
        speak("Good Afternoon Ninad...")
        print("Good Afternoon Ninad...")

    elif hour>=16 and hour<=23:
        speak("Good Evening Ninad...")
        print("Good Evening Ninad...")
    
    else:
        speak("Good Night Ninad...")
        print("Good Night Ninad...")
    
    speak("I am Edith, How can I help you?")


def takeCommand():
    # It take microphone input and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.8
        audio = r.listen(source)
        
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User Said: {query}\n")

    except Exception as e:
        # print(e)
        speak("Say that again please...")
        return 'none'

    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)


wishMe()
while True:
    query = takeCommand().lower()
    # logic for executing queries
    if 'wikipedia' in query:
        speak("Searching wikipedia...")
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("According to wikipedia...")
        speak(results)
    
    elif 'open youtube' in query:
        webbrowser.get(chromepath).open("youtube.com")
    
    elif 'open google' in query:
        webbrowser.get(chromepath).open("google.com")

    elif 'play music' in query or 'play song' in query:
        music_dir = 'D:/Music'
        songs = os.listdir(music_dir)
        os.startfile(os.path.join(music_dir, songs[random.randint(0,len(songs))]))
    
    elif 'time' in query:
        nowTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Sir, Time is {nowTime}")
    
    elif 'code' in query:
        os.startfile(codepath)

    elif 'spotify' in query:
        os.startfile(spotifypath)
    
    elif 'email to' in query:
        found = False
        for i in range(0, len(email_dictonary_name)):
            if email_dictonary_name[i] in query:
                to = email_dictonary_email[i]
                found = True
                break

        if found == False:
            speak("The person is not in dictonary...")
        else:
            try:
                speak("What is the content of mail?")
                content = takeCommand()
                sendEmail(to, content)
                speak(f"Email has been sent to {to}.")
            except:
                speak("Currently I am facing some issues with sending email. Please try again later...!")    
    elif query != 'none':
        speak("Sorry command not found..., Please try again...") 
