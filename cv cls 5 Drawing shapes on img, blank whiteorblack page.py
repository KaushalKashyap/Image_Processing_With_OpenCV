# Drawing Function in OpenCV
import cv2
import numpy as np

#img1= cv2.imread("C:\\Users\\VICTORS\\Desktop\\Koenigsegg_Agera_N_.jpg")
# print(img1)

# or if you want to create a blank image and draw all below shape on it.
#img1=cv2.resize(img1,(700,600))

#it accept parameter(height,width, channel, start_co, end_co, color, thickness)
#img1 = np.zeros([512,512,3],np.uint8)*255 # for black screen and uint8 (unsigned int 8)..
img1 = np.ones([512,512,3], np.uint8)*255
img1=cv2.resize(img1,(900,700))

# Here line accept 5 parameter (img, (starting) (ending), (color code), thickness of line)
img1 = cv2.line(img1,(0,0),(200,200), (154,92,424),8)# color format BGR

#arrowed line accept also 5 parameter (img, starting, ending, color, thickness of line)
img1 = cv2.arrowedLine(img1, (0,125), (255,255), (255,0,255),10)

#Rectangle - accept parameter(img, start_co, end_co, color, thickness)
#if thickness value is -1, means it will be act different . fill the whole shape with given color.
img1 = cv2.rectangle(img1, (384,10), (510,128),(128,0,255),8)
img1 = cv2.rectangle(img1, (520,100), (720,320),(128,0,255),-1)

# circle - accept (img,star_co, radius, color, thickness)
img1 = cv2.circle(img1, (447,125),63,(214,255,0),5)

# puttext - accept (img, text,start_co, font, fontsize, color, thickness, linetype)
font = cv2.FONT_ITALIC
img1 = cv2.putText(img1, "Agera", (20,500), font, 2, (0,125,255),10,cv2.LINE_AA)

# ellipse-accept(img, start_cor, (length,height),x_coordinate,y_coordinate,color thickness)
img1 = cv2.ellipse(img1,(400,600),(100,50),0,0,270,200,2)


cv2.imshow("original",img1)
cv2.waitKey(0)
cv2.destroyAllWindows()