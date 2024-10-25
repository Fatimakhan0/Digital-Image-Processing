#Program to read an image and display it

#Load the image
import cv2
img1=cv2.imread("D:/7086/Resources/ice cream.jpeg")

#Displaying the image
cv2.imshow("Ice Cream",img1)
cv2.waitKey(0)

#Window shown waits for any key pressing event
cv2.destroyAllWindows()