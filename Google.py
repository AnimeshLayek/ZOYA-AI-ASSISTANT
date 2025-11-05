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

# Ignore unnecessary warnings
warnings.simplefilter("ignore")

def google_search():
    try:
        
        y = True
        while y:
            # Define the URL
            speak(" what do i search ? sir ")
            Query = get_command()
            Query.replace("search","")
            Query.replace("zoya","")
            Query.replace("joya","")
            Query.replace("jya","")
            Query.replace("from","")
            Query.replace("the","")
            Query.replace("please","")
            Query.replace("show","")
            Query.replace("me","")
            Query.replace("of","")
            if "picture" in Query or "image" in Query or "photo" in Query or "screenshort" in Query:
                image_name = Query.replace("photo","")
                image_name = Query.replace("image","")
                image_name = Query.replace("picture","")
                image_name = Query.replace("screenshort","")
                url = "https://www.google.com/search?q="+image_name+"&sca_esv=2465539c7fa84006&hl=en-GB&biw=1536&bih=730&udm=2&ei=ePAWZqH6Lozf2roPjZSs8AY&ved=0ahUKEwihlru2uLiFAxWMr1YBHQ0KC24Q4dUDCBA&uact=5&oq=gole&gs_lp=Egxnd3Mtd2l6LXNlcnAiBGdvbGUyDRAAGIAEGIoFGEMYsQMyChAAGIAEGIoFGEMyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABEjtG1AAWPQXcAF4AJABAJgB8QGgAccGqgEFMC4yLjK4AQPIAQD4AQGYAgSgAt8GqAIAwgIIEAAYgAQYsQOYAwPiAwUSATEgQJIHBTAuMi4yoAe1Ew&sclient=gws-wiz-serp"
            else:    
                Query.replace("google","")
                url = "https://www.google.com/search?q="
                url = url + Query

            # Set up Chrome options
            chrome_driver_path = "D:\\code\\ZOYA\\chromedriver-win64\\chromedriver.exe"  # Write the path of chromedriver.exe file
            chrome_options = Options()
            chrome_options.headless = False #see to apening chrome
            #chrome_options.add_argument("--headless=new")
            chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
            chrome_options.add_argument('--log-level=3')
            service = Service(chrome_driver_path)
            chrome_options.add_argument("--use-fake-ui-for-media-stream")  # Disable UI pop-ups for media access
            chrome_options.add_argument("--use-fake-device-for-media-stream")

            # Initialize the Chrome driver
            driver = webdriver.Chrome(service=service, options=chrome_options)
            driver.maximize_window()
            driver.get(url)

            x = True
            speak(" sir here i find some results according to your query ")
            sleep(2)

            while x:

                speak(" i will close the search window sir ")
                Query = get_command()
                if (("close" in Query or "off" in Query) and "window" in Query) or ("yes" in Query):
                    speak(" thank you sir i am closing the google window ")
                    x = False
                    y = False
                elif "wait" in Query or "no" in Query :
                    speak(" ok sir i am wating few second ")
                    sleep(10)
                    speak(" now")
                elif "search" in Query or "qusation" in Query or "thing" in Query:
                    x = False
                    y = True


    except Exception as e: #if there is any error in try statement then executed except statement
        print("Error: Unable to configure the ChromeDriver properly.")
        print("To resolve this error, make sure to set up the ChromeDriver correctly.")
        print(e) #print the error

