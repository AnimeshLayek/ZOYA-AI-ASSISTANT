# At first install "opencv" module by typing "pip install opencv-python"

import cv2        # cv2 import from 'opencv'

###############################################################################
def open_image(path):
                # replace by your image path 
    img = cv2.imread(path)         # read the image
    #img1= cv2.resize(img,(500,600))# resize image----- width-height
    cv2.imshow("logo image",img)  # display the image 
    cv2.waitKey(0)                 # hold the image in screen milli-second ->
                                   # ->if value is 0 then press key to exit

################################################################################

# [j folder e ei file ta save korbi sei folder e image ta rakbi]
path = "D:/anime/Pictures/my docoment/my_docoment/my_photos.png"
i = input ("enter open_img:")
if (i=="open_img"):
    open_image(path)
else:
    print ("you enter wrong input")












