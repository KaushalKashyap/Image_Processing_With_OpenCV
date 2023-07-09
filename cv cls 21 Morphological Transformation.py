# improve damaged image to near about original image.
# Morphological Transformation= Morphological Transformation will help you to mask the image at its good pixel management.

# helps in finding the shapes in image
# it is normally performed on binary images. (grayscale (hsv portions))
# It need two thing. Original image, Structuring Element(kernel)
# two types of it. Erosion and Dilation

# Erosion - it erodes away the boundaries of foreground object.
# (it make large and seggregate the foreground object, with the help of kernel )
# simply understand this way. when you do masking and thresholding the image, you actually loss many border of image due to shadow or color affection. 
# Erosion will help you to have proper shape of that object when performing threshold or masking.

# Note(* mandatory): Always morphological image should have black background and objects should be in white. 

import cv2
import numpy as np

# Image Reading and conversion to grayscale image
img = cv2.imread("C:\\Users\\RANGER\\Desktop\\george-desipris.jpg",0)
img = cv2.resize(img, (500,500))

# set up the pixel value where you find full accessible of the objects 
_,mask = cv2.threshold(img,80,255,cv2.THRESH_BINARY_INV) # here why Threshbinaryinverse is used because it will convert image background to black and image's objects into white.

# Structuring element(kernel) 
kernel = np.ones((5,5),np.uint8) #simple array (5*5) kernel with full of ones.
# With the help of erosion, we will rotate the kernel to compare. 

e = cv2.erode(mask,kernel)

# Dilation --
# it is just opposite of Erosion.
# here, a pixel element is '1', if atleast one pixel under the kernel is '1'.
# it increment the white region in the image or size or foreground object in.
# Normally, in cases like noise removal , erosion is followed by dilation.
# Because, erosion removes white noises, but it is also shrinks our object.
# erosion works well with boundaries of object, but if any distortion found in between object erosion ruin it when shaping the boundaries.

kernel = np.ones((2,2),np.uint8) # try (1,1) to see the difference.
d = cv2.dilate(mask,kernel) # iteration =2

# using matplotlib plot the images.
from matplotlib import pyplot as plt
titles = ["Img","mask","erosion","dilation"]
images = [img,mask,e,d]

for i in range(4):
    plt.subplot(2,2, i+1), plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])#for gaps between images
plt.show()


#cv2.imshow("image", img)
#cv2.imshow("Mask",mask)
#cv2.imshow("kernel",kernel)
#cv2.imshow("Erosion",e)
#cv2.imshow("Dilation",d)
cv2.waitKey(0)
cv2.destroyAllWindows()