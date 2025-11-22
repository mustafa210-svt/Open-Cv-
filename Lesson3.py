import cv2

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
        pika[r,c] = sum(pika[r,c]) * 0.33

cv2.imshow("average pika", (row,column))

#Wait and destroy
cv2.waitKey(0)
cv2.destroyAllWindows()

    