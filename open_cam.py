# At first install "opencv" module by typing "pip install opencv-python"

import cv2                                # cv2 import from 'opencv'


def open_cam():
    video=cv2.VideoCapture(0)             # activate the camera 
    while(True):
        ret,frame = video.read()          # video.read() is use to read the footage and ret and frame used to store the capture footage image 
        cv2.imshow('camera is open',frame)# it is used to show the image which is store in frame by a popup window 
        if cv2.waitKey(1) & 0xFF == ord('s'): # the terminating condition for close the camera 
            break
    video.release()                       # this function deactivate the camera 
    cv2.destroyAllWindows()               # this is close the window
    
query = input ("enter query :")
if (query=="open_camera"):
    open_cam()