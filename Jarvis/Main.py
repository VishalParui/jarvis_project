import pyjokes as pyjokes
import pyttsx3
import datetime
import speech_recognition as sr
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)


def Speak(audio):
    print(audio)
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        Speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        Speak("Good Afternoon!")

    else:
        Speak("Good Evening!")
    Speak("I am your voice assistant. How can I help you?")


def TakeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:

        print("Listening....")

        r.pause_threshold = 1

        audio = r.listen(source)

    try:

        print("Recognizing...")

        query = r.recognize_google(audio, language='en-in')

        print("Your Command : {query}\n")

    except:
        return ""

    return query.lower()


def TaskExe():
    while True:

        query = TakeCommand()

        if 'google search' in query or 'search google' in query or 'search' in query:

            from Features import GoogleSearch
            GoogleSearch(query)

        elif 'youtube search' in query or 'search youtube' in query:

            Query = query.replace("jarvis", "")
            query = Query.replace("youtube search", "")

            from Features import YouTubeSearch
            YouTubeSearch(query)

        elif 'set alarm' in query:

            from Features import Alarm
            Alarm(query)

        elif 'speed test' in query:
            from Features import SpeedTest
            SpeedTest()

        elif 'where is my location' in query or 'show my location' in query:

            from Features import My_Location
            My_Location()

        elif 'where is' in query:

            from Automations import GoogleMaps
            Place = query.replace("where is ", "")
            Place = Place.replace("jarvis", "")
            GoogleMaps(Place)

        elif 'write a note' in query or 'take a note' in query:

            from Automations import Notepad
            Notepad()

        elif 'dismiss' in query:

            from Automations import CloseNotepad
            CloseNotepad()

        elif 'show time table' in query:

            from Automations import TimeTable
            TimeTable()

        elif 'what is the time' in query or 'the time is what' in query:

            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            Speak(f"Sir, the time is {current_time}")

        elif "weather" in query:

            from Features import Weather
            Weather()

        elif 'corona cases' in query:

            from Features import CoronaVirus
            Speak("Which Country's Information ?")
            cccc = TakeCommand()
            CoronaVirus(cccc)

        elif 'joke' in query:

            Speak(pyjokes.get_joke())

        elif 'open chrome' in query:

            from Automations import Chrome
            command = TakeCommand()
            Chrome(command)

        elif 'open facebook' in query:

            from Automations import Facebook
            Facebook()

        elif 'open instagram' in query:

            from Automations import Instagram
            Instagram()

        elif 'open whatsapp' in query:

            from Automations import WhatsApp
            WhatsApp()

        elif 'open youtube' in query:

            from Automations import Youtube
            Youtube()

        elif 'open amazon prime' in query:

            from Automations import AmazonPrime
            AmazonPrime()

        elif 'open spotify' in query:

            from Features import Spotify
            Spotify()

        elif 'today news' in query or 'tell me news' in query:

            from Features import News
            News()

        else:

            from DataBase.ChatBot.ChatBot import ChatterBot

            reply = ChatterBot(query)

            Speak(reply)

            if 'bye' in query:

                break

            elif 'exit' in query:

                break

            elif 'go' in query:

                break


wishMe()
TaskExe()
