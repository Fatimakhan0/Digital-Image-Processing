#Program to read an image and save it in either color format or grayscale format

import cv2
import numpy as np

imgc=cv2.imread("D:/7086/Resources/ice cream.jpeg")
imgg=cv2.imread("D:/7086/Resources/ice cream.jpeg",cv2.IMREAD_GRAYSCALE)

#Displaying the image
cv2.imshow("D:/7086/Resources/ice cream.jpeg",imgc)

#Storing the key pressed by the user
k=cv2.waitKey(0)

#Check if user hit 'c' or 'g' key
if (k==ord('c')):
    cv2.imwrite("D:/7086/Resources/ice cream c.jpeg",imgc)
    print("Color image is saved.")
    cv2.destroyAllWindows()

if (k==ord('g')):
    cv2.imwrite("D:/7086/Resources/ice cream g.jpeg",imgg)
    print("Greayscale image is saved.")
    cv2.destroyAllWindows()