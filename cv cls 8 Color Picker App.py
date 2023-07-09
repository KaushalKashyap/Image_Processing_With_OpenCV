# Building Color Picker using Trackbars

import cv2
import numpy as np

def cross(x):
    pass

#create a Black color image or can say page
img = np.zeros((300,512,3), np.uint8)
cv2.namedWindow("Color Picker") # fixing the name of blank image/page

#Create Switch with the help of createTrackbar
s1 = "OFF / ON"
cv2.createTrackbar(s1,"Color Picker",0,1,cross) # it will create switch. 0 means starting value and 1 means last value
# when it is not performing any event then it will called cross which will pass.

#creating for rgb

# Creating Trackbars for Adjusting Colors
cv2.createTrackbar("R","Color Picker",0,255,cross)
cv2.createTrackbar("G","Color Picker",0,255,cross)
cv2.createTrackbar("B","Color Picker",0,255,cross)

while True:
    cv2.imshow("Color Picker",img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27: # here 27 means escape key.
        break
    
    #this is written under loop bcz whatever changes you made should reflect on image.
    #now get trackbar pos
    s = cv2.getTrackbarPos(s1,"Color Picker")
    r = cv2.getTrackbarPos("R","Color Picker")
    g = cv2.getTrackbarPos("G","Color Picker")
    b = cv2.getTrackbarPos("B","Color Picker")
    
    if s == 0: # this logic for if s == 0 then every color should be zero.
        img[:]=0
    else:
        img[:]=[r,g,b]
cv2.destroyAllWindows()