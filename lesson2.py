import cv2 
import numpy as np
#reading images
building = cv2.imread(r"open cv images\buildings.jpg")
space = cv2.imread(r"open cv images\space.jpg")
diamond = cv2.imread(r"open cv images\diamond.jpg")
star = cv2.imread(r"open cv images\star.jpg")

#showing images
cv2.imshow("building", building)
cv2.imshow("space", space)

#adding images
combined = cv2.addWeighted(building,0.8,space,0.4,1)
cv2.imshow("combined image", combined)
#wait and destroy
cv2.waitKey(0)
cv2.destroyAllWindows()

#showing images
cv2.imshow("star",star)
cv2.imshow("diamond",diamond)

#subtracting images
subtracted = cv2.subtract(star,diamond)
cv2.imshow("subtracted images", subtracted)
#wait and destroy
cv2.waitKey(0)
cv2.destroyAllWindows()

#resizing images
car = cv2.imread(r"open cv images\car.jpeg",cv2.IMREAD_COLOR)
cv2.imshow("car",car)
resize = cv2.resize(car,dsize=(400,400))
cv2.imshow("car image resized",resize)
#wait and destroy
cv2.waitKey(0)
cv2.destroyAllWindows()



pika = cv2.imread(r"open cv images\pika.png",cv2.IMREAD_COLOR)
cv2.imshow("pika", pika)
#eroding
kernel = np.ones((5,5),np.uint8)
erode = cv2.erode(pika, kernel)
cv2.imshow("pika eroded", erode)
#wait and destroy
cv2.waitKey(0)
cv2.destroyAllWindows()
