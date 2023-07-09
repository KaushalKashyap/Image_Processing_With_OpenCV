#objective is to by using image smoothening and bluring, fix the distorted pixel of blur and low visible image to good looking image.
# image smoothning or can say bluring
#it is used to remove noise from images.
#LPS - Low Pass Filter use to remove Noise from the Image.
#HPS - use to detect and finding edges in an images.

#Filters like -- 
#Homogeneous, blur(averaging), gaussian, median, bilateral

import cv2
import numpy as np

img = cv2.imread("C:\\Users\\RANGER\\Desktop\\bess1.jpg",0)
img = cv2.resize(img,(400,400))

# kernel parameter 5x5 = 25
kernel = np.ones((3,3),np.float32)/9
# Filter 
# Homogeneous filter. this filter work like, each output pixel is the mean of its kernel neighbors
# it is aka homogeneous filter in this all pixel contribute with equal weight.
# kernel is a small shape or matrix which he apply on image.
# in this filter kernel is [(1/kernel(h,w))*kernel]

# jo bhi image ke neighbors pixel hote h uske mean value nikal ke image pixel se replace kr deta hai..
# what this filter does that, it replace the pixel value by calculating the mean of neighbors pixels., 
h_filter = cv2.filter2D(img,-1,kernel) # -1 is desired depth.

# take the avg of all the pixel under kernel area.
# replace the central element with this average.
blur = cv2.blur(img,(2,2)) # (5,5 is kernel parameter(row,column))

#Gaussian filter - it uses different weight kernel in row as well as column
# it means side value are small then centre. It manage distance b/w value of pixels.
gau = cv2.GaussianBlur(img,(5,5),0) # here 0 is sigma x value.

# Median Blur computes the median of all the pixels under the kernel window
# and the central pixel is replaced with this median value.
# this works very fine in removing salt and pepper noise.
# here kernel size must be odd except one.
med = cv2.medianBlur(img,5) #kernel = 5

#Bilateral Filter .. Highly effective at noise removal while preserving edges.
# It works like gaussian filter but more focus on edges.
# it is slow as compare with other filters
# argument (img, neighbor_pixel_diameter, sigma_color, sigma_space)
bi_f = cv2.bilateralFilter(img,9,75,75)
# it works on edge surface of the object and make it sharp.
cv2.imshow("Original == ", img)
cv2.imshow("Homogeneous ",h_filter)
cv2.imshow("Blur ",blur)
cv2.imshow("Gaussian filter",gau)
cv2.imshow("median filter",med)
cv2.imshow("Bilateral filter",bi_f) 

cv2.waitKey(0)
cv2.destroyAllWindows()