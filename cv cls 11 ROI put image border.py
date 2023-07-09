# creating image border
# with the help of cv2.copyMakeBorder() 
# it takes parameter like(img, border_width(4-sides), bordertype, val_brder)
# border width = top, bottom, right, left...

import cv2
import numpy

img1 = cv2.imread("C:\\Users\\RANGER\\Desktop\\beauty and the beast.jpg")
img1 = cv2.resize(img1, (1000,600))

# creating image border
brdr = cv2.copyMakeBorder(img1,10,10,15,15, cv2.BORDER_CONSTANT, value = [255,0,255])

cv2.imshow("res",brdr)
cv2.waitKey()
cv2.destroyAllWindows()