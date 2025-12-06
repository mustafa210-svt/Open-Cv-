import cv2
import numpy as np 

#transforming coloured image into grayscale
pika = cv2.imread(r"open cv images\pika.png",cv2.IMREAD_COLOR)
Grey_pika = cv2.cvtColor(pika, cv2.COLOR_BGR2GRAY) 
cv2.imshow("Normal pika", pika)
cv2.imshow("Grey pika", Grey_pika) 

#Wait and destroy
cv2.waitKey(0)
cv2.destroyAllWindows()

#Averaging of pixels method to grayscale image
(row,column) = pika.shape[0:2]

for r in range(row):
    for c in range(column):
       pika[r, c] = np.sum(pika[r, c], dtype=np.int32) * 0.3

cv2.imshow("average pika", (row,column))

#Wait and destroy
cv2.waitKey(0)
cv2.destroyAllWindows()

#rotating an image 
space = cv2.imread(r"open cv images\space.jpg") 
cv2.imshow("normal space",space) 
rows,coloumns = space.shape[0:2]
rotated_matrix = cv2.getRotationMatrix2D((coloumns/2, rows/2),90,1)
rotated_space = cv2.warpAffine(space,rotated_matrix , (coloumns,rows))
cv2.imshow("rotated space", rotated_space)

#Wait and destroy
cv2.waitKey(0)
cv2.destroyAllWindows()

#converting image from rgb to hsv
buildings = cv2.imread(r"open cv images\buildings.jpg")
cv2.imshow("normal buildings", buildings)

hsv = cv2.cvtColor(buildings,cv2.COLOR_BGR2HSV)
cv2.imshow("rgb to hsv buildings", hsv)

#Wait and destroy
cv2.waitKey(0)
cv2.destroyAllWindows()