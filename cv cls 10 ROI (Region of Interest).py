# Region of Interest here is nothing but just some cordinate or some particular point in image where you want to work on..
# suppose there is an image of some one person, and objective is to work on face of the person.
# In this situation, you need to focus only on face (particular coordinate axes where face lies..)

import cv2
import numpy as np

#read
img = cv2.imread("C:\\Users\\RANGER\\Desktop\\beauty and the beast.jpg")

img = cv2.resize(img,(800,600))

#ROI (Region of Interest)
# (180,220) (545,544)
# (y1,y2),(x1,x2)
roi = img[220:544,180:545]






cv2.imshow("Original",roi)
cv2.waitKey()
cv2.destroyAllWindows()