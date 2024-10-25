#Program to display the image in a plot [RGB image]

import cv2
import matplotlib.pyplot as plt

#Reading color image
img2=cv2.imread("D:/7086/Resources/Google logo.jpg")

#Displaying image in plot
plt.imshow(img2)