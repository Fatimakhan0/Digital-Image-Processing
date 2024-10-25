#Program to read an image and print it as a color image

#Load the image
import cv2
img=cv2.imread("D:/7086/Resources/flower.jpg", cv2.IMREAD_COLOR)

#Displaying the image
cv2.imshow("Image",img)
cv2.waitKey(10000)

#Window shown waits for any key pressing event
cv2.destroyAllWindows()