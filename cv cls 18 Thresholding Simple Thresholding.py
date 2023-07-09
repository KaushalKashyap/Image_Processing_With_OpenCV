# Thresholding
# For every pixel, the same threshold value is applied. If the pixel value is smaller than the threshold, it is set to 0, 
# otherwise it is set to a maximum value. The function cv.threshold is used to apply the thresholding. The first argument is the source image,
# which should be a grayscale image. The second argument is the threshold value which is used to classify the pixel values. 
# The third argument is the maximum value which is assigned to pixel values exceeding the threshold. 
# OpenCV provides different types of thresholding which is given by the fourth parameter of the function.
# it accepts four parameter (Imagesource, pixel_thresholdvalue,max_pixel_thresholdvalue, and which type of threshold to perform.

import cv2
import numpy as np

img = cv2.imread("C:\\Users\\RANGER\\Desktop\\beauty and the beast1.jpg")
img = cv2.resize(img,(400,400))

cv2.imshow("Original",img)

# th1 (data stored in th1,), Parameter(img,min threshold value, max threshold value, style(THRESH_BINARY) iT MEANS threshold binary means either 0 or 1...

#THRESH_BINARY = { dst(x,y) = {maxval if src(x,y) > THRESH else 0 Otherwise}}
_, th1 = cv2.threshold(img,50,255,cv2.THRESH_BINARY)
cv2.imshow("1 - THRESH_BINARY",th1)

#THRESH_BINARY_INV = { dst(x,y) = {0 if src(x,y) > THRESH else maxval Otherwise}}

# now with Binary Inverse ()
_, th2 = cv2.threshold(img,50,255,cv2.THRESH_BINARY_INV)
cv2.imshow("2 - THRESH_BINARY_INVERSE",th2)

#THRESH_TRUNC = { dst(x,y) = {THRESHOLD if src(x,y) > THRESH else src(x,y) Otherwise}}

_, th3 = cv2.threshold(img,120,255,cv2.THRESH_TRUNC)
cv2.imshow("3 - THRESH_BINARY_TRUNCATED",th3)

#THRESH_TOZERO = { dst(x,y) = {src(x,y) if src(x,y) > THRESH else 0 Otherwise}}

_, th4 = cv2.threshold(img,120,255,cv2.THRESH_TOZERO)
cv2.imshow("4 - THRESH_TOZERO",th4)

#THRESH_TOZERO = { dst(x,y) = {0 if src(x,y) > THRESH else src(x,y) Otherwise}}

_, th5 = cv2.threshold(img,120,255,cv2.THRESH_TOZERO_INV)
cv2.imshow("5 - THRESH_TOZERO_INV",th5)

cv2.waitKey(0)
cv2.destroyAllWindows()
