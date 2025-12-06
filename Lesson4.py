import cv2

#drawing a line on an image
space = cv2.imread(r"open cv images\space.jpg")
#properties of the line
start_point = 0,100 
end_point = 600,100
color = 0,0,255
thickness = 8
#drawing line
space_l = cv2.line(space,start_point,end_point,color,thickness)
cv2.imshow("space image with a line", space)
#Wait and destroy
cv2.waitKey(0)
cv2.destroyAllWindows()

#drawing a rectangle on an image
#properties for the rectangle
color = 123,78,140
thickness = -1
topleft = 20,130
bottomright = 60,200
#drawing the rectangle
space_r = cv2.rectangle(space, topleft,bottomright,color,thickness)
cv2.imshow("rectangle in space", space_r)
#Wait and destroy
cv2.waitKey(0)
cv2.destroyAllWindows()

