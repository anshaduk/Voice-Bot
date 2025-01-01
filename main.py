import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as speech:
            print('Listening...')
            voice = listener.listen(speech,timeout=50,phrase_time_limit=60)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa','')
                print(command)
    except Exception as e:
        # print("Error: ", e)
        command=''
    return command

def run_alexa():
    command = take_command()
    if not command:
        return
    print(command)
    if 'play' in command:
        song = command.replace('play','')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who' in command:
        person = command.replace('who','')
        info = wikipedia.summary(person,1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry, I have a headache')
    elif 'are you single' in command:
        talk('I am in a relationship')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'stop' in command:
        talk('Goodbye!')
        return False
    else:
        talk('Please say the command again.')
    return True

while(True):
    if not run_alexa():
        break





