#part 2 of face recognition software
#===================================
import cv2
import os 
import numpy as np 

#path variables
path = r"open cv images\face recognition"
haarfile = r"open cv images\face recognition\haarcascade_frontalface_default.xml"

images = []
labels = []
names = {}
id = 0

#walk function would look though everything in face recognition folder
for (subdirectories,directories,files) in os.walk(path):
    for directory in directories:
        names[id] = directory 
        path2 = os.path.join(path,directory)
        for file in os.listdir(path):
            imagePath = os.path.join(path2,file)
            readImage = cv2.imread(imagePath,0)
            images.append(readImage)
            labels.append(id)
        id = id + 1

(images,labels) = [np.array(lis) for lis in [images,labels]] #converting list into array for faster excution 
model = cv2.face.LBPHFaceRecognizer_create()
model.train(images,labels)
print("model trained succesfuly ")



            
    
    
