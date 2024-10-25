#Program to Subplot an image by applying threshold and erosion method

import cv2
import numpy as np
import matplotlib.pyplot as plt

#Load the image and convert to greyscale
image=cv2.imread("D:/7086/Resources/Landscape.jpg")
gray=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(gray,70,255,cv2.THRESH_BINARY_INV)

kernel=np.ones((5,5),np.uint8)
print(kernel)

#Apply erosion
eroimg1=cv2.erode(thresh,kernel,iterations=1)
eroimg2=cv2.erode(thresh,kernel,iterations=2)
eroimg3=cv2.erode(thresh,kernel,iterations=3)

#Displaying the image
plt.subplot(231),plt.imshow(image,cmap='gray'),plt.title('Original image'),plt.axis('off')
plt.subplot(232),plt.imshow(thresh,cmap='gray'),plt.title('Thresholded image'),plt.axis('off')
plt.subplot(234),plt.imshow(eroimg1,cmap='gray'),plt.title('Erosion i = 1'),plt.axis('off')
plt.subplot(235),plt.imshow(eroimg2,cmap='gray'),plt.title('Erosion i = 2'),plt.axis('off')
plt.subplot(236),plt.imshow(eroimg3,cmap='gray'),plt.title('Erosion i = 3'),plt.axis('off')
plt.savefig("D:/7086/Resources/Erosion p160.png",format="png",dpi=1200)
plt.show()