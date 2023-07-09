"""
# Draw Date time and figures on Video
import datetime
import cv2

cap = cv2.VideoCapture("C:\\Users\\VICTORS\\Downloads\\cv\\Course Resources and Study Material _ Image Processing and Computer Vision _ Github_.mp4")

print("For Width===",cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print("For HEIGHT===",cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
# IN SHORT FORM YOU CAN ALSO WRITE
#print("For Width===",cap.get(3)) # HERE 3 DENOTE FOR WIDTH
#print("For HEIGHT===",cap.get(4)) # HERE 4 DENOTE FOR HEIGHT

while (cap.isOpened()):
    ret, frame = cap.read()
    frame = cv2.resize(frame, (800,650))
    if ret == True:
        font = cv2.FONT_HERSHEY_COMPLEX_SMALL
        text = 'Height: ' +str(cap.get(4))+ ' Width' + str(cap.get(3))
        frame = cv2.putText(frame, text, (10,20),font,1,(0,155,255),1,cv2.LINE_AA)
        date_data = "Date: "+str(datetime.datetime.now())
        frame = cv2.putText(frame, date_data, (20,50), font, 1,(100,255,255),1,cv2.LINE_AA)
        
        cv2.imshow('frame', frame)
        
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()

"""
# draw the same shape thing on webcam
import datetime
import cv2

cap = cv2.VideoCapture(0)

print("For Width===",cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print("For HEIGHT===",cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
# IN SHORT FORM YOU CAN ALSO WRITE
#print("For Width===",cap.get(3)) # HERE 3 DENOTE FOR WIDTH
#print("For HEIGHT===",cap.get(4)) # HERE 4 DENOTE FOR HEIGHT

while (cap.isOpened()):
    ret, frame = cap.read()
    frame = cv2.resize(frame, (800,650))
    if ret == True:
        font = cv2.FONT_HERSHEY_COMPLEX_SMALL
        text = 'Height: ' +str(cap.get(4))+ ' Width' + str(cap.get(3))
        frame = cv2.putText(frame, text, (10,20),font,1,(0,155,255),1,cv2.LINE_AA)
        date_data = "Date: "+str(datetime.datetime.now())
        frame = cv2.putText(frame, date_data, (20,50), font, 1,(100,255,255),1,cv2.LINE_AA)
        
        cv2.imshow('frame', frame)
        
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()