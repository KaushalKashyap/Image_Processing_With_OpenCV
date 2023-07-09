"""
# How to use android Device camera as webcam in OpenCV.
import cv2
# download Ip webcam from playstore open,scroll down click start server.
# connect to laptop using given IP Address.

camera="http://192.168.117.41:8080/video"
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW) # parameter 0 is a path of any video.
cap.open(camera)
print("Check ===", cap.isOpened())
#it is 4 byte code which is use to specify the video codec.
fourcc = cv2.VideoWriter_fourcc(*"XVID") # *"XVID"
# it contains 4 parameter , name, codec, fps, resolution
output = cv2.VideoWriter("C:\\Users\\VICTORS\\Downloads\\output.avi", fourcc, 20.0,(640,480),0)

while(cap.isOpened()):
    ret, frame = cap.read() #here read the frame
    if ret == True:
        frame = cv2.resize(frame,(700,700))
        cv2.imshow('Colorframe',frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
# Release everything if job is finished
cap.release()
output.release()
cv2.destroyAllWindows()
"""
Below code is not working...
"""
import cv2
import pafy
# fetch video from online platform like youtube .. without downloading...
url = "https://www.youtube.com/watch?v=tc355CBeeX0&ab_channel=TheB1M"
data = pafy.new(url)
data = data.getbest(preftype = 'mp4')

cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
cap.open(data.url)
print("check ===",cap.isOpened())
# it is 4 byte code which is use to specify the video codec

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        frame = cv2.resize(frame,(700,700))
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow('ColorFrame',frame)
        cv2.imshow('Gray',gray)
        #output.write(frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
        """