import cv2

image = cv2.imread(r"open cv images\pika.png",cv2.IMREAD_COLOR)
cv2.imshow("Pika image coloured", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

image = cv2.imread(r"open cv images\pika.png",cv2.IMREAD_GRAYSCALE)
cv2.imshow("Pika image grayscale", image)
cv2.waitKey(0)




image = cv2.imread(r"open cv images\pika.png",cv2.IMREAD_UNCHANGED)
cv2.imshow("Pika image unchanged", image)
cv2.waitKey(0)

