# At first install "opencv" module by typing "pip install opencv-python"

import cv2                                # cv2 import from 'opencv'



def open_cam():                           # define a function for camera opening
    img_counter = 0
    video=cv2.VideoCapture(0)             # activate the camera 
    while(True):
        ret,frame = video.read()          # video.read() is use to read the footage and ret and frame used to store the capture footage image 
        cv2.imshow('camera is open ---- press "space bar" to take picture and press "Esc" to exit',frame)# it is used to show the image which is store in frame by a popup window 
        k = cv2.waitKey (1)
        #print ("camera is open ")
        
        if k%256 == 27:
            print ("Esc key is pressed ")
            print ("camera is off")
            break
        elif k%256 == 32:
            img_name = "opencv_picture_{}.png".format(img_counter)
            cv2.imwrite(img_name,frame)
            print ("space bar is pressed and picture is taken ")
            img_counter = img_counter + 1
            
    video.release()                       # this function deactivate the camera 
    cv2.destroyAllWindows()               # this is close the window
    
query = input ("enter query :")

if (query=="take_pic"):
    open_cam()