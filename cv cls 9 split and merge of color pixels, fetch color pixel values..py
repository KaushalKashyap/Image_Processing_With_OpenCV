"""
# we perform operations on image's pixels and try to manipulate it. By using split() and merge() we perform some interest tasks.
import cv2
import numpy as np

#Read an Image...
img = cv2.imread("C:\\Users\\RANGER\\Desktop\\Koenigsegg_Agera_N_.jpg")
img = cv2.resize(img,(600,400))

print(img.shape)
print("No. of Pixels",img.size)
print(img.dtype)
print(type(img))


#print(cv2.split(img))
#Now try to split an image
# split - return 3 channel of ur image which is blue, green and red.

b,g,r = cv2.split(img)

#cv2.imshow("Blue", b)
#cv2.imshow("Green", g)
#cv2.imshow("Red", r)

#cv2.imshow("Original", img)

mr1= cv2.merge((b,g,r))
mr2= cv2.merge((r,g,b))
cv2.imshow("bgr",mr1)
cv2.imshow("rgb",mr2)
cv2.imshow("Original", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
"""

# Working on pixel color Values----
import cv2
img=cv2.imread("C:\\Users\\RANGER\\Desktop\\beauty and the beast.jpg")
img=cv2.resize(img,(1024,700))
cv2.imshow("lion==",img)

print(img.shape)
print("No. of Pixels",img.size)
print(img.dtype)
print(type(img))

# access a pixel value by its row and column coordinate
px= img[520,580] #store coordinate in variable
print("the Pixel of that co-ordinate ==",px)# we get the pixel color coordinate value

# Now try to find selected channel value from coordinate
# we know the default value of b,g,r in OpenCV is 0,1,2
#accesssing only blue pixel
blue = img[520,580,0]
print("blue color pixels",blue)

# accessing only green pixel
grn = img[520,580,1]
print("green color Pixels",grn)

# accessing only Red
red = img[520,580,2]
print("Red color Pixels",red)


cv2.waitKey(0)
cv2.destroyAllWindows()