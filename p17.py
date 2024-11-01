#Program to convert a colored image to binary image

#Import required libraries
import cv2
import matplotlib.pyplot as plt

#Load the inpuit image
image=cv2.imread("D:/7086/Resources/ice cream.jpeg")

#Convert BGR to RGB using matplotlib
image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)

#Displaying the image
plt.imshow(image)

#Convert colored image to Grayscale image
gray_image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

#Display the grayscale image
plt.imshow(gray_image, cmap="gray")

#Convert the image to a binary image
(thresh, binary_image) = cv2.threshold(gray_image, 175, 255, cv2.THRESH_BINARY)

#Display the binary image
plt.imshow(binary_image, cmap = "gray")