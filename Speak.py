import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    Id = r'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'   # girl voice id
    #Id = r'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0' # boy voice id
    engine.setProperty('voice',Id) # set the proporty of voice passing id
    print("")
    print(f"==> ZOYA AI : {text}")
    print("")
    engine.say(text=text)
    engine.runAndWait()  