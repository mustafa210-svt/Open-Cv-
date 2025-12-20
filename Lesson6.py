import cv2
import os
from PIL import Image 

#making a slideshow with 5 images
path = r"open cv images\slideshow images"
os.chdir(path) #change path's directory 

#calculating the mean of the images 
width = 0
height = 0
number_of_images = len(os.listdir(".")) #list all present directory  

for file in os.listdir("."):
    img = Image.open(file)
    w,h = img.size 
    width = width + w
    height = height + h

avg_height = height // number_of_images
avg_width = width // number_of_images

#resizing and saving images
for file in os.listdir("."):
    if file.endswith(".jpg") or file.endswith(".png") or file.endswith(".jpeg"):
        image = Image.open(file)
        resized_image = image.resize((avg_width,avg_height),Image.Resampling.LANCZOS)
        resized_image.save(file,"JPEG",quality = 95)

#preparing the slideshow
v_name = "Nature slideshow.avi"
images = []
for file in os.listdir("."):
    if file.endswith(".jpg") or file.endswith(".png") or file.endswith(".jpeg"):
        images.append(file)


frame = cv2.imread(images[0])
height,width,layers = frame.shape
video = cv2.VideoWriter(v_name,0,1,(width,height))
for image in images:
    video.write(cv2.imread(image))

cv2.destroyAllWindows()
video.release()

        
