#Program to read an image and convert it from BGR to RGB

import cv2
img=cv2.imread("D:/7086/Resources/Google logo.jpg")
rgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

#Displaying the image
cv2.imshow("Image BGR",img)
cv2.imshow("Image RGB",rgb)
cv2.waitKey(0)

#Window shown waits for any key pressing event
cv2.destroyAllWindows()