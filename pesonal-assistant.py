# Importing Libraries
import datetime

import pyjokes
import pyttsx3
import pywhatkit
import requests
import speech_recognition as sr
import sys
import wikipedia

listener = sr.Recognizer()

engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty('voice', voices[1].id)


def engine_talk(text):
    engine.say(text)
    engine.runAndWait()


def weather(city):
    api_key = "3ea4fef11d33c52b0ff8f4511cd9a3e3"

    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    city_name = city

    complete_url = base_url + "appid=" + api_key + "&q=" + city_name

    response = requests.get(complete_url)

    x = response.json()

    if x["cod"] != "404":
        y = x["main"]

        current_temperature = y["temp"]

        return str(current_temperature)


def user_commands():
    try:
        with sr.Microphone() as source:
            print("Start Speaking!!")
            engine_talk('hello!iam your personal assistant how may i assist you')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass
    return command


def run_alexa():
    command = user_commands()
    if 'play' in command:
        song = command.replace('play', '')
        # print('New Command is' +command)
        # print('The bot is telling us: Playing' +command)
        engine_talk('Playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        engine_talk('The current time is' + time)
    elif 'who is' in command:
        name = command.replace('who is', '')
        info = wikipedia.summary(name, 2)
        print(info)
        engine_talk(info)
    elif 'joke' in command:
        engine_talk(pyjokes.get_joke())
    elif 'weather' in command:
        weather_api = weather('Hyderabad')
        engine_talk(weather_api + 'degree fahreneit')
    elif 'created by' in command:
        engine_talk('i was created by Maahi')
    elif 'stop' in command:
        sys.exit()
    else:
        engine_talk('I could not hear you properly')


while True:
    run_alexa()
