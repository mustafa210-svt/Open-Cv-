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
resize = cv2.resize(car,(400,400))
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

#addon
resize1 = cv2.resize(space,(500,500))
resize2 = cv2.resize(star,(500,500))
combined1 = cv2.addWeighted(resize1,0.6,resize2,0.3,1)
cv2.imshow("combined image 1", combined1)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Bordering
Space = cv2.imread(r"open cv images\space.jpg")
Bordered_image = cv2.copyMakeBorder(Space, 6,6,5,5,cv2.BORDER_CONSTANT,value= (128,128,0))
cv2.imshow("Bordered space image", Bordered_image)
#Bordering car image
Bordered_space= cv2.copyMakeBorder(Space,7,7,5,5,cv2.BORDER_REFLECT)
cv2.imshow("Bordered space image 2", Bordered_space)
#Wait and destroy
cv2.waitKey(0)
cv2.destroyAllWindows()

#Image blurring 

#gaussian Blur
cv2.imshow("Normal pika",pika)
Gaussian_pika = cv2.GaussianBlur(pika, (7,7), 0)
cv2.imshow("Gaussian blurred pika", Gaussian_pika)

#median Blur
Median_pika = cv2.medianBlur(pika,9)
cv2.imshow("Median blurred pika", Median_pika)

#Bilateral blur
Bilateral_pika = cv2.bilateralFilter(pika,9,75,75)
cv2.imshow("Bilateral blurred pika", Bilateral_pika)


#Wait and destroy
cv2.waitKey(0)
cv2.destroyAllWindows()
