#image Bleanding 
# two important function cv2.add(), cv2.addWeighted()
# 
import cv2
import numpy as np

img1 = cv2.imread("C:\\Users\\RANGER\\Desktop\\beauty and the beast.jpg")
img2 = cv2.imread("C:\\Users\\RANGER\\Desktop\\Koenigsegg_Agera_N_.jpg")
img1 = cv2.resize(img1,(500,700))
img2 = cv2.resize(img2,(500,700))

cv2.imshow("Image one", img1)
cv2.imshow("Image Twp", img2)

#result = img1+img2
#cv2.imshow("Blended")

#result = cv2.add(img1+img2)
#cv2.imshow("blended",result)

# function cv2.addWeighted(img1,wt1,img2,wt2,gama_val)  gama_val is nothing but saturation value...
# Add weighted image1,weight,image2,weight, gamma value) weight is basically in percentage. giving weight 
# value is actually you are giving, which image should be more merged and be shown more, than other.

result = cv2.addWeighted(img1, 0.7, img2,0.3,0)
cv2.imshow("Add Weighted",img)

cv2.waitKey(0)
cv2.destroyAllWindows()