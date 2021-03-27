import Speak as aas
import datetime

def firstWelcome():
    user = open('user.txt','w')
    aas.speak("Hi, I am your virtual assistant. Whats your name?")
    owner_Name = aas.takeCommand()
    user.write(owner_Name + '\n')
    aas.speak("Should I call you Sir or Madam?")

    while 1:
        sign = aas.takeCommand()
        sign = sign.lower()
        if 'sir' in sign:
            user.write('Sir\n')
            signature = 'Sir'
            break
        if 'madam' in sign:
            user.write('Madam\n')
            signature = 'Madam'
            break
        aas.speak('Please choose between Sir or Madam...')
    
    aas.speak('What do you want to call me?')
    assistant_Name = aas.takeCommand()
    user.write(assistant_Name + '\n')
    aas.speak(f"{assistant_Name}, That's a great name!!!")
    aas.speak(f"At your service {signature}!!!")
    user.close()


def wishMe():
    user = open('user.txt', 'r')
    userlines = user.readlines()
    owner_Name = userlines[0]
    signature = userlines[1]
    assistant_Name = userlines[2]
    user.close()
    hour = (datetime.datetime.now().hour)
    if hour>=6 and hour<12:
        aas.speak(f"Good Morning {signature}...")
        # print("Good Morning Ninad...")
    
    elif hour>=12 and hour<16:
        aas.speak(f"Good Afternoon {signature}...")
        # print("Good Afternoon Ninad...")

    else:
        aas.speak(f"Good Evening {signature}...")
        # print("Good Evening Ninad...")
    
    aas.speak(f"I am {assistant_Name}, How can I help you?")