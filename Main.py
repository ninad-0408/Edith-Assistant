import os
import datetime
import webbrowser
import random
import wikipedia
import Speak as aas
import Resource as ar
import Greeting as ag


if not os.path.isfile('user.txt'):
    ag.firstWelcome()
else:
    ag.wishMe()
while True:
    user = open('user.txt', 'r')
    userlines = user.readlines()
    owner_Name = userlines[0]
    signature = userlines[1]
    assistant_Name = userlines[2]
    user.close()
    query = aas.takeCommand().lower()
    query = query.replace(assistant_Name.lower(),'')

    if 'wikipedia' in query:
        aas.speak("Searching wikipedia...")
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        aas.speak("According to wikipedia...")
        aas.speak(results)

    elif 'search' in query and 'on google' in query:
        aas.speak("Opening Google")
        query = query.replace('search', '')
        query = query.replace('google', '')
        query = query.replace('on', '')
        webbrowser.get(ar.chromepath).open(f"https://www.google.com/search?q={query}")

    elif 'search' in query and 'on youtube' in query:
        aas.speak("Opening Youtube")
        query = query.replace('search', '')
        query = query.replace('youtube', '')
        query = query.replace('on', '')
        webbrowser.get(ar.chromepath).open(f"https://www.youtube.com/results?search_query={query}")
    
    elif 'open youtube' in query:
        aas.speak("Opening Youtube")
        webbrowser.get(ar.chromepath).open("youtube.com")
    
    elif 'open google' in query:
        aas.speak("Opening Youtube")
        webbrowser.get(ar.chromepath).open("google.com")

    elif 'play music' in query or 'play song' in query:
        music_dir = 'D:/Music'
        songs = os.listdir(music_dir)
        os.startfile(os.path.join(music_dir, songs[random.randint(0,len(songs))]))
    
    elif 'time' in query:
        nowTime = datetime.datetime.now().strftime("%H:%M:%S")
        aas.speak(f"Sir, Time is {nowTime}")
    
    elif 'code' in query:
        os.startfile(ar.codepath)

    elif 'spotify' in query:
        os.startfile(ar.spotifypath)
    
    elif 'email to' in query:
        found = False
        for i in range(0, len(ar.email_dictonary_name)):
            if ar.email_dictonary_name[i] in query:
                to = ar.email_dictonary_email[i]
                found = True
                break

        if found == False:
            aas.speak("The person is not in directory...")
        else:
            try:
                aas.speak("What is the content of mail?")
                content = aas.takeCommand()
                aas.speak(f"Email has been sent to {to}.")
            except:
                aas.speak("Currently I am facing some issues with sending email. Please try again later...!")

    elif query != 'none':
        aas.speak("Sorry command not found..., Please try again...") 
