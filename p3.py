#Program to change the name of the image and save it

#Load the image
import cv2
img1=cv2.imread("D:/7086/Resources/Iceberg.jpg")

#Displaying the image
cv2.imshow("Nature",img1)
cv2.imwrite("D:/7086/Resources/Iceberg11.jpg",img1)
cv2.waitKey(10000)

#Window shown waits for any key pressing event
cv2.destroyAllWindows()