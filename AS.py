import webbrowser
import pyttsx3
import datetime
import wikipedia as wik
import speech_recognition as sr
import webbrowser
import os
import smtplib

master = "Rishabh"

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)

rate = engine.getProperty("rate")
engine.setProperty("rate", 180)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    date = int(datetime.datetime.now().day)
    month = int(datetime.datetime.now().month)
    speak(f"Hello{master}")
    if date == 10 and month == 6:
        speak(f"Happy Birthday{master}")

    if hour >= 0 and hour <= 12:
        speak("Good Morning!" + master)
    elif hour >= 12 and hour <= 18:
        speak("Good Afternoon!" + master)
    else:
        speak("Good Evening!" + master)

    speak(
        f"This is your audio assistant {master} at your service.Tell me how may i help you."
    )
    list = [
        "send email",
        "Search on wikipedia",
        "open youtube",
        "open google",
        "open vs code",
        "play Music",
        "open coding ninjas",
        "open geeksforgeeks",
    ]
    speak(list)


def send_email(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("0105cd211044@oriental.ac.in", "rishabh@10")
    server.sendmail("0105cd211044.oriental.ac.in", to, content)
    server.close()


def take_commands():
    r = sr.Recognizer()
    r.energy_threshold = 3000
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-US")
        if query == "hello":
            speak("hello")

        print(f"User said: {query}\n")

    except Exception as e:
        speak("Sorry, I didn't get that. Please try again.")
        return "None"

    return query


if __name__ == "__main__":
    wishme()
    if 1:
        query = take_commands().lower()

        if "wikipedia" in query:
            speak("tell me what to search?")
            print("What to search?")
            topic = take_commands()

            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wik.summary(topic, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif "open youtube" or "from youtube" in query:
            webbrowser.open("youtube.com")
        elif "open google" in query:
            webbrowser.open("google.com")
        elif "open coding ninjas" in query:
            webbrowser.open("https://www.codingninjas.com/")
        elif "open gfg" in query:
            webbrowser.open("geeksforgeeks.com")

        elif "play music" in query:
            music_dir = "D:\\Music"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif "the time" in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strtime)
            speak(f"here is the time {strtime}")

        elif "open vs code" in query:
            codepath = "C:\\Program Files\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)

        elif "send email" in query:
            try:
                speak("What should i say?")
                content = take_commands()
                speak("Please Provide the Email")
                to = input("Email address Please?\n")
                send_email(to, content)
                speak("Email has been sent")
            except Exception as e:
                speak("Sorry,I am unable to send the email Please try again")
