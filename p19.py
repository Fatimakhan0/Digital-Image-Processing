#Program to convert a colored image to binary image by applying thresholding techniques

import cv2
import numpy as np

#Load the input image
img = cv2.imread("D:/7086/Resources/flowers.jpg")

#To convert the image in grayscale
imgg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#Applying different thresholding with threshold value as 120
ret,thresh1 = cv2.threshold(imgg, 120, 255, cv2.THRESH_BINARY)
ret,thresh2 = cv2.threshold(imgg, 120, 255, cv2.THRESH_BINARY_INV)
ret,thresh3 = cv2.threshold(imgg, 120, 255, cv2.THRESH_TRUNC)
ret,thresh4 = cv2.threshold(imgg, 120, 255, cv2.THRESH_TOZERO)
ret,thresh5 = cv2.threshold(imgg, 120, 255, cv2.THRESH_TOZERO_INV)

#The window showing output images
cv2.imshow("Binary Threshold",thresh1)
cv2.imshow("Binary Threshold Inverted",thresh2)
cv2.imshow("Truncated Threshold",thresh3)
cv2.imshow("Set to 0",thresh4)
cv2.imshow("Set to 0 Inverted",thresh5)

cv2.waitKey(0)
cv2.destroyAllWindows()