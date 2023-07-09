# bitwise operation on Image'
# AND, OR, NOT, and XOR
# and find ROI(region of Interest) which is in complex shape.

import cv2
import numpy as np

img1 = np.zeros((250,500,3), np.uint8)
img1 = cv2.rectangle(img1,(150,100),(200,250),
                     (255,255,255),-1)

img2 = np.zeros((250,500,3), np.uint8)
img2 = cv2.rectangle(img2,(10,10),(170,190),
                     (255,255,255),-1)

cv2.imshow("Image 1",img1)
cv2.imshow("Image 2",img2)

#basically AND operator return common from both values.
#bitAnd = cv2.bitwise_and(img2,img1)
#cv2.imshow("Bitand",bitAnd)

# Or operator merge both image.
#bitOr = cv2.bitwise_or(img2, img1)
#cv2.imshow("bitOr",bitOr)

# Not Operator 
#bitNot1= cv2.bitwise_not(img1)
#bitNot2= cv2.bitwise_not(img2)
#cv2.imshow("Bitnot1",bitNot1)
#cv2.imshow("Bitnot2",bitNot2)

# XOR Operator will negate (Opposite) of other two value.
# if place is black will be converted to white. if both white then will be converted to black,  
bitXor= cv2.bitwise_xor(img1,img2)
cv2.imshow("bitxor",bitXor)


cv2.waitKey(0)
cv2.destroyAllWindows()