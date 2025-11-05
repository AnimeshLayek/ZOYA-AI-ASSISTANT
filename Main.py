import path # here i import all function path 
import pyttsx3
import speech_recognition as sr
import sys
from datetime import datetime
import time
import whatAppss
from vosk import Model,KaldiRecognizer
import pyaudio
import warnings
#from googletrans import Translator
import webbrowser as wb
import wikipedia
import pyautogui
import os
from Screen_Brightness_2 import brightness
from SpeechRecognition import get_command
from Speak import speak
from flipkart import Flipkart
from Google import google_search
import calculator as col
y = 0
warnings.simplefilter('ignore')
 
def voice_translate(voice_text):
    translator = Translator()
    out = translator.translate(voice_text,dest="en")
    speech_text = out.text
    return speech_text

  

def MainExecution(z,query):
    Query = str(query).lower()
    
    if "what is your" in Query:
        speak(" My name is ZoYA  ")
        speak("i am a personal voice assistant , made by tiny coders by using python")

    elif "good morning" in Query:
        speak("good morning sir , what can i help you ? ")

    elif ("hello" in Query or "hii" in Query or "hey" in Query) :
        if z == 0:
            speak("Hello Sir, Welcome Back!")

        else:
            if "hello" in Query:
                speak(" hello sir ")

            elif "hii" in Query:
                speak(" hii sir ")
        

    elif "byy" in Query:
        speak("Nice to meet you sir, Have a nice day!")
    
    elif "calculate" in Query :
        col.cal(Query)
  
    elif "time" in Query:    
        time = datetime.now().strftime("%H:%M:%S")
        speak(f"The Time Now Is : {time}")

    elif "love you" in Query:
        speak(f" Love you two Sir ")

    # play music
    elif "play" in Query and "music" in Query:
        
        try:
            music_Dir = "D:\\code\\ZOYA\\Music"
            songs = os.listdir(music_Dir)
            print(songs)
            os.system(os.startfile(os.path.join(music_Dir, songs[1])))
            
        except:
          pass      

    # brightness controle
    elif "brightness" in Query:
        brightness(Query)

    # wish you
    elif "byy" in Query:
        speak("Nice to meet you sir, Have a nice day!")

    # send message on whatapps
    elif "message" in Query:
        speak("who should I message sir?")
        name = get_command()
        speak("What should I say in the message, sir?")
        msg = get_command()
        whatAppss.WhatsApp(name,msg)

    # search from wikipedia
    elif "wikipedia" in Query and "search" in Query:
        try:
            speak("Searching Wikipedia........")
            Query = Query.replace("wikipedia","")
            results = wikipedia.summary(Query, sentences=2)
            speak("According to wikipedia")
            speak(results)
        except:
            speak(" Sorry sir, I do not find any result ")

    # open yuoutube
    elif "youtube" in Query and "open" in Query:
        speak("opening youtube .................")
        wb.open("https://youtube.com/")

    # open flipkart
    elif "flipkart" in Query and "open" in Query:
        speak(" opening flipkart sir.")
        Flipkart()

    # search from google 
    elif ("search" in Query or "open google" in Query) or "google" in Query :
        speak(" opening google sir.")
        google_search() 
    
    # open any application
    elif "open" in Query:
        Query = Query.replace("please","")
        Query = Query.replace("open","")
        Query = Query.replace("jarvis","")
        Query = Query.replace("zoya","")
        Query = Query.replace("joya","")
        Query = Query.replace("the","")
        Query = Query.replace("soya","")
        pyautogui.press("super")
        pyautogui.sleep(2)
        pyautogui.typewrite(Query)
        pyautogui.sleep(2)
        pyautogui.press("enter")
        pyautogui.sleep(3)
        # camera open and take photo
        if "camera" in Query:
            speak(" should I take a picture ?")
            
            while "close" not in Query:
                Query = get_command()
                if (("take" in Query or "click" in Query) and ("photo" in Query or "picture" in Query or "selfie" in Query)) or "yes" in Query:
                    pyautogui.sleep(2)
                    pyautogui.press("enter")
                elif "close" in Query or "no" in Query:
                    speak(" ok sir .")
                    pyautogui.click(1906,4)
    # stop main program
    elif "good bye" in Query:
        speak("goodbye sir, have a nice day.")
        exit()
    # close window
    elif "close" in Query or "close window" in Query :
        speak(" ok sir .")
        pyautogui.click(1906,4)
z = 0
x = True    
while x:
    
    user_input = get_command()  # str(input("enter youre Query:"))
    if user_input  == "":
        pass
    elif "stop" in user_input:
        speak("are you sure sir ?")
        sure = get_command()
        if "yes" in sure:
            speak(" ok sir, good by sir. ")
            x = False
        else:
            speak("i am still here sir .")
    elif "zoya" in user_input :
        user_input = user_input.replace("zoya","")
        MainExecution(z,user_input)
        z = z+1  