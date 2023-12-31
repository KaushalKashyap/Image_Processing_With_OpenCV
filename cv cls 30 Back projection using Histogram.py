# BackProjection using histogram technique
# With the help of back projection, we will be able to remove the background completely by detecting objects through histogram shapes.

import cv2
import numpy as np

# image data load, resizing and converting to gray scale
original_image = cv2.imread("Data\\green.jpg")
original_image = cv2.resize(original_image,(600,650))
hsv_original = cv2.cvtColor(original_image, cv2.COLOR_BGR2HSV)

# loading the cropped image part of the background of real image.
roi = cv2.imread("Data\\g.jpg")
hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)


# Histogram ROI
roi_hist = cv2.calcHist([hsv_roi], [0, 1], None, [180, 256], [0, 180, 0, 256])
mask = cv2.calcBackProject([hsv_original], [0, 1], roi_hist, [0, 180, 0, 256], 1)

# Filtering remove noise
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5)) # it will nothing but will create an array of given shape.
mask = cv2.filter2D(mask, -1, kernel)
_, mask = cv2.threshold(mask, 200, 255, cv2.THRESH_BINARY)

mask = cv2.merge((mask, mask, mask))
result = cv2.bitwise_or(original_image, mask)

cv2.imshow("Mask", mask)
cv2.imshow("Original image", original_image)
cv2.imshow("Result", result)
cv2.imshow("Roi", hsv_original)
cv2.waitKey(0)
cv2.destroyAllWindows()