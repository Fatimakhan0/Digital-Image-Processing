#Program to read an image and display the grayscale image

import cv2
img=cv2.imread("D:/7086/Resources/Hat1.jpg",cv2.IMREAD_GRAYSCALE)

#Displaying the image
cv2.imshow("Image",img)
cv2.waitKey(10000)

#Window shown waits for any key pressing event
cv2.destroyAllWindows()