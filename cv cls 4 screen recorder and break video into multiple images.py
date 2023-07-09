"""
# Screen Recorder
import cv2 as c
import pyautogui as p
import numpy as np

#XVID is a codec which helps to make frame to write/save your video..

# Create resolution
rs = p.size()

#filename in which we store recording
fn = input("Please Enter any file name and Path")
# Fix the frame rate
fps = 60.0

fourcc = c.VideoWriter_fourcc(*'XVID')
output = c.VideoWriter(fn,fourcc, fps,rs)

# create recording module
c.namedWindow("Live_Recording",c.WINDOW_NORMAL)
c.resizeWindow("Live_Recording",(600,400))

while True:
    img = p.screenshot()
    f = np.array(img)
    f = c.cvtColor(f,c.COLOR_BGR2RGB) #color convert
    output.write(f)
    c.imshow("Live_Recording",f)
    if c.waitKey(1) == ord("q"):
        break
output.release()
c.destroyAllWindows()
"""

# Break video into Multiple Images and Store in a folder
import cv2

vidcap = cv2.VideoCapture("C:\\Users\\VICTORS\\Downloads\\cv\\Course Resources and Study Material _ Image Processing and Computer Vision _ Github_.mp4")
ret, image = vidcap.read() # Read the Video
count = 0
while True:
    if ret == True:
        cv2.imwrite("C:\\Users\\VICTORS\\Desktop\\imgN%d.jpg"%count,image)
        vidcap.set(cv2.CAP_PROP_POS_MSEC,(count**100))
        ret,image = vidcap.read()
        cv2.imshow("res",image)
        
        count += 1
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
            cv2.destroyAllWindows()
vidcap.release()
cv2.destroyAllWindows()