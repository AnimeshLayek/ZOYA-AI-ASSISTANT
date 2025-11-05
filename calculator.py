# Import necessary packages
from SpeechRecognition import get_command
from Speak import speak
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import warnings
from selenium.webdriver.chrome.service import Service
import pyautogui

def cal (b):
    try:
        #a = (input ("enter two number :"))
        a=b
        # replace the value
        a=a.replace("calculate","")
        a=a.replace("into" or "x","*")
        a=a.replace("subtract","-")
        a=a.replace("plus","+")
        a=a.replace("divided ","/")
        a=a.replace("multiply","*")
        a=a.replace("minus","-")
        a=a.replace("modulo","%")
        a=a.replace("addition","+")
        a=a.replace("add","+")#
        a=a.replace("Royal Enfield","")
        speak (eval (a))
        #print (type (a))
        #a.replace("calculate","")
    except:
        speak ("wrong input")
#cal("calculate 2 $ 2")
