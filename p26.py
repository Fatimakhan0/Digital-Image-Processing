#Program to compare bilateral filtering and box filter and display in matplotlib

#Importing required libraries
import cv2
import matplotlib.pyplot as plt

#Load the input image 
img=cv2.imread("D:/7086/Resources/flowers.jpg")

#Convert BGR to RGB to display using matplotlib
imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

#Apply bilateral blur with d=5,sigma=75
Billmg=cv2.bilateralFilter(imgRGB, 5, 75, 75)

#Aplply box blur with k=5
k5blur = cv2.blur(imgRGB,(5,5))

plt.subplot(131),plt.imshow(imgRGB),plt.title("Original Image"),plt.axis('off')
plt.subplot(132),plt.imshow(Billmg),plt.title("Bilateral Blur d=5"),plt.axis('off')
plt.subplot(133),plt.imshow(k5blur),plt.title("Box Blur k=5"),plt.axis('off')