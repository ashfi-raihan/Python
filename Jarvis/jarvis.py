import pyttsx3
import speech_recognition as sr
import datetime
import pyjokes
import pywhatkit
import pyautogui
import wikipedia
import os
import webbrowser

listener= sr.Recognizer()

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate',200)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            print(command)
            return command
    except sr.UnknownValueError:
        print("Sorry, I did not understand that.")
        return ""
    except sr.RequestError:
        print("Error with the speech recognition service.")
        return ""
    except:
        return ""

def greetings():
    current_time = datetime.datetime.now()
    hour = current_time.hour
    if 3 <= hour < 12:
        talk("Good Morning!")
    elif 12 <= hour < 18:
        talk("Good Afternoon!")
    else:
        talk("Good Evening!")


def run_zoro():
    command = take_command()
    if "hello" in command or "YO" in command:
        talk("Hi boss, How are you")
    
    elif "That's all for now" in command:
        talk("okay boss. Goodbye.")  
    
    elif 'time' in command:
        time = datetime.datetime.now().strftime("%I:%M %P")
        print(time)
        talk(time)
    
    elif 'jokes' in command:
        talk(pyjokes.get_joke())
    
    elif 'play' in command:
        song = command.replace('play', "")
        talk('playing' + song)
        pywhatkit.playonyt(song)

    elif "stop" in command or "start" in command:
        pyautogui.press('k') 

    elif "full screen" in command:
        pyautogui.press('f')
      
    elif "turn off full screen" in command:
        pyautogui.press('esc')

    
    elif "theatre" in command:
        pyautogui.press('t')

    # to open any page
    elif "open" in command:
        command = command.replace("open", "")
        talk("opening" + command)
        pyautogui.press("super") #start button is also called super
        pyautogui.typewrite(command)
        pyautogui.sleep(1)
        pyautogui.press('enter')
    
    #to close any page
    elif 'close' in command:
        talk("Closing program")
        pyautogui.hotkey('alt','f4')

    # to search any person in wikipedia 
    elif 'who is ' in command:
        person = 'Ashfi'
        try:
            info = wikipedia.summary(person, sentences=1, auto_suggest=False)
            # we need only 1 paragraph about the person
            print(info)
            talk(info)
        except wikipedia.exceptions.PageError:
            search_results = wikipedia.search(person)
            print(search_results)
            talk("Do you mean " )
            talk(search_results)    

    # to search anything in internet
    elif "search" in command:
        searchItem = command.replace('search', "")
        searchItem = searchItem.lower()
        webbrowser.open(f"{searchItem}")
        talk("this is what I found ")
        

    elif "remember that " in command:
        commandMessage = command.replace("remember that", " ")
        rememberMessage = commandMessage.replace("I", "You")
        print(rememberMessage)
        talk("you told me to remember that " + rememberMessage)
        remember = open("remember.txt","a")
        remember.write(rememberMessage)
        remember.close()

    elif "what do you remember" in command:
        remember = open("remember.txt", 'r')
        talk("you told me to remember that " + remember.read())
        print(remember)

    elif "forget everything" in command:
        file=open("remember.txt", 'w')
        file.write(f"")
        talk("done sir. cleared everything.")
    
    elif "shutdown" in command:
        talk("shutting down the pc")
        talk("3. 2. 1")
        os.system("shutdown /s /t 1")
    
    elif "restart" in command:
        talk("restarting the pc")
        talk("3. 2. 1")
        os.system("restart /r /t 1")

    else:
        talk("No command detacted.")


while True:
   run_zoro()