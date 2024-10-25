#Program to generate a random image and save it in the folder

#Load the image
import cv2
import numpy as np

#Randomly generate an image within the given dimensions
grey_img=np.random.randint(255,size=(300,600,3))
isWritten=cv2.imwrite("D:/7086/Outputs/p10.png",grey_img)

#Save the image after it is successfully generated
if isWritten:
    print("The image is successfully saved.")