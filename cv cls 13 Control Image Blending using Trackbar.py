# Control Image blending with Trackbars
import cv2
import numpy as np

img1 = cv2.imread("C:\\Users\\RANGER\\Desktop\\beauty and the beast.jpg")
img1 = cv2.resize(img1,(500,700))
img2 = cv2.imread("C:\\Users\\RANGER\\Desktop\\Koenigsegg_Agera_N_.jpg")
img2 = cv2.resize(img2,(500,700))

#cv2.imshow("Image 1",img1)
#cv2.imshow("Image 2",img2)

def blend(x):
    pass

img = np.zeros((400,400,3),np.uint8)  # blank image when switch is off.
cv2.namedWindow('win') #create trackbar windows
cv2.createTrackbar('alpha','win',1,100,blend) # create trackbar named alpha, inside win window, will have range of 1-100,blend function 
switch = '0 : OFF \n 1: ON' # create switch for invoke the trackbars
cv2.createTrackbar(switch,'win',0,1,blend)# create trackbar for switch

while True:
    s = cv2.getTrackbarPos(switch,'win')
    a = cv2.getTrackbarPos("alpha", 'win')
    n = float(a/100)
    print(n)
    
    if s == 0: # if switch off
        dst = img[:] # show blank image
    else:
        # here blending is performing. parameter (Image1,) 
        # as you know the sum of weight of both images should be 1. 
        # the logic here is n is a/100, which becomes less than 1, so 1-n will be image1 weight and n will be image2 weight.
        dst = cv2.addWeighted(img1,1-n,img2,n,0)
        cv2.putText(dst, str(a), (20,50),cv2.FONT_ITALIC,2,(0,125,255),2)
    cv2.imshow("dst",dst)
    
    k = cv2.waitKey(1)& 0xFF
    if k == 27:
        break


cv2.waitKey()
cv2.destroyAllWindows()