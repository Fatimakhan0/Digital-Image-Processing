#Program to convert a colored image to binary image by applying thresholding techniques using matplotlib.pyplot

import cv2
import numpy as np
import matplotlib.pyplot as plt

#Load the input image
img = cv2.imread("D:/7086/Resources/flowers.jpg")
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

#To convert the image in grayscale
imgg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#Applying different thresholding with threshold value as 120
ret,thresh1 = cv2.threshold(imgg, 120, 255, 0)
ret,thresh2 = cv2.threshold(imgg, 120, 255, cv2.THRESH_BINARY_INV)
ret,thresh3 = cv2.threshold(imgg, 120, 255, cv2.THRESH_TRUNC)
ret,thresh4 = cv2.threshold(imgg, 120, 255, cv2.THRESH_TOZERO)
ret,thresh5 = cv2.threshold(imgg, 120, 255, cv2.THRESH_TOZERO_INV)

plt.subplot(131),plt.imshow(img,cmap='gray'),plt.title('Original Image'),plt.axis('off')
plt.subplot(132),plt.imshow(imgg,cmap='gray'),plt.title('Grayscale Image'),plt.axis('off')
plt.subplot(133),plt.imshow(thresh1,cmap='gray'),plt.title('Binary Image'),plt.axis('off')
plt.subplot(134),plt.imshow(thresh2,cmap='gray'),plt.title('Binary Inverted Image'),plt.axis('off')
plt.subplot(135),plt.imshow(thresh3,cmap='gray'),plt.title('Truncated Threshold Image'),plt.axis('off')
plt.subplot(136),plt.imshow(thresh4,cmap='gray'),plt.title('Set to 0 Image'),plt.axis('off')
plt.subplot(137),plt.imshow(thresh5,cmap='gray'),plt.title('Set to 0 Inverted Image'),plt.axis('off')

plt.show()