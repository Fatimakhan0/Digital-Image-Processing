#Program to implement Gaussian filter and display in matplotlib

#Importing required libraries
import cv2
import matplotlib.pyplot as plt

#Load the input image 
img=cv2.imread("D:/7086/Resources/flowers.jpg")
RGB_img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
plt.imshow(RGB_img)

#Converting to grayscale
gray=cv2.cvtColor(RGB_img,cv2.COLOR_BGR2GRAY)

#Remove noise
img=cv2.GaussianBlur(gray, (3,3), 0)

#Convolute with sobel kernels
sobelx=cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5) #x
sobely=cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5) #y

#Plotting images alternatively

print("Sobel operator on X-axis")
plt.imshow(sobelx)


print("Sobel operator on Y-axis")
plt.imshow(sobely)
