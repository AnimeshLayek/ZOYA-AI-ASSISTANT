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

def Flipkart():
    
    try:
        # Define the URL
        url = "https://www.flipkart.com/"
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
       
        """user_agent = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.2 (KHTML, like Gecko) Chrome/22.0.1216.0 Safari/537.2'
        chrome_options.add_argument(f'user-agent={user_agent}')"""

            # Initialize the Chrome driver
        driver = webdriver.Chrome(service=service, options=chrome_options)
        driver.maximize_window()
        driver.get(url)
        speak(" flipkart is open sir ")
                
            # Wait for the page to load
        sleep(1)
        x = True
        count = 0
        while x:
                # Execute JavaScript to enable microphone access
                """driver.execute_script('navigator.mediaDevices.getUserMedia({ audio: true })')
                sleep(1)
            """
                speak(" what do I search ? sir  ")
                Query = get_command()
                Query=Query.replace("search","")
                Query=Query.replace("zoya","")
                Query=Query.replace("please","")
                Query=Query.replace("the","")
                Query=Query.replace("joya","")

                speak(" ok sir ")
                if count > 0 :
                    # send data in search ber if search more then one time
                    driver.find_element(by=By.XPATH,value="/html/body/div/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input").clear()
                    
                    driver.find_element(by=By.XPATH,value="/html/body/div/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input").send_keys(Query)
                    sleep(1)
                    pyautogui.press("enter")
                    
                else :
                     
                    # send data in search ber
                    driver.find_element(by=By.XPATH,value="/html/body/div[1]/div/div[1]/div/div/div/div/div[1]/div/div[1]/div/div[1]/div[1]/header/div[1]/div[2]/form/div/div/input").send_keys(Query)
                    sleep(1)
                    count = 1
                    # click on search icon
                    search_icon_xpath = "/html/body/div[1]/div/div[1]/div/div/div/div/div[1]/div/div[1]/div/div[1]/div[1]/header/div[1]/div[2]/form/div/button"
                    driver.find_element(by=By.XPATH, value=search_icon_xpath).click()
                    sleep(1)
                

            # Click the mine price button
                start_button_xpath = "/html/body/div/div/div[3]/div[1]/div[1]/div/div[1]/div/section[2]/div[4]/div[3]/select/option[1]"
                driver.find_element(by=By.XPATH, value=start_button_xpath).click()
                speak(" price set in lowest amount, sir ")
                y = True
                while y:
                    speak(" Apart from this, what else do you search for sir?  Otherwise I will close the Flipkart window. ")
                    Query1 = get_command()
                    if "close" in Query1 or "nothing" in Query1 or "yes" in Query1:
                        x = False
                        y = False
                        speak(" thank you sir ")
                    elif "wait" in Query1:
                        speak ("  ok sir i am waiting ")
                        sleep(10)
                    elif "search" in Query1:
                         y = False


    except Exception as e: #if there is any error in try statement then executed except statement
        print("Error: Unable to configure the ChromeDriver properly.")
        print("To resolve this error, make sure to set up the ChromeDriver correctly.")
        print(e) #print the error
#Flipkart()