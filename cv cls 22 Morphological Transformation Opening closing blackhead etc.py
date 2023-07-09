"""
# why do we use morphological Transformation?
# it used to decrease distortion and for good shaping of the objects.
# Two Basic operation for Morphological transformation. Opening and Closing.
# opening = it is just another name of erosion followed by dilation.
# means first Erosion and then dilation.

import cv2
import numpy as np

img = cv2.imread("C:\\Users\\RANGER\\Desktop\\dids.jpg")
img = cv2.resize(img,(500,450))
_,mask = cv2.threshold(img,110,255,cv2.THRESH_BINARY_INV)
kernel = np.ones((4,4),np.uint8) #5x5 kernel with full of ones.
o = cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel) #optional parameters iteration = 2


# Closing opposite of opening
# means first dilation and then erosion
kernel = np.ones((3,3),np.uint8) #kernel with full of ones
c = cv2.morphologyEx(mask, cv2.MORPH_CLOSE,kernel)

# Optionals
x1 = cv2.morphologyEx(mask, cv2.MORPH_TOPHAT, kernel)
x2 = cv2.morphologyEx(mask, cv2.MORPH_GRADIENT, kernel)
x3 = cv2.morphologyEx(mask, cv2.MORPH_BLACKHAT, kernel)




#cv2.imshow("img",img)
#cv2.imshow("kernel",kernel)
cv2.imshow("mask",mask)
cv2.imshow("opening",o)
cv2.imshow("closing",c)
cv2.imshow("tophat",x1)
cv2.imshow("gradient",x2)
cv2.imshow("blackhat",x3)


cv2.waitKey(0)
cv2.destroyAllWindows()

"""
import cv2
import numpy as np

img = cv2.imread("C:\\Users\\RANGER\\Desktop\\Koenigsegg_agera.jpg",0)
img = cv2.resize(img, (400,400))

_,mask = cv2.threshold(img,160,255,cv2.THRESH_BINARY_INV)
kernel = np.ones((2,2),np.uint8) # 5x5 kernel with full of ones.

#All Morphological Operation.
e=cv2.erode(mask,kernel)
d=cv2.dilate(mask,kernel)
o = cv2.morphologyEx(mask,cv2.MORPH_OPEN, kernel)
c = cv2.morphologyEx(mask,cv2.MORPH_CLOSE, kernel)
x1 = cv2.morphologyEx(mask,cv2.MORPH_TOPHAT, kernel)
x2 = cv2.morphologyEx(mask,cv2.MORPH_GRADIENT, kernel)
x3 = cv2.morphologyEx(mask,cv2.MORPH_BLACKHAT, kernel)

cv2.imshow("image",img)
cv2.imshow("mask",mask)
cv2.imshow("erosion",e)
cv2.imshow("Dilation",d)
cv2.imshow("Opening",o)
cv2.imshow("Closing",c)
cv2.imshow("Tophat",x1)
cv2.imshow("Gradient",x2)
cv2.imshow("Blackhat",x3)

cv2.waitKey(0)
cv2.destroyAllWindows()