import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
listener =sr.Recognizer()
engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
def talk(text):
    engine.say(text)
    engine.runAndWait()
engine.runAndWait()
def take_command():  
    try:
        with sr.Microphone() as source:
         print('listening...')
         voice=listener.listen(source)
         command=listener.recognize_google(voice)
         command=command.lower()
         if 'alexa' in command:
             command=command.replace('alexa','')
             print(command)
    except:
        pass
    return command
def run_alexa():
    command=take_command()
    print(command)
    if 'play' in command:
        song=command.replace('play','')
        talk('playing'+song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
         time=datetime.datetime.now().strftime('%I:%M %p')
         print(time)
         talk('Current time is'+time)
    elif 'what is' in command:
         person=command.replace('what is','')
         info=wikipedia.summary(person,1)
         print(info)
         talk(info)
    elif 'date' in command:
        talk('sorry,i have an headache')
    elif 'single' in command:
                 talk('sorry,iam married')
    elif 'features' in command:
           talk('I can make ur work easier, enhance ur travelling experiene by being ur partner in crime .I can entertain u,search for u,crack some jokes,remind ur works and most importantly be ur saviour when ur in trouble')

    elif 'joke' in command:
        print(pyjokes.get_joke())
        talk(pyjokes.get_joke())
    
run_alexa()
