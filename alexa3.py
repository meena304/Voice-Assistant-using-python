
from os import name
from pyttsx3 import speak
import speech_recognition as sr
import pyttsx3
import webbrowser
import pywhatkit
import datetime
import os 
from PyDictionary import PyDictionary as d


r = sr.Recognizer()

def speakText(command):
    engine = pyttsx3.init()
    engine.setProperty('rate',100)
    engine.say(command)
    engine.runAndWait() 
    

def TakeCommand():
    try:
        with sr.Microphone() as source2:
            # wait for the recognizer to adjust the energy threshold
            r.adjust_for_ambient_noise(source2,duration=0.3)

            #listen to the user
            print('I am Alexa..How can i help you....')
            audio2 = r.listen(source2)

            mytext = r.recognize_google(audio2)
            # mytext = r.recognize_sphinx(audio2)
            mytext = mytext.lower()

            print("Did you say "+ mytext)
            # speakText(mytext)
         

    except sr.RequestError as e:
        print("Could Not request Result; {0}".format(e))

    except Exception:                #For Error handling
        speak("error...")
        print("Network connection error")
        return "none"
    return mytext


# speakText("Hello, Hello Meena.. How are you")
# TakeCommand()
chrome_path="C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"

def Task():
    def music():
        speak('Tell me the name of the song..')
        MusicName = TakeCommand()
        if 'my song' in  MusicName:
            os.startfile('we.mp3')
        elif 'new song' in MusicName:
            os.startfile('badshah.mp3')
        else:
            pywhatkit.playonyt(MusicName)
            speak('you song has been started.. enjoy')
    
    def openapps():
        speak("Ok Ma'am! Wait a second...")
        # if 'open vs code' in query:
        #     os.startfile("C:\Users\hp\AppData\Local\Programs\Microsoft VS Code\code.exe")
        if 'open sublime' in query:
            os.startfile("C:\Program Files\Sublime Text 3\sublime_text.exe")
        elif 'open power point' in query:
            os.startfile("C:\Program Files\Microsoft Office\root\Office16\powerpoint.exe")
        speak("Your command has been completed sir!!")
    def closeapps():
        speak("Ok Sir! Wait a second...")
        if 'close vs code' in query:
            os.startfile()
        # elif 'close' in query:
            # os.startfile("TASKKILL /F /im chrome.exe")
        elif 'close sublime' in query:
            os.system("taskkill /f /im sublime_text.exe")
        speak("Your command has been completed sir!!")

    def Whatsapp():
        speak("Tell me the Name of the persona!")
        name = TakeCommand() 

        if 'meena' in name:
            speak("tell me the message!")
            msg =TakeCommand()
            speak("tell Me The Time sir!")
            speak("Time in Hours!")
            hour =int(TakeCommand())
            speak("Time In Minutes!")
            min = int(TakeCommand())
            pywhatkit.sendwhatmsg("+917000846823",msg,hour,min,20)  
            speak("ok sir,Sending whatsqpp Message")
            
        else:
            speak("Tell Me the Phone Number!")
            phone =int(TakeCommand())
            ph ='+91' + phone
            speak("tell me the message!")
            msg =TakeCommand()
            speak("tell Me The Time sir!")
            speak("Time in Hours!")
            hour =int(TakeCommand())
            speak("Time In Minutes!")
            min = int(TakeCommand())
            pywhatkit.sendwhatmsg(ph,msg,hour,min,20)  
            speak("ok sir,Sending whatsqpp Message")

    def wishMe():
        hour = int(datetime.datetime.now().hour)
        if hour>=0 and hour<12:
            speak("Good Morning!")
        elif hour>=12 and hour<18:
            speak("Good Afternoon!")
        else:
            speak("Good Evening!")

    def Dict():
        speak("Activated dictionary!")
        speak("Tell Me The Problem!")
        prob1 = TakeCommand()

        if 'meaning' in prob1:
            prob1 = prob1.replace("what is the","")
            prob1 = prob1.replace("jarvis","")     
            prob1 = prob1.replace("of","") 
            prob1 = prob1.replace("meaning of","")
            result =d.meaning(prob1)
            speak(f"The Meaning for {prob1} is {result}")   
        elif 'synonym' in prob1:
            prob1 = prob1.replace("what is the","")
            prob1 = prob1.replace("jarvis","")     
            prob1 = prob1.replace("of","") 
            prob1 = prob1.replace("synonym of","")
            result =d.synonym(prob1)
            speak(f"The synonym for {prob1} is {result}")
        elif 'antonym' in prob1:
            prob1 = prob1.replace("what is the","")
            prob1 = prob1.replace("jarvis","")     
            prob1 = prob1.replace("of","") 
            prob1 = prob1.replace("antonym of","")
            result =d.antonym(prob1)
            speak(f"The synonym for {prob1} is {result}")
            speak("Exited Dictionary!")

    wishMe()
    while True:
        query = TakeCommand()

        if 'hello alexa' in query:
            speak("Hello Meena, I am alexa")
            speak('Your personal AI assistent')
            speak('How may I help you')
        elif 'how are you' in query:
            speak("I am fine.")
        elif 'number system' in query:
            speak("first, Sum of first n natural number is n(n + 1) divide by 2")
            speak('second, Sum of square of first n natural number is  n ( n + 1 ) (2n + 1) divide by 6')
            speak('third, Sum of cube of first n natural number is  (n(n + 1) divide by 2) whole square')
            speak('forth, Sum of first n odd numbers is n square')
            speak('fifth, Sum of first n even numbers is n(n + 1)')
        elif 'about python' in query:
            speak("Python was created by Guido van Rossum, and first released on February 20, 1991. ")
        elif "open python" in query:
            speak("Opening")
            # webbrowser.get(url).open()
            webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path))
            webbrowser.get('chrome').open_new_tab('http://www.python.org')
        elif "open youtube" in query:
            speak("Opening youtube")
            webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path))
            webbrowser.get('chrome').open_new_tab('https://www.youtube.com/')
        elif "search on youtube" in query:
            query = query.replace('search on youtube', " ")
            web = "https://www.youtube.com/results?search_query="+query
            webbrowser.open(web)
            speak("Done Sir, Mill gya sir")
        elif "google search" in query:
            query = query.replace('google search', " ")
            pywhatkit.search(query)
            speak("done sir")
        elif 'open website' in query:
            speak('Tell me the name of the website..')
            name = TakeCommand()
            web ='https://www.' + name + '.com'
            webbrowser.open(web)
            speak("Done ma'am")
        elif 'facebook' in query:
            speak("Ok Ma'am")
            webbrowser.open('https://www.facebook.com/')
            speak("Done Ma'am")
        elif 'music' in query:
            music()
        elif 'close all tab' in query:
            os.system('taskkill /F /IM chrome.exe')
        elif 'shutdown' in query:
            pywhatkit.shutdown(time=1)
        elif 'open vs code' in query:
            openapps()
        elif 'open' in query:
            openapps()
        elif 'close' in query:
            closeapps()
        elif 'send message' in query:
            Whatsapp()
        elif 'dictionary' in query:
            Dict()
        
        


Task()
