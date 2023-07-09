# Canny Edge Detection (edge detection approach)
# it combines 5 steps 1- Noise Reduction(gaussian), 2- Gradient Calculation, 3- Non-maximum suppresson, 4- Double Threshold, 5- Edge Tracking by hysteresis
"""
import cv2
import numpy as np

img = cv2.imread("C:\\Users\\RANGER\\Desktop\\usgs-W.jpg",0)
img = cv2.resize(img,(500,500))

# canny(img,thresh1,thresh2 at different lvl.
canny = cv2.Canny(img,10,200)


cv2.imshow("Original Gray",img)
cv2.imshow("Canny",canny)

cv2.waitKey(0)
cv2.destroyAllWindows()


"""
################################################
# using Trackbar perform canny edge detection.

import cv2
import numpy as np

img = cv2.imread("C:\\Users\\RANGER\\Desktop\\Koenigsegg_agera.jpg",0)
img = cv2.resize(img,(600,600))

def nothing(x):
    pass

cv2.namedWindow("Canny")
cv2.createTrackbar("Threshold","Canny",0,255,nothing)

while True:
    a = cv2.getTrackbarPos("Threshold","Canny")
    print(a)
    res = cv2.Canny(img,a,255)
    cv2.imshow("Canny",res)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

cv2.waitKey(0)
cv2.destroyAllWindows()
