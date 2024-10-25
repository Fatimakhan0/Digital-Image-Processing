#Program to read an image and display it in a plot

import cv2
import matplotlib.pyplot as plt

#Reading color image
img=cv2.imread("D:/7086/Resources/Mountain.jpg")

#Displaying image in plot
plt.imshow(img)
