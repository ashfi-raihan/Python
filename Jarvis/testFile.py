'''
#basic talk
greetings()
talk("My name is Zoro.")
'''
'''
# tell a joke
joke = pyjokes.get_joke()
print(joke)
talk(joke)
'''
'''
# play song
song = "Bella Ciao"
talk('playing' + song)
pywhatkit.playonyt(song)
'''
'''
#telling time
time = datetime.datetime.now().strftime("%I:%M:%S %p")
print(time)
talk("Current time is " + time)
'''
'''
# opening 
command = "chrome"
talk("opening" + command)
pyautogui.press("super") #start button is also called super
pyautogui.typewrite(command)
pyautogui.sleep(1)
pyautogui.press('enter')
'''
'''
#closing 
talk("Closing program")
pyautogui.hotkey('alt','f4')
'''
'''
#to search any person
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
'''

'''
# remember a massage
command = "remember that I hava an exam tomorrow."
commandMessage = command.replace("remember that", " ")
rememberMessage = commandMessage.replace("I", "You")
print(rememberMessage)
talk("you told me to remember that " + rememberMessage)
remember = open("remember.txt","a")
remember.write(rememberMessage)
remember.close()
'''

'''
# telling a remembered massage
remember = open("remember.txt", 'r')
talk("you told me to remember that " + remember.read())
print(remember) 
'''

'''
# clearing everything
file=open("remember.txt", 'w')
file.write(f"")
talk("done sir. cleared everything.")
'''

'''
# Searching anything in internet
command = "search Coffee"
searchItem = command.replace('search', "")
searchItem = searchItem.lower()
webbrowser.open(f"{searchItem}")
talk("this is what I found ")


'''