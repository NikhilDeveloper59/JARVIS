'''
--> Speak (Text to Speech)
--> Listen from microphone (Speech to Text)
--> Search Wikipedia
--> Open websites (YouTube/Google/Gmail)
--> Tell time/date
--> Play songs on YouTube
--> Tell jokes
-->Open Apps
-->Exit by voice command
'''
#<----------------importing modules------------------->

import pyttsx3          # Text to Speech engine : convert text to voice
import datetime         # Used for getting current time/date
import wikipedia        # Used to search and fetch results from Wikipedia.
import speech_recognition as sr  # take voice input from microphone and convert it to text.
import webbrowser       # Helps open websites in your default browser.
import os               # Used to run system commands
import pywhatkit        # Used for playing YouTube videos, sending WhatsApp messages etc.
import pyjokes          # Gives random jokes.
import musicFile # my local file


#<---------------Initialize Voice Engine--------------->
    
def speak(text):
    engine = pyttsx3.init()                  # re-init every time and start the voice engine
    voices = engine.getProperty('voices')    # get available voice into the system(male/female)
    engine.setProperty('voice', voices[1].id)# female voice, for male voice use voices[0]
    engine.setProperty('rate', 170)          # it control speed rate of speech(normal speed)
    engine.say(text)                         # used to pass the text to the voice engine
    engine.runAndWait()                      # Executes speaking


#<-----------------Greeting message------------------->
def wishMe():
    current_time = int(datetime.datetime.now().hour)
    if current_time >= 0 and current_time < 12:
        speak("Good Morning Sir")
    elif current_time >= 12 and current_time < 18:
        speak("Good Afternoon Sir")
    else:
        speak("Good Evening Sir")
    speak("I am Jarvis. How can I help you")


def open_app(path, app_name):
    speak(f"Opening {app_name}")
    os.startfile(path)


def commandProcess(query):
        
    if "how r u" in query or "how are you" in query:
        speak("Hii i am fine , How can help you")
        print("Hii i am fine , How can help you")
   
    #   Wikipedia Search
    if "wikipedia" in query:
        speak("Searching Wikipedia...")
        # update query --> remove word wikipedia from query 
        query = query.replace("wikipedia", "")
                
        # get summary aboutt that query in 3 line from wikipedia
        result = wikipedia.summary(query,sentences=3)
        speak("According to wikipedia")
        print(result)
        speak(result)

    # Open Websites
    elif "open youtube" in query or "open the youtube" in query:
        speak("Opening Youtube")
        webbrowser.open("https://youtube.com")

    elif "close youtube" in query or "close the youtube" in query:
        speak("Closing Youtube")
        os.system("taskkill /f /im msedge.exe")   # close Microsoft Edge
        # os.system("taskkill /f /im chrome.exe") when chrome

    elif "open google" in query:
        speak("Opening Google")  
        webbrowser.open("https://google.com")

    elif "close google" in query:
        speak("Closing Google")
        os.system("taskkill /f /im msedge.exe") 
        # os.system("taskkill /f /im chrome.exe")

    elif "open facebook" in query:
        speak("wait opening facebook")
        webbrowser.open("https://www.facebook.com/")  

    elif "open git" in query or "open github" in query:
        speak("wait opening your github account")
        webbrowser.open("https://github.com/NikhilDeveloper59")
    
    elif "open linkedln" in query:
        speak("wait opening your linkedln account")
        webbrowser.open("https://www.linkedin.com/in/nikhil-kumar-ab451018b/")
    
    elif "open instagram" in query:
        speak("wait opening your instagram account")
        webbrowser.open("https://www.instagram.com/its_nikhil_ns/")

    elif "open gmail" in query or "open email" in query:
        speak("Opening Gmail")
        webbrowser.open("https://mail.google.com")

    elif "close gmail" in query or "close email" in query:
        speak("Closing Gmail")
        os.system("taskkill /f /im msedge.exe") 
        # os.system("taskkill /f /im chrome.exe")
      
    
    # Opening Apps
    elif "open desktop" in query:
        open_app(r"C:\\Users\\Nikhil\\Desktop","Desktop")
    
    elif "code" in query:
        open_app("C:\\Users\\Nikhil\\AppData\\Local\\Programs\\Microsoft VS Code\\bin\\code","VS code")
    
    # Time
    elif "time" in query:
        time = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Current time is {time}")
        print(time)

    # Date
    elif "date" in query:
        date = datetime.datetime.now().strftime("%d %B %Y")
        speak(f"Today's date is {date}")
        print(date)
            
    #  Play song
    elif query.startswith("play"):
        pywhatkit.playonyt(query) # search directly from youtube

        # play music which is present in my local file
        # song = list(query.split(" "))[1]  # input like ["play","song_name","song"]
        # link = musicFile.music[song]
        # webbrowser.open(link)

    # jokes
    elif "joke" in query:
        joke = pyjokes.get_joke()
        speak(joke)
        print(joke)

    else:
        speak("Sorry, I don't have that feature yet.")    

# #<---------------------- Main Program --------------------->

if __name__ == "__main__":
    wishMe()
    #<------------------Voice input----------------------->
    while True:
        r = sr.Recognizer()  # Creates a Recognizer object which handles speech recognition.
        print("Recognizing...")

        try:
            # Uses microphone as audio input source.
         with sr.Microphone() as voice_source:

            print("\nListening......🧏‍♀️")
            record_audio = r.listen(voice_source,timeout=5,phrase_time_limit=1)
            word = r.recognize_google(record_audio)

            if word.lower() == "jarvis":
                speak("Yaa")
                with sr.Microphone() as source:
                    print("jarvis now active")
                    # Google speech recognition converts audio into English
                    audio = r.listen(source)
                    query = r.recognize_google(audio, language="en-in")
                    print(f"You said: {query}\n")

                    commandProcess(query.lower())

                    if "exit" in query or "bye" in query:
                     speak("Goodbye Sir. Have a nice day!")
        
        except Exception as e :
            print(f"error:{e}")
       
    

        
