import path
import pyautogui
import time
from Speak import speak
from SpeechRecognition import get_command
#from tkinter import *

#x= input("Enter the chatting persino name: ")
#msg=input("Enter your massage to send: ")
def WhatsApp(name,msg):
    # windoes Point(x=575, y=1054)
    # windows search Point(x=810, y=161)
    #window=Tk()
    ''' time.sleep(10)
    x=pyautogui.position()
    print(x) '''
    try:
        Query = Query.replace("please","")
        Query = Query.replace("open","")
        Query = Query.replace("jarvis","")
        Query = Query.replace("the","")
    except:
        pass
    pyautogui.press("super") # click on Windows butten
    time.sleep(1) # hold the program for 1 second
    pyautogui.typewrite("WhatsApp") # write WhatsApp on windows search ber
    time.sleep(1)
    pyautogui.press("enter") # press enter to open the whatsApp
    time.sleep(2)
    x = True
    while x:
        time.sleep(2)
        pyautogui.press("Ctrl+N") #click on search ber using short cut key
        time.sleep(2)
        pyautogui.typewrite(name) # write on search bur to search persion
        time.sleep(2)
        pyautogui.press("enter") # press enter to search
        time.sleep(1)
        pyautogui.press("Tab") # press Tab to select the persion to send message
        time.sleep(1)
        pyautogui.press("Enter")# press enter to open search persion chat
        time.sleep(1)
        #pyautogui.click(586,881)
        pyautogui.typewrite(msg) # write the message to the persion
        time.sleep(2)
        pyautogui.press("enter")
        y = True
        speak("message successfully send sir to " + name)
        while y:
            speak("tell me, any one I send message for you sir ?")
            Query = get_command().lower()
            if "yes" in Query or "no" in Query:
                y=False
        if "yes" in Query:
            speak("Which person shuld i message sir?")
            name = get_command().lower()    
            speak("what shuld i say sir ?")
            msg = get_command()
        elif "no" in Query:
            x = False
            speak("closing whatapps successfully sir.")
            
    pyautogui.click(1906,4) # click on window close butten