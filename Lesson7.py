import cv2
import numpy as np

#capturing image
video = cv2.VideoCapture(r"open cv images\video.mp4")
background = 0
#reading the background image from video
for i in range(10):
    return_value,background = video.read()
    if return_value == False:
        continue

#flipping backgroud image along the xy axis
background = np.flip(background,axis= 1)

#checking for red pixels
while(video.isOpened()):
    return_value,image = video.read()
    if return_value == False:
        continue
    image = np.flip(image,axis= 1)
    hsv = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)      

    lower_red1 = np.array([100,40,40])
    upper_red1 = np.array([100,255,255])
    mask1 = cv2.inRange(hsv,lower_red1,upper_red1)

    lower_red2 = np.array([155,40,40])
    upper_red2 = np.array([180,255,255])
    mask2 = cv2.inRange(hsv,lower_red2,upper_red2)

    mask1 = mask1 + mask2

    mask1 = cv2.morphologyEx(mask1,cv2.MORPH_OPEN,np.ones((3,3), np.uint8),iterations= 2)
    mask1 = cv2.dilate(mask1,np.ones((3,3),np.uint8), iterations= 1)
    mask2 = cv2.bitwise_not(mask1)
    
    result1 = cv2.bitwise_and(background,background,mask= mask1)
    result2 = cv2.bitwise_and(image,image,mask= mask2)

    combined = cv2.addWeighted(result1,1,result2,1,0)
    cv2.imshow("Combined images",combined)
    key = cv2.waitKey(10)
    if key == 27: 
        break







    