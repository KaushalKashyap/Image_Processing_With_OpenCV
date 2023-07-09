# HSV (Hue saturation value) color detection. 
# with the help of hsv we easily separate the color information and its intensity
import cv2
import numpy as np

frame = cv2.imread("C:\\Users\\RANGER\\Desktop\\Koenigsegg_Agera_N_.jpg")
frame = cv2.resize(frame,(700,700))
while True:
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV) # you will convert image(frame) to hsv
    u_v=np.array([130,235,225]) # upper value
    l_v = np.array([110,50,50]) # lower value
    # creating mask
    mask = cv2.inRange(hsv,l_v,u_v)
    
    #solve or filter the mask
    res = cv2.bitwise_and(frame,frame, mask=mask)
    
    cv2.imshow("frame",frame)
    cv2.imshow("mask",mask) 
    cv2.imshow("res",res)
    
    key = cv2.waitKey(1)
    if key == 27:
        break
cv2.destroyAllWindows()