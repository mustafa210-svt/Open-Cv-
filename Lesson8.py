import cv2 

face_folder = r"open cv images\face recognition"
haarfile = r"open cv images\face recognition\haarcascade_frontalface_default.xml"

webcam = cv2.VideoCapture(0)
facecascade = cv2.CascadeClassifier(haarfile)

count = 1
while count <= 30:
    returnvalue,image = webcam.read()
    if returnvalue == False:
        continue

    greyscale = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    faces = facecascade.detectMultiScale(greyscale,1.3,3)
    
    for face in faces:
        x,y,w,h = face
        cv2.rectangle(image,(x,y),(x+w,y+h),color= "Red",thickness= 3)
        face = greyscale[x:x+w, y:y+h]
        resizeFace = cv2.resize(face,(130,100))
        cv2.imwrite("%s/%s.png"(face_folder,count), resizeFace )
    count = count + 1

    cv2.imshow("Face image",image)
    key = cv2.waitKey(10)
    if key == 27:
        break 






        














