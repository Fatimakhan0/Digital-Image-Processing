#Program to display the RGB channels in subplots of an image

import cv2
import matplotlib.pyplot as plt

#Reading color image
img=cv2.imread("D:/7086/Resources/rgbcircles.png")
rgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

plt.subplot(221),plt.imshow(rgb),plt.title("Original Image"),plt.axis("off")

r,g,b=cv2.split(rgb)

#Displaying image in plot

plt.subplot(222),plt.imshow(r,cmap='gray'),plt.title("Red Channel"),plt.axis("off")
plt.subplot(223),plt.imshow(g),plt.title("Green Channel"), plt.axis("off")
plt.subplot(224),plt.imshow(b),plt.title("Blue Channel"), plt.axis("off")
