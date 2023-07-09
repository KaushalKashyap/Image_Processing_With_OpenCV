# image pyramid. image pyramid is basically single bt many image with different resolution.
# why we need this.. at the time of object deection or image blending you might need to focus on some spit hole which mey be not observable from given resultion image.
# so we create many image of same image with different resolution to detect things or objects.
# two types of it.. # Gaussian Pyramid # Laplacian Pyramid.
import cv2
import numpy as np

img = cv2.imread("C:\\Users\\RANGER\\Desktop\\cdc.jpg",0)
img = cv2.resize(img,(500,500))

#in Gaussian we have 2 function  cv2.pyrUp(), cv2.pyrDown()
pd1 = cv2.pyrDown(img) 
pd2 = cv2.pyrDown(pd1)

pd3 = cv2.pyrDown(pd2)

cv2.imshow("Original ",img)
cv2.imshow("pddown1 ",pd1)
cv2.imshow("pddown2",pd2)
cv2.imshow("pdup",pd3)

cv2.waitKey(0)
cv2.destroyAllWindows()