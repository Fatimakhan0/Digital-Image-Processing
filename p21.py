#Program to implement Average / Mean filter to blur an image

#Importing required libraries
import cv2
import numpy as np
import matplotlib.pyplot as plt

#Reading the input image
img= cv2.imread("D:/7086/Resources/ice cream.jpeg")
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

#Displaying the original image
plt.imshow(img)

#Blurring the image
img=cv2.blur(img(3,3))

#Dispalying the blur image
plt.imshow(img)



