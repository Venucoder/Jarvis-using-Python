from email import message
import subprocess
import pyttsx3
from datetime import datetime
import speech_recognition as sr
from random import choice
from utils import opening_text # user defined module 
# import pyaudio
from decouple import config
from pprint import pprint
from Functions.os_func import *
from Functions.online_func import *


USERNAME = config("USERNAME")
BOTNAME = config("BOTNAME")

engine = pyttsx3.init('sapi5')

# Set Rate
engine.setProperty('rate', 200)

# Set Volume
engine.setProperty('volume', 1.0)

# Set Voice (Male)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


# Text to speech
def speak(text):
    """Used to speak whatever text is passed to it"""

    engine.say(text)
    engine.runAndWait()


# Greet the user
def greet_user():
    """Greets the user according to the time"""

    hour = datetime.now().hour
    if hour >= 6 and hour < 12:
        speak(f'Good Morning {USERNAME}')
    elif hour >= 12 and hour < 16:
        speak(f'Good Afternoon {USERNAME}')
    elif hour >= 16 and hour < 19:
        speak(f'Good Evening {USERNAME}')
    speak(f'I am {BOTNAME}, how may I assist you?')


# Takes input from the user
def take_user_input():
    """Takes user input, recognizes it using Speech Recognition module and converts it into text"""

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening....')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        if not ('exit' in query or 'terminate' in query):
            speak(choice(opening_text))
        else:
            hour = datetime.now().hour
            if hour >= 21 and hour < 6:
                speak('Good night sir, take care!')
            else:
                speak('Have a good day sir!')
            exit()
    except Exception:
        speak('Sorry, I could not understand. Could you please say it again?')
        query = 'None'
    return query


# main function
if __name__ == '__main__':

    greet_user()
    
    while True:
        query = take_user_input().lower()
        
        # OS
        if 'open cmd' in query or 'open command prompt' in query:
            open_cmd()

        elif 'open calculator' in query:
            open_calc()

        elif 'open camera' in query:
            open_camera()

        elif 'open chrome' in query or 'open browser' in query:
            open_chrome()

        elif 'open notepad' in query:
            open_notepad()

        elif 'paint' in query:
            open_paint()
        
        elif 'open settings' in query:
            open_settings()

        elif 'open vs code' in query or 'open visual studio code' in query:
            open_vscode()

        # Online
        elif 'ip address' in query:
            ip_address = find_my_ip()
            speak(f"Your IP address is {ip_address}.\n For your convenience I am printing it on the screen sir")
            print(f'Your IP address is {ip_address}')

        elif 'wikipedia' in query:
            speak('What do you want to search in wikipedia, sir?')
            search_query = take_user_input().lower()
            results = search_on_wikipedia(search_query)
            speak(f"According to wikipedia, {results}")
            speak("For your convenience, I am printing it on the screen sir")
            pprint(results)

        elif 'youtube' in query:
            speak("What do you want to play on youtube, sir?")
            video = take_user_input().lower()
            play_on_youtube(video)

        elif 'search on google' in query or 'search' in query:
            speak("What do you want to search on Google, sir?")
            query = take_user_input().lower()
            search_on_google(query)
        
        elif 'send message' in query or "whatsapp" in query:
            speak('On what number should I send the message sir? Please enter in the console: ')
            number = input("Enter the number: ")
            speak("What is the message sir?")
            message = take_user_input().lower()
            send_whatsapp_message(number, message)
            speak("I've sent the message sir")

        elif 'send an email' in query:
            speak("On what email address do I send sir? Please enter in the console: ")
            receiver_address = input("Enter email address: ")
            speak("What should be the subject sir?")
            subject = take_user_input().capitalize()
            speak('What is the message sir?')
            message = take_user_input().capitalize()
            if(send_email(receiver_address, subject, message)):
                speak("I've sent the email sir.")
            else:
                speak("Something went wrong while I sending the email, Please check the error logs sir")
            
        elif 'joke' in query:
            speak(f"Hope you like this one sir.")
            joke = get_randon_joke()
            speak(joke)
            speak("For your convenience, I am printing it on the screen sir.")
            pprint(joke)

        elif 'advice' in query:
            speak(f"Here's an advice for you sir?")
            advice = get_random_advice()
            speak(advice)
            speak("For your convenience, I am printing it on the screen sir.")
            pprint(advice)

        elif 'news' in query:
            speak(f"I'm reading out the latest news headlines, sir")
            speak(get_latest_news())
            speak("For your convenience, I am printing it on the screen sir.")
            print(*get_latest_news(), sep='\n')

        elif 'trending movies' in query:
            speak(f"Some of the trending movies are: {get_trending_movies()}")
            speak("For your convenience, I am printing it on the screen sir.")
            print(*get_trending_movies())

        elif 'weather' in query:
            ip_address = find_my_ip()
            city = requests.get(f"https://ipapi.co/{ip_address}/city/").text
            speak(f"Getting weather report for your city {city}")
            weather, temperature, feels_like = get_weather_report(city)
            speak(f"The current temperature is {temperature}, but it feels like {feels_like}")
            speak(f"Also, the weather report talks about {weather}")
            speak("For your convenience, I am printing it on the screen sir.")
            print(f"Description: {weather}\nTemperature: {temperature}\nFeels like: {feels_like}")
        