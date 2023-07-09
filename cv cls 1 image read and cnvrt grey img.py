import cv2
"""
img1= cv2.imread("C:\\Users\\VICTORS\\Desktop\\Koenigsegg_Agera_N_.jpg",1)
#parameter 1 means print it originally, default value. RGB
img1= cv2.resize(img1,(1280,700))#width, height
# resize will here resize the image( with parameter (image,(width,height)))
print(img1)
cv2.imshow("original",img1)

img2 = cv2.imread("C:\\Users\\VICTORS\\Desktop\\Koenigsegg_Agera_N_.jpg",0)
# parameter 0 means display grey (black & White Image)
img2 = cv2.resize(img2,(1280,700))#width, height
cv2.imshow("Grey Scale Image",img2)
print("image in Grey Scale==\n",img2)


img3 = cv2.imread("C:\\Users\\VICTORS\\Desktop\\Koenigsegg_Agera_N_.jpg",-1)
# parameter 0 means display grey (black & White Image)
img3 = cv2.resize(img3,(1280,700))#width, height
cv2.imshow("Unchanged Image",img3)
print("image in Grey Scale==\n",img3)


cv2.waitKey()
# waitKey basically hold the output display.it takes parameter also in millisecond.
cv2.destroyAllWindows()
# saved memory for this file code will be destroyed after every execution.



###############################
# take input from user the image and path, convert it to grey , and save it.
path = input("enter the path and name of an image:  ")
print("you Enter this===",path)

im = cv2.imread(path,0)
im = cv2.resize(im,(560,700))
cv2.imshow("converted image==",im)

k= cv2.waitKey()
if k == ord("s"):
    cv2.imwrite("C:\\Users\\VICTORS\\Downloads\\output.jpg",im)
else:
    cv2.destroyAllWindows()

#store/save 
"""
img1 = cv2.imread("C:\\Users\\VICTORS\\Downloads\\Koenigsegg_Agera_N_.jpg",0)
img1 = cv2.resize(img1, (560,700))
img1 = cv2.flip(img1, -1)# it accept parameter as -0,0,1
cv2.imshow("flipped",img1)
cv2.waitKey()
cv2.destroyAllWindows()