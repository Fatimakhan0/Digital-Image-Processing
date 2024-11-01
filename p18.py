#Program to convert a colored image to binary image using matplotlib.pyplot

import cv2
import matplotlib.pyplot as plt

#Load the input image
image=cv2.imread("D:/7086/Resources/ice cream.jpeg")

#Convert BGR to RGB using matplotlib
image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)

#Convert colored image to Grayscale image
gray_image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)


#Convert the image to a binary image
ret,thresh = cv2.threshold(gray_image, 170, 255, 0)

#Displaying the original , grayscale and binary image in subplots
plt.subplot(131),plt.imshow(image,cmap='gray'),plt.title('Original image'),plt.axis('off')
plt.subplot(132),plt.imshow(gray_image,cmap='gray'),plt.title('Grayscale image'),plt.axis('off')
plt.subplot(133),plt.imshow(thresh,cmap='gray'),plt.title('Binary image'),plt.axis('off')
plt.show()