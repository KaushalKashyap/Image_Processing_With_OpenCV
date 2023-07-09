# Thresholding
# In Previous, we used one global value as a threshold. But this might not be good in all cases, e.g. if an image has different lighting 
# conditions in different areas. In that case, adaptive thresholding can help. Here, the algorithm determines the threshold for a pixel based
# on a small region around it. So we get different thresholds for different regions of the same image which gives better results for images with
# varying illumination.

# Now Adaptive method contains two type.
# cv.ADAPTIVE_THRESH_MEAN_C  - Here, the threshold value is the mean of the neighbourhood area minus the constant C.
# cv.ADAPTIVE_THRESH_GAUSSIAN_C - and Here, threshold value is a gaussian-weighted sum of the neighbourhood values minus the constant C.
# The blockSize determines the size of the neighbourhood area and C is a constant that is subtracted from the mean or weighted sum of the neighbourhood pixels.

import cv2
import numpy as np
# from keras.preprocessing import image

img = cv2.imread("C:\\Users\\RANGER\\Desktop\\images.jpg")
#img = image.img_to_array(img,dtype ='uint8')
#img = img.astype(np.uint8)
img = cv2.resize(img,(400,400))
# converting original image to grayscale image.
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# Simple thresholding Parameter (imagesource,threshold value, maxthresoldvalue,threshold type,)
_,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)

#Adaptive Thresholding
# Parameter (Image Source, max_thershold value, adaptive threshold type, simple threshold type, (number of pixels))
# Adaptive Thresholding mean Constant
th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)

# Adaptive Thresholding Gaussian Constant
th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)


cv2.imshow("Image",img)
cv2.imshow("Thresh_Binary",th1)
cv2.imshow("Adaptive Thresh Mean Constant",th2)
cv2.imshow("Adaptive Thresh Gaussian Constant",th3)

cv2.waitKey(0)
cv2.destroyAllWindows()