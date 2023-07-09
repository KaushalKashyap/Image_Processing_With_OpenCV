# Image Gradient..
# It is a directional change in the color or intensity in an image
# it is most important part to find information from range.
# Like finding edges within the images.
# There are various methods to find image gradient.
# laplacian Derivatives, SobelX and SobelY.
# image should be gray scale.

import cv2 
import numpy as np

img = cv2.imread("C:\\Users\\RANGER\\Desktop\\pixabay.jpg",0)
img = cv2.resize(img,(400,400))

# Laplacian = it calculate la placian derivate in pixels.
# parameter (image, data_type for -ve val,ksize)
# why datatype (because in laplacian derivate calculation if any -ve number found then these special datatye will handle those -ve numbers.)
lap = cv2.Laplacian(img,cv2.CV_64F,ksize=3)
# here in edges filtration you may find so much noise.
# so for clear edge filtration we will create array
# ksize will alway be odd number.
lap = np.uint8(np.absolute(lap))


# sobel Operation
# joint operation of Gaussian Smoothening and Differentiation operation.
# more resistant to noise.
# parameter(image, type for -ve val, x= 1(#vertical lines), y=0(horizontal line), ksize)

sobelX= cv2.Sobel(img, cv2.CV_64F,1,0,ksize=3)
sobelY= cv2.Sobel(img, cv2.CV_64F,0,1,ksize=3)
# here you may find very noise and distortion which is caused by datatype which hold 64 byte int size.
# which is why we need  to convert it into unsigned int 8.
sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))

# here you can find the difference i.e., in sobelX pixel will be verfied by vertically (top-buttom), 
# but in sobelY it is verified by Horizontal way( left - right).

# finally combine sobelX and sobelY
sobelcombine = cv2.bitwise_or(sobelX,sobelY)

cv2.imshow("grayimage",img)
cv2.imshow("Laplacian",lap)
cv2.imshow("Sobelx",sobelX)
cv2.imshow("Sobely",sobelY)
cv2.imshow("SobelCombine",sobelcombine)
cv2.waitKey(0)
cv2.destroyAllWindows()