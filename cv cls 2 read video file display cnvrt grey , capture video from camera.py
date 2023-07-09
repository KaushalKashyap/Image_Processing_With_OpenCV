import cv2
"""
# program to read video file and display it with frame resize and 
cap = cv2.VideoCapture("C:\\Users\\VICTORS\\Downloads\\cv\\Course Resources and Study Material _ Image Processing and Computer Vision _ Github_.mp4")
print("cap",cap)

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame,(700,450))
    cv2.imshow("frame",frame)
    k= cv2.waitKey(25) #here parameter contains as playback speed. less value more speed. more value less speed.
    if k == ord("q"):# by pressing 'q', it window of video will be closed.
        break
#sometime ord() keyword didn't work, then try this:
# if k== ord("q")& 0xFF:   '0xFF' is nothing but a mask which refine code.
    #break
cap.release()
cv2.destroyAllWindows()
"""
"""
# convert video into grayscale.
cap = cv2.VideoCapture("C:\\Users\\VICTORS\\Downloads\\cv\\Course Resources and Study Material _ Image Processing and Computer Vision _ Github_.mp4")
print("cap",cap)

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, (700,450))
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow("frame",frame)
    cv2.imshow("gray",gray)
    k = cv2.waitKey(25)
    if k == ord("q") & 0xFF:
        break
cap.release()
cv2.destroyAllWindows()
"""
"""
# program to capture video and save it.
cap = cv2.VideoCapture(0) # for inbuilt camera 0 and for external camera 1

#DIVX, XVID, MJPG, X264, WMV1, WMV2
fourcc = cv2.VideoWriter_fourcc(*"XVID") 
#it contain 4 parameter name, codec,fps, resolution.
output = cv2.VideoWriter("C:\\Users\\VICTORS\\Downloads\\output.avi", fourcc, 20.0,(640,480),0)

print("cap",cap)

while cap.isOpened():
    ret, frame = cap.read()
    if ret == True:
        
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow("frame",frame)
        cv2.imshow("gray",gray)
        output.write(gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
cap.release()
output.release()
cv2.destroyAllWindows()

"""
