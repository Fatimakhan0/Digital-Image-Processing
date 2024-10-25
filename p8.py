#Program to generate three images randomly of different ranges

import cv2
import numpy as np

#image range 150 = neither too bright nor too dark
grey_img=np.random.randint(150,size=(300,600,3))

#image range 1 = dark image
dark_img=np.random.randint(1,size=(300,600,3))

#image range 300 = bright image
bright_img=np.random.randint(300,size=(300,600,3))

#Save the images successfully
isWritten=cv2.imwrite("D:/7086/Resources/New0.png",grey_img)
isWritten=cv2.imwrite("D:/7086/Resources/New1.png",dark_img)
isWritten=cv2.imwrite("D:/7086/Resources/New2.png",bright_img)

#if the images have been saved, print the following statement
if isWritten:
    print("The image is successfully saved.")