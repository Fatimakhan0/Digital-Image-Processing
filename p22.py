#Program to implement Box Blur/ Mean filter to blur an image

#Importing required libraries
import cv2
import matplotlib.pyplot as plt

#Reading the input image
img= cv2.imread("D:/7086/Resources/flower.jpg")

#Convert BGR to RGBto display using matplotlib
imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

#Kernel size
ksize=(3,3)
#Using cv2.blur() method
k3blur=cv2.blur(imgRGB,ksize)

#Kernal size
ksize=(5,5)
#Using cv2.blur() method
k5blur=cv2.blur(imgRGB,ksize)

#Kernal size
ksize=(10,10)
#Using cv2.blur() method
k10blur=cv2.blur(imgRGB,ksize)

#Display Original and Box Blur images
plt.subplot(221),plt.imshow(imgRGB),plt.title("Original Image"),plt.axis('off')
plt.subplot(222),plt.imshow(k3blur),plt.title("Blur (k=3*3)"),plt.axis('off')
plt.subplot(223),plt.imshow(k5blur),plt.title("Blur (k=5*5)"),plt.axis('off')
plt.subplot(224),plt.imshow(k10blur),plt.title("Blur (k=10*10)"),plt.axis('off')
