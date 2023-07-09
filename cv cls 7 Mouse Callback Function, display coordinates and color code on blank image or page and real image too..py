# Mouse Callback Functions
import cv2
import numpy as np
"""
# here x,y are axis on page, flag are denoting click event (right/left), param means execution done or not.
def draw(event,x,y,flags, param):
    # you can see the value by printing it.
    print("x=", x)
    print("y=", y)
    print("flags", flags)
    print("param=", param)
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img, (x,y), 100,(125,0,255),5)
    if event == cv2.EVENT_RBUTTONDBLCLK:
        cv2.rectangle(img,(x,y),(x+100, y+75),(125,125,125),2)
        
cv2.namedWindow(winname = "res")

img = np.zeros((512,512,3),np.uint8)
cv2.setMouseCallback("res",draw)

while True:
    cv2.imshow("res", img)
    if cv2.waitKey(1) & 0xFF == 27 : #esc
        break
cv2.destroyAllWindows()
# On double left click will draw circle on blank page, 
# On double Right click will draw rectangle on blank page.
"""

# Create a function which help to find coordinate of any pixel and 
# its color by click event
"""
def mouse_event(event, x,y,flg,param):
    print("event = ",event)
    print("x = ",x)
    print("y = ",y)
    print("flg = ",flg)
    print("param = ",param)
    font = cv2.FONT_HERSHEY_PLAIN
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x,', ',y)
        
        cord = ". "+str(x) +', '+str(y)
        cv2.putText(img, cord, (x, y), font, 1, (155,125,100),2)
        #cv2.imshow('image', img)
    if event == cv2.EVENT_RBUTTONDOWN:
        b = img[y, x, 0] #for blue channel is 0
        g = img[y,x,1] # for green channel is 1
        r = img[y,x,2] # for red channel is 2
        
        color_bgr = ". "+str(b)+', '+str(g)+ ', '+str(r)
        cv2.putText(img, color_bgr, (x,y), font, 1, (152,255,130),2)
        #cv2.imshow('image',img)
        
cv2.namedWindow(winname = "res")

img = np.zeros((512,512,3),np.uint8)
cv2.setMouseCallback("res",mouse_event)

while True:
    cv2.imshow("res", img)
    if cv2.waitKey(1) & 0xFF == 27 : #esc
        break
cv2.destroyAllWindows()

"""

# Try the same with colored image.
def mouse_event(event, x,y,flg,param):
    print("event = ",event)
    print("x = ",x)
    print("y = ",y)
    print("flg = ",flg)
    print("param = ",param)
    font = cv2.FONT_HERSHEY_PLAIN
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x,', ',y)
        
        cord = ". "+str(x) +', '+str(y)
        cv2.putText(img, cord, (x, y), font, 1, (155,125,100),2)
        #cv2.imshow('image', img)
    if event == cv2.EVENT_RBUTTONDOWN:
        b = img[y, x, 0] #for blue channel is 0
        g = img[y,x,1] # for green channel is 1
        r = img[y,x,2] # for red channel is 2
        
        color_bgr = ". "+str(b)+', '+str(g)+ ', '+str(r)
        cv2.putText(img, color_bgr, (x,y), font, 1, (152,255,130),2)
        #cv2.imshow('image',img)
        
cv2.namedWindow(winname = "res")

#img = np.zeros((512,512,3),np.uint8)
img = cv2.imread("C:\\Users\\VICTORS\\Desktop\\Koenigsegg_Agera_N_.jpg")
cv2.setMouseCallback("res",mouse_event)

while True:
    cv2.imshow("res", img)
    if cv2.waitKey(1) & 0xFF == 27 : #esc
        break
cv2.destroyAllWindows()