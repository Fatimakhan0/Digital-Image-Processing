#DCT

#Importing the required libraries
import cv2
import numpy as np

#Load the image and convert to grayscale
image=cv2.imread("D:/7086/Resources/flowers.jpg")
gray=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#Compute the Discrete Cosine Transform of the image
dctimg=cv2.dct(np.float32(gray),cv2.DCT_INVERSE)

#Inverse DCT
idctimg=cv2.idct(dctimg)

#Convert to uint8
idct=np.uint8(idctimg)

#Display the results
cv2.imshow("Original Image", gray)
cv2.imshow("Cosine Transform", dctimg)
cv2.imshow("Inverse Cosine Transform", idct)
cv2.waitKey(0)
cv2.destroyAllWindows()
