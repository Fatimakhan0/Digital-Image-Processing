#Program to implement erosion and dilation on an image

#Importing required libraries
import cv2
import numpy as np

#Reading the input image
img=cv2.imread("D:/7086/Resources/flowers.jpg",1)
#Loads the image as grayscale

#Define the structure of the element
kernel=np.ones((5,5),np.uint8)

#Perform dilation
dilation=cv2.dilate(img,kernel,iterations=1)

#Display results
cv2.imshow("Original",img)
cv2.imshow("Dilation",dilation)

#Perform erosion
erosion=cv2.erode(img,kernel,iterations=1)

#Display results
cv2.imshow("Original",img)
cv2.imshow("Erosion",erosion)
cv2.waitKey(0)
cv2.destroyAllWindows()