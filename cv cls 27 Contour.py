

"""
# Image Contours helps in shape Detection, Analyzation and Recognition.
# contours is just like a curve which is made by continous data. and this depends on the color or its intensity.
# In Simple words, (it is simply a curve joining all continous points which is having same color or intensity).
# Accepts gray Scale image.
# findContour() manipulate original image, so copy it before proceeding.
# findContour() is like finding white object from black background. so better be change the image accordingly.
# Contour Features:-
# Moments, Contour Area, Contour Perimeter, Contour approximation , Convexhull, Checking convexity, Bounding Rectangle(Straight boundary Rectangle, Rotated Rectangle), Minimum enclosing circle, Fitting an Ellipse, Fitting a line, 
# Contour retrieval Mode
# RETR_LIST = it simply retrieves all the contours and store in the list.
# RETR_EXTERNAL = You can use this mode if you want to extract only the outer contours. It might be useful in some cases.
# RETR_CCOMP =This mode retrieves all the contours and arranges them to a 2-level hierarchy. ie external contours of the 
# object (ie its boundary) are placed in hierarchy-1. And the contours of holes inside object (if any) is placed in hierarchy-2
# RETR_TREE =  It retrieves all the contours and creates a full family hierarchy list.


import cv2
import numpy as np

img = cv2.imread("C:\\Users\\RANGER\\Desktop\\Z7.jpg")
img = cv2.resize(img,(600,600))
img1 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img1 = cv2.resize(img1,(600,600))

ret,thresh = cv2.threshold(img1,63,255,0)

# detecting contours after after thresholding image...
# cnts(coordinate),hier(hierarchy) = findcontour(img,contour_retrival_mode,method)
# this function return list containing coordinates of founded contours and ech contour is an array of x,y and heirarchy
cnts, hier = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

print(cnts,len(cnts))

# draw Contours 
# drawcontour(img,cnts, id of contour, color, thickness) # here if we draw contour just pass -1
img = cv2.drawContours(img,cnts,-1,(25,100,15),4)
# as you can see in the ouput dialog, there are 61 contour in this image if you want to perform on some specific number of contours.
# then write the number at -1(number should be between 0 number of contours.)
# img = cv2.drawContours(img,cnts,36,(25,100,15),4)

#output 
cv2.imshow("Originals --",img)
cv2.imshow("GrayScale--",img1)
cv2.imshow("Threshold--",thresh)


cv2.waitKey(0)
cv2.destroyAllWindows()
"""


################################################
# Contour and its functions
# Moment - Moment detect the functionality of the objects.it also return you the center points of the objects 


import cv2
#import numpy as np

img = cv2.imread("C:\\Users\\RANGER\\Desktop\\Z7.jpg")
img = cv2.resize(img,(600,700))
img1 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(img1,120,255,cv2.THRESH_BINARY_INV)

# Findcontour(img,contour_retrival_mode,method)
cnts, hier= cv2.findContours(thresh,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

print("Number of Contours==",cnts ,"\n total contour ==",len(cnts))
print("Heirarchy ",hier)
 

# loop over Contours(img, cnts, -1,(10,20,100),4)
for c in cnts:  # Loop to reach every contours for moment operation.
    #compute the center of the contour
    #an image moment is a certain particular weighted average(moment)
    M = cv2.moments(c)    # passing all contours one by one into moment function
    print("M==",M)
    cX = int(M["m10"] / M["m00"]) # formula for finding x_coordinates
    cY = int(M["m01"] / M["m00"]) # formula for finding y_coordinates
    
    # draw the contour and center of the shape on the image
    cv2.drawContours(img,[c],-1,(0,255,0),2) # drawing contours
    cv2.circle(img,(cX,cY),1,(255,255,255),2) # drawing circle just as shape 
    cv2.putText(img, "center",(cX - 20, cY -20),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,255,255),2) #getting center and print also on the object.
    # parameter (img,"text",font,fontsize, (color parameter (255,255,255), 2, cv.LINE_AA))

#output
cv2.imshow("Original ",img)
cv2.imshow("gray",img1) 
cv2.imshow("Thresh",thresh)

cv2.waitKey(0)
cv2.destroyAllWindows()

"""
# Contour and its functions
# Moment - Moment detect the functionality of the objects.it also return you the center points of the objects 
# Apprroximation

import cv2
import numpy as np

img = cv2.imread("C:\\Users\\RANGER\\Desktop\\Z7.jpg")
img = cv2.resize(img,(600,700))
img1 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(img1,120,255,cv2.THRESH_BINARY_INV)

# Findcontour(img,contour_retrival_mode,method)
cnts, hier= cv2.findContours(thresh,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

print("Number of Contours==",cnts ,"\n total contour ==",len(cnts))
print("Heirarchy ",hier)
 
area1 = []
# loop over Contours(img, cnts, -1,(10,20,100),4)
for c in cnts:  # Loop to reach every contours for moment operation.
    #compute the center of the contour
    #an image moment is a certain particular weighted average(moment)
    M = cv2.moments(c)    # passing all contours one by one into moment function
    print("M==",M)
    # you can extract useful data like area, centroid etc. Centroid is given by the relations, Cx=M10/M00 and Cy=M01/M00.
    cX = int(M["m10"]/M["m00"]) # formula for finding x_coordinates
    cY = int(M["m01"]/M["m00"]) # formula for finding y_coordinates
    
    #Finding Area of contour
    area = cv2.contourArea(c)
    area1.append(area)
    
    #Contour approx - It is use to approx shape with less number of vertices
    epsilon = 0.1 * cv2.arcLength(c,True) # arc length take contour and return it as small size as it can.
    # Note: the more small size of contour, the more good result will come.
    # 0.1 is a random value. but it shouldn't be more than 1. 
    # arclength() returns the parameter of contour
    data = cv2.approxPolyDP(c,epsilon, True)
    # then passing epsilon to polygon shape dp. Because polygon has multiple sides.
    # passed contour with True value, which will pass the value to data. other wise it will not pass to store data in data variable.
    
    # Convexhull is used to provide proper contours convexity
    # in other word, whatever area detected by contour which will be bounded with the help of convexHull() is called convexHull.
    # whatever area covered by object with what shape, will be convexity..
    hull = cv2.convexHull(data)
    
    # we are just creating bounded rectangle which will cover the whole image..
    x,y,w,h = cv2.boundingRect(hull)
    img = cv2.rectangle(img,(x,y), (x+w,y+h),(125,10,20),5)
    
    # draw the contour and center of the shape on the image
    cv2.drawContours(img,[c],-1,(0,255,0),2) # drawing contours
    cv2.circle(img,(cX,cY),7,(255,255,255),-1) # drawing circle just as shape 
    cv2.putText(img, "center",(cX - 20, cY -20),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,255,255),2) #getting center and print also on the object.
    # parameter (img,"text",font,fontsize, (color parameter (255,255,255), 2, cv.LINE_AA))

#output
cv2.imshow("Original ",img)
cv2.imshow("gray",img1) 
cv2.imshow("Thresh",thresh)

cv2.waitKey(0)
cv2.destroyAllWindows()
"""