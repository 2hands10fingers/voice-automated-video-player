from gtts import gTTS
import speech_recognition as sr
import os
import re
import webbrowser
import smtplib
import requests
from weather import Weather
from os import listdir, path
from subprocess import call

def talkToMe(audio):
    "speaks audio passed as argument"
    print(audio)
    for line in audio.splitlines():
        os.system("say " + audio)

def myCommand():
    "listens for commands"

    r = sr.Recognizer()

    with sr.Microphone() as source:
        # print('Ready...')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio).lower()
        print('You said: ' + command + '\n')

    #loop back to continue to listen for commands if unrecognizable speech is received
    except sr.UnknownValueError:
        print('Your last command couldn\'t be heard')
        command = myCommand();

    return command

def movie(string):
    moviefolder = '/Volumes/TonoDrive/Movies'

    for i in listdir(moviefolder):
        title = i.split('.')
        
        if string.lower() == title[0].lower():
            vlc = '/Applications/VLC.app/Contents/MacOS/VLC'
            
            call(['open', '-a', vlc, path.join(moviefolder, i)])


def assistant(command):
    "if statements for executing commands"

    if 'play' in command:
        parsed = command[5:]
        movie(parsed)
    else:
        talkToMe('I beg your pardon?')


talkToMe('I am ready for your command')

#loop to continue executing multiple commands
while True:
    assistant(myCommand())  
