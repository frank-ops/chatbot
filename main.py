import speech_recognition as sr
import pywhatkit
import datetime
import wikipedia
import pyjokes
from gtts import gTTS
from playsound import playsound
import os
listener = sr.Recognizer()
# engine = pyttsx3.init('dummy')
if os.path.exists("comm.mp3"):
    os.remove("comm.mp3")
listener = sr.Recognizer()
def talk(command):
    v = gTTS(command)
    v.save("comm.mp3")
    playsound("comm.mp3")
    os.remove("comm.mp3")

def take_command():
    try:
        with sr.Microphone() as source:
            talk("hello im nova how may i help you")
            print('listening...')
            voice = listener.listen(source)
        command = listener.recognize_google(voice)
        command = command.lower()
        if 'nova' in command:
            command = command.replace('nova', '')
            print("--> you : "+command)
    except:
        pass
    return command


def run_alexa():
    try:
        command = take_command()

        if 'play' in command:
            song = command.replace('play', '')
            print("                                                         --> Nova : playing"+song)
            talk('playing ' + song)
            pywhatkit.playonyt(song)
        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            print("                                                         --> Nova : current time is",time)
            talk('Current time is ' + time)
        elif 'who is' in command:
            person = command.replace('who is', '')
            info = wikipedia.summary(person, 1)
            print("                                                        --> Nova : ",info)
            talk(info)
        elif 'date' in command:
            print("                                                        --> Nova : sorry i'm very busy")
            talk('sorry im very busy')
        elif 'are you single' in command:
            print('                                                        --> Nova : sorry im taken by python')
            talk('sorry im taken by python')
        elif 'joke' in command:
            joke = pyjokes.get_joke()
            print("                                                        --> Nova : "+joke)
            talk(joke)
        else:
            talk('Please say the command again.')
    except:
        talk("sorry invalid command")
run_alexa()
