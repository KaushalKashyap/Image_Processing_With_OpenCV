# Objective - to select an object from one image and put it into another images (Object Subtraction).
# This operation will be performed using ROI, BITWISE operators, Thresholding..
import cv2
import numpy as np

img1 = cv2.imread('C:\\Users\\RANGER\\Desktop\\livia.jpg')
img2 = cv2.imread('C:\\Users\\RANGER\\Desktop\\sebastiaan.jpg')

# One important thing here is that Image 1 should be bigger than image 2.
# image2 = where object will be selected , Image1 = where selected object will be placed.
img1= cv2.resize(img1,(1024,650))
img2= cv2.resize(img2,(700,650))

# Here we are getting no. of rows,columns and channel of image 2.
r,c,ch = img2.shape

print(r,c,ch)

# ROI
# basically ROI will store size of image2(700,650) in image 1.
roi = img1[0:r,0:c] # in img1 0 to row of image2(700),0 to column of image2(650).

# we will use Thresholding to cutout the object part from image by given pixel value. 
# Now pixel value what i provide is from ms paint.
# (180,230)(440,490)
#first convert image2 into grayscale 
img_gray= cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
# now we will perform masking which help us to get exact object without background.  
_,mask = cv2.threshold(img_gray, 100,255, cv2.THRESH_BINARY)
# about above parameters, (gray image source, Threshold value, maximum threshold value, threshold type)
# for getting only object, try to change and see for perfrect pixel where only object if getting fetched with no background.

# to subtracting background.
mask_inv = cv2.bitwise_not(mask) # this will inverse the whole image color pixel. black to white and white to black.so you will have no background 

# put mask into roi
img1_bg = cv2.bitwise_and(roi,roi, mask = mask_inv)


# Now will perform bitwise operation to cutout the selected or detected part of object. It will take only region of figure from original image.
img2_fg = cv2.bitwise_and(img2,img2,mask=mask)

# put img in ROI and Modify the main image.
res = cv2.add(img1_bg, img2_fg)

final = img1

final[0:r,0:c] = res

cv2.imshow("image1", img1)
cv2.imshow("image2", img2)
cv2.imshow("ROI", roi)
cv2.imshow("1 Gray", img_gray)
cv2.imshow("2 Mask",mask)
cv2.imshow("3 image reverse",mask_inv)
cv2.imshow("4 Put Mask Background",img1_bg)
cv2.imshow("5 foreground",img2_fg)
cv2.imshow("Result", res)
cv2.imshow("Final", final)

cv2.waitKey(0)
cv2.destroyAllWindows()