import sys
# adding Module to the system path
sys.path.insert(0, 'D:\\code\\ZOYA\\Module')
from time import sleep
import screen_brightness_control as screen
from Speak import speak
from SpeechRecognition import get_command


    # increase part

def brightness_up():
    get = screen.get_brightness()    # return a list
    speak("now the screen brightness is ")
    speak(get)
    speak("how much percent to increase the brightness ? sir ")
    a = get_command()
    a = a.replace("%","")
    a = a.replace("%","")
    a = a.replace("the","")
    a = a.replace("brightness","")
    a = a.replace("by","")
    a = a.replace("level","")
    a = a.replace("decrease","")
    a = a.replace("please","")
    a = a.replace("zoya","")
    a = a.replace("increase","")
    i1 = int (a)
    k=get[0]+i1
    if (k>100):
        speak (" now the brightness is 100 % ")
        screen.set_brightness(k)
    else:
        screen.set_brightness(k)

    # decrease part

def brightness_down():
        get = screen.get_brightness()    # return a list
        speak("now the screen brightness is ")
        speak(get)
        speak("how much percent to decrease the brightness ? sir ")
        a2 = get_command()
        a2 = a2.replace("%","")
        a2 = a2.replace("the","")
        a2 = a2.replace("brightness","")
        a2 = a2.replace("decrease","")
        a2 = a2.replace("please","")
        a2 = a2.replace("level","")
        a2 = a2.replace("by","")
        a2 = a2.replace("zoya","")
        a2 = a2.replace("increase","")
        i = int (a2)
        k=get[0]-i
        if (k<0):
            speak (" now the brightness is 0 % ")
            k=0
            screen.set_brightness(k)
        else:
            screen.set_brightness(k)

def brightness(Query):
    x = True
    while x: 
        if "increase" in Query:
            brightness_up()
            speak(" brightness sucessfully increase sir")
            break
        elif "decrease" in Query:
            brightness_down()
            speak(" brightness sucessfully decrease sirr")
            break
        else:
            speak("Sir please tell me one more time whether to increase or decrease the brightness of the screen ? ")
            sleep(0.4)
            Query = get_command()
