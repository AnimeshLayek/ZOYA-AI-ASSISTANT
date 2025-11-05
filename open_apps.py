import pyautogui
Query = "open camera"
if "open" in Query:
        Query = Query.replace("please","")
        Query = Query.replace("open","")
        Query = Query.replace("jarvis","")
        Query = Query.replace("the","")
        pyautogui.press("super")
        pyautogui.typewrite(Query)
        pyautogui.sleep(2)
        pyautogui.press("enter")