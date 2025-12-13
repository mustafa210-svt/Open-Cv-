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

#drawing a circle on an image
#properties for circle
color = 154,87,50
thickness = -1
radius = 30
centre_coords = 400,200
#drawing the circle
space_c = cv2.circle(space, centre_coords,radius,color,thickness)
cv2.imshow("circle in space", space_c)
#Wait and destroy
cv2.waitKey(0)
cv2.destroyAllWindows()

#typing text on an image
#properties for text
text = "Hello,world"
thickness = 4
color = 155,170,125
topleft = 80, 80
fontstyle = cv2.FONT_HERSHEY_DUPLEX
fontscale = 2
#typing text 
space_t = cv2.putText(space, text,topleft,fontstyle,fontscale,color,thickness,cv2.LINE_AA)
cv2.imshow("Text in space", space_t)
#Wait and destroy
cv2.waitKey(0)
cv2.destroyAllWindows()