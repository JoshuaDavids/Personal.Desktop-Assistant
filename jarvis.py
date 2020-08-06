import datetime
import os
import smtplib
import webbrowser

import pyttsx3
import speech_recognition as sr
import wikipedia

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_EN-GB_GEORGE_11.0')


# Speaks the string that will be passed
def speak(text):
    engine.say(text)
    engine.runAndWait()


print("Initializing Karen...")


def greetMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        print("Good Morning!")
        speak("Good Morning!")
    elif 12 < hour < 18:
        print("Good Afternoon!")
        speak("Good Afternoon!")
    else:
        print("Good Evening!")
        speak("Good Evening!")

    print("I am Karen. Please let me know how I may serve you...")
    speak("I am Karen. Please let me know how I may serve you...")


def takeCommand():
    # takes microphone input from user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("I am listening...")
        speak("I am listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

        try:
            print("Recognizing...")
            query1 = r.recognize_google(audio, language='en')
            print(f"You said: {query1}\n")
        except Exception as E:
            print(E)
            print("Say that again please...")

            return "None"
        return query1


def sendEmail(toward, context):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("joshuadavids.jds@gmail.com", "Joker2505")
    server.sendmail("joshuadavids.jcd@gmail.com", toward, context)
    server.close()


if __name__ == '__main__':
    greetMe()
    while True:
        query = takeCommand().lower()

        # logic for executing tasks based on theory
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            print("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'play music' in query:
            music_dir = 'C:\\Users\\Joshua Davids\\Music'  # fix this
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is: {strTime}")
        elif 'open code' in query:
            codePath = "C:\\Users\\Joshua Davids\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif 'email' in query:
            try:
                speak("Sir, what would you like to say?")
                content = takeCommand()
                to = "joshuadavids.jcd@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry sir, im unable to send the email")
        else:
            speak("I will tell your operating system")
