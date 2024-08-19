import pywhatkit
import wikipedia
from pywikihow import RandomHowTo, search_wikihow
import os
from os import startfile
import speech_recognition as sr
import webbrowser as web
import bs4
import pyttsx3
from time import sleep
import requests

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)

def Speak(audio):
    print(" ")
    print(f": {audio}")
    engine.say(audio)
    engine.runAndWait()
    print(" ")

def TakeCommand():

    r = sr.Recognizer()

    with sr.Microphone() as source:

        print(": Listening....")

        r.pause_threshold = 1

        audio = r.listen(source)

    try:

        print(": Recognizing...")

        query = r.recognize_google(audio,language='en-in')

        print(f": Your Command : {query}\n")

    except:
        return ""

    return query.lower()

def GoogleSearch(term):
    query = term.replace("jarvis","")
    query = query.replace("what is","")
    query = query.replace("google search", "")
    query = query.replace("how to","")
    query = query.replace("what is","")
    query = query.replace(" ","")
    query = query.replace("what do you mean by","")

    writeab = str(query)

    oooooo = open('D:\\How To Make Jarvis\\Data.txt','a')
    oooooo.write(writeab)
    oooooo.close()

    Query = str(term)

    pywhatkit.search(Query)

    # os.startfile('D:\\How To Make Jarvis\\DataBase\\ExtraPro\\start.py')

    if 'how to' in Query:

        max_result = 1

        how_to_func = search_wikihow(query=Query,max_results=max_result)

        assert len(how_to_func) == 1

        how_to_func[0].print()

        Speak(how_to_func[0].summary)

    else:

        search = wikipedia.summary(Query,2)

        Speak(f"According To Your Search : {search}")

def News():

    web.open("https://indianexpress.com/todays-paper/")

def YouTubeSearch(term):
    result = "https://www.youtube.com/results?search_query=" + term
    web.open(result)
    Speak("This is what I found for your search ")
    pywhatkit.playonyt(term)
    Speak("This May Also Help You Sir .")

def Alarm(query):

    TimeHere=  open('D:\\How To Make Jarvis\\Data.txt','a')
    TimeHere.write(query)
    TimeHere.close()
    os.startfile("D:\\How To Make Jarvis\\DataBase\\ExtraPro\\Alarm.py")

def Spotify():

    Speak("Here you go with spotify")
    startfile("C:\\Users\\koush\\AppData\\Local\Microsoft\\WindowsApps\\Spotify.exe")

def SpeedTest():

    os.startfile("D:\\How To Make Jarvis\\DataBase\\Gui Programs\\SpeedTestGui.py")

def DateConverter(Query):

    Date = Query.replace(" and ","-")
    Date = Date.replace(" and ","-")
    Date = Date.replace("and","-")
    Date = Date.replace("and","-")
    Date = Date.replace(" ","")

    return str(Date)

def My_Location():

    op = "https://www.google.com/maps/@22.5759109,88.372492,15z"

    Speak("Checking....")

    web.open(op)

    ip_add = requests.get('https://api.ipify.org').text

    url = 'https://get.geojs.io/v1/ip/geo/' + ip_add + '.json'

    geo_q = requests.get(url)

    geo_d = geo_q.json()

    state = geo_d['city']

    country = geo_d['country']

    Speak(f"Sir , You Are Now In {state , country} .")

def Weather():

    web.open('https://www.google.com/search?q=weather+today&rlz=1C1RXQR_enIN982IN982&sxsrf=APq-WBtJPhxYYBP3egQarNE6JvzXbB9mmg%3A1649076032133&ei=QOdKYs3RB_iOseMP9uaykA0&oq=wether&gs_lcp=Cgdnd3Mtd2l6EAEYADIHCAAQRxCwAzIHCAAQRxCwAzIHCAAQRxCwAzIHCAAQRxCwAzIHCAAQRxCwAzIHCAAQRxCwAzIKCAAQRxCwAxDJAzIICAAQkgMQsAMyCAgAEJIDELADMgcIABBHELADSgQIQRgASgQIRhgAUABYAGDxCGgBcAF4AIABAIgBAJIBAJgBAMgBCsABAQ&sclient=gws-wiz')

def CoronaVirus(Country):

    countries = str(Country).replace(" ","")

    url = f"https://www.worldometers.info/coronavirus/country/{countries}/"

    result = requests.get(url)

    soups = bs4.BeautifulSoup(result.text,'lxml')

    corona = soups.find_all('div',class_ = 'maincounter-number')

    Data = []

    for case in corona:

        span = case.find('span')

        Data.append(span.string)

    cases , Death , recovored = Data

    Speak(f"Cases : {cases}")
    Speak(f"Deaths : {Death}")
    Speak(f"Recovered : {recovored}")
    
