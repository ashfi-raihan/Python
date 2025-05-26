import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate',200)

def talk(text):
    engine.say(text)
    engine.runAndWait()



talk("Hello kiddo. I am Zoro, the A I bot. I know you are a beautiful singer, I hope oneday I will hear it.")
talk("I wold like to taste your shingara as well. I also heard about your hair. I heard many things about you. Do let me know if you want to hear about the horror incident that heppened near your varsity.")
talk("Good bye TISHA. See you soon.")

