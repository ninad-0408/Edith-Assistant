import os
import datetime
import webbrowser
import random
import wikipedia
import Edith_speak as es
import Edith_resource as er

def wishMe():
    hour = (datetime.datetime.now().hour)
    if hour>=6 and hour<12:
        es.speak("Good Morning Ninad...")
        # print("Good Morning Ninad...")
    
    elif hour>=12 and hour<16:
        es.speak("Good Afternoon Ninad...")
        # print("Good Afternoon Ninad...")

    elif hour>=16 and hour<=23:
        es.speak("Good Evening Ninad...")
        # print("Good Evening Ninad...")
    
    else:
        es.speak("Good Night Ninad...")
        # print("Good Night Ninad...")
    
    es.speak("I am Edith, How can I help you?")


wishMe()
while True:
    query = es.takeCommand().lower()

    if 'wikipedia' in query:
        es.speak("Searching wikipedia...")
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        es.speak("According to wikipedia...")
        es.speak(results)
    
    elif 'open youtube' in query:
        webbrowser.get(er.chromepath).open("youtube.com")
    
    elif 'open google' in query:
        webbrowser.get(er.chromepath).open("google.com")

    elif 'play music' in query or 'play song' in query:
        music_dir = 'D:/Music'
        songs = os.listdir(music_dir)
        os.startfile(os.path.join(music_dir, songs[random.randint(0,len(songs))]))
    
    elif 'time' in query:
        nowTime = datetime.datetime.now().strftime("%H:%M:%S")
        es.speak(f"Sir, Time is {nowTime}")
    
    elif 'code' in query:
        os.startfile(er.codepath)

    elif 'spotify' in query:
        os.startfile(er.spotifypath)
    
    elif 'email to' in query:
        found = False
        for i in range(0, len(er.email_dictonary_name)):
            if er.email_dictonary_name[i] in query:
                to = er.email_dictonary_email[i]
                found = True
                break

        if found == False:
            es.speak("The person is not in dictonary...")
        else:
            try:
                es.speak("What is the content of mail?")
                content = es.takeCommand()
                es.speak(f"Email has been sent to {to}.")
            except:
                es.speak("Currently I am facing some issues with sending email. Please try again later...!")
                    
    elif query != 'none':
        es.speak("Sorry command not found..., Please try again...") 
