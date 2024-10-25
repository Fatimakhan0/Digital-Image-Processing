#Program to obtain the dimensions of the image and change it to a greyscale image

#Import opencv
import cv2

#Load the input image
img=cv2.imread("D:/7086/Resources/flower.jpg")

#Get the dimensions of image
dimensions=img.shape

#height , width , number of channels in image
height=img.shape[0]
width=img.shape[1]
channels=img.shape[2]

print("Image Dimension :",dimensions)
print("Image Height :",height)
print("Image Width :",width)
print("Number of channels :",channels)

#Obtain the dimensions of the image array
#Using the shape method
(row,col)=img.shape[0:2]

#Take the average of pixel values of the BGR channels
#to convert the colored image to greyscale image
for i in range(row):
    for j in range(col):
        #Find the average of the BGR pixel values
        img[i,j]=sum(img[i,j])*0.33

cv2.imshow("Grayscale image",img)
cv2.waitKey(0)

#Window shown waits for any key pressing event
cv2.destroyAllWindows()
