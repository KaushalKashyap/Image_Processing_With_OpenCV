#Contours - 
###############################################################################################################
#Contours can be explained simply as a curve joining all the continuous points 
#(along the boundary), having same color or intensity. 

#The contours are a useful tool for shape analysis and object detection and recognition

#For better accuracy, use binary images and also apply edge detection before 
#findig countours.

#findCountour function manipulate original imge so copy it before proceeding.
#findContour is like finding white object from black background.
#so you must turn image in white and background is black.

#We have to find and draw contours as per the requirement

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
############################################################################################################################
"""
import cv2
import numpy as np

img = cv2.imread("C:\\Users\\RANGER\\Desktop\\Z7.jpg")
img = cv2.resize(img,(600,700))
img1 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret,thresh = cv2.threshold(img1,220,255,cv2.THRESH_BINARY_INV)

#findcontour(img,contour_retrival_mode,method)
# detecting contours after after thresholding image...
# cnts(coordinate),hier(hierarchy) = findcontour(img,contour_retrival_mode,method)
# this function return list containing coordinates of founded contours and ech contour is an array of x,y and heirarchy
cnts,hier = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
#Here cnts is a list of contours. ANd each contour is an array with x, y cordinate   
#hier variable called hierarchy and it contain image information.
print("Number of contour==",cnts,"\ntotal contour==",len(cnts))
print("Hierarchy==\n",hier)

# loop over the contours
for c in cnts:
    # compute the center of the contour
    #an image moment is a certain particular weighted average (moment) of the image pixels
    M = cv2.moments(c)
    print("M==",M)
    # These are nothing but the formula to find the x and y coordinate 
    # # you can extract useful data like area, centroid etc. Centroid is given by the relations, Cx=M10/M00 and Cy=M01/M00.
    cX = int(M["m10"] / M["m00"])
    cY = int(M["m01"] / M["m00"])
    
    
    # draw the contour and center of the shape on the image
    cv2.drawContours(img, [c], -1, (0, 255, 0), 2)
    cv2.circle(img, (cX, cY), 7, (255, 255, 255), -1)
    cv2.putText(img, "center", (cX - 20, cY - 20),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
    
cv2.imshow("original===",img)
cv2.imshow("gray==",img1)
cv2.imshow("thresh==",thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""
""" 
############################################################################################################################################
#-------------Contour Area , Approximation and Convex hull

#Find countour area , aprroximation and convex hull
img = cv2.imread("C:\\Users\\RANGER\\Desktop\\Z7.jpg")
img = cv2.resize(img,(600,700))
img1 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret,thresh = cv2.threshold(img1,220,255,cv2.THRESH_BINARY_INV)

#findcontour(img,contour_retrival_mode,method)
cnts,hier = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
#Here cnts is a list of contours. ANd each contour is an array with x, y cordinate   
#hier variable called hierarchy and it contain image information.
print("Number of contour==",cnts,"\ntotal contour==",len(cnts))
#print("Hierarchy==\n",hier)

area1 = []
# loop over the contours
for c in cnts:
    # compute the center of the contour
    #an image moment is a certain particular weighted average (moment) of the image pixels
    M = cv2.moments(c)
    #print("M==",M)
    cX = int(M["m10"] / M["m00"])
    cY = int(M["m01"] / M["m00"])
    #find area of contour
    area = cv2.contourArea(c)
    area1.append(area)
    
    if area<10000:
        #contour Approx -  it is use to approx shape with less number of vertices
        epsilon = 0.1*cv2.arcLength(c,True) #arc lenght take contour and return its perimeter
        data= cv2.approxPolyDP(c,epsilon,True)
        #Convexhull is used to provide proper contours convexity.
        
        hull = cv2.convexHull(data)
        
        x,y,w,h = cv2.boundingRect(hull)
        img = cv2.rectangle(img,(x,y),(x+w,y+h),(125,10,20),5)
 
    # draw the contour and center of the shape on the image
    cv2.drawContours(img, [c], -1, (50, 100, 50), 2)
    cv2.circle(img, (cX, cY), 7, (255, 255, 255), -1)
    cv2.putText(img, "center", (cX - 20, cY - 20),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
    
    
cv2.imshow("original===",img)
cv2.imshow("gray==",img1)
cv2.imshow("thresh==",thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""

####################################################################################################################################
# find contours in an image of hand show convexity
# Convexhull is nothing but the whole area where all contours exists. 

import cv2

img = cv2.imread("C:\\Users\\RANGER\\Desktop\\hand.jpg")
img = cv2.resize(img,(600,700))
img1 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# when performing threshold after that too we are not getting clear view and noiseless image. yes there are still some dot marks and noises.
# so we will clean it manually
blur = cv2.medianBlur(img1,5)
ret,thresh = cv2.threshold(blur,240,255,cv2.THRESH_BINARY_INV)

#findcontour (img,contour_retrieval_mode, method)
cnts, hier = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Draw the contours
#cv2.drawContours(img,cnts,-1,(50,50,150),2) # here -1 means draw all contours from image.

# convexHull...
for c in cnts:
    epsilon = 0.0001* cv2.arcLength(c,True) #
    data = cv2.approxPolyDP(c,epsilon,True)
    
    hull = cv2.convexHull(data)
    
    cv2.drawContours(img, [c], -1 ,(50,50,150),2)
    cv2.drawContours(img, [hull], -1 ,(0,255,0),2)

# Convexity Effect 
hull2 = cv2.convexHull(cnts[0],returnPoints = False) # hull2 will store the coordinates when returnpoints= False. 
# defect returns an array which contain value [start_point, end_point, far point, approximation points]
defect = cv2.convexityDefects(cnts[0], hull2)


for i in range(defect.shape[0]):
    s,e,f,d = defect[i,0]
    print(s,e,f,d)
    start = tuple(c[s][0])
    end = tuple(c[e][0])
    far = tuple(c[f][0])
    # cv2.line(img, start, end, [255,0,0],2)
    cv2.circle(img, far, 5,[0,0,255],-1)

# Extreme Points
#it means topmost, bottommost, rightmost, leftmost point of the object.

c_max = max(cnts, key=cv2.contourArea)

#determine the most extreme points along the contour
extLeft = tuple(c_max[c_max[:, :, 0].argmin()][0])
extRight = tuple(c_max[c_max[:, :, 0].argmin()][0])
extTop = tuple(c_max[c_max[:, :, 1].argmin()][0])
extButtom = tuple(c_max[c_max[:, :,1].argmin()][0])

# draw the ouline of the object then draw each of the extreme points, where the left most is red, right-most is green, top-most is blue, and buttom most is teal.

cv2.circle(img,extLeft,8,(255,0,255),-1)#pink
cv2.circle(img,extRight,8,(0,125,255),-1)#brown
cv2.circle(img,extTop,8,(255,10,0),-1)#blue
cv2.circle(img,extButtom,8,(19,152,152),-1)#green

cv2.imshow("Original==",img)
cv2.imshow("gray== ",img1)
cv2.imshow("Threshold= ",thresh) 
cv2.waitKey(0)
