#DFT

#Importing the required libraries
import cv2
import numpy as np


#Load the image and convert to grayscale
img=cv2.imread("D:/7086/Resources/flowers.jpg")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#Compute the DIscrete Fourier Transformation of the image
#Compare numpy array to float32
#cv2.dft() functional 3D numpy array of shape
#The output of 2D fourier Transform is a 2D complex array
#The first and second channel of the f are the real and imaginary parts respectively
#F complex =

fourier=cv2.dft(np.float32(gray),flags=cv2.DFT_COMPLEX_OUTPUT)

#Calculate the magnitude of the fourier transform
#Take the log of absolute value as it has wide range
magnitude=20*np.log(cv2.magnitude(fourier[:,:,0],fourier[:,:,1]))

#Scale the magnitude for diaplay
#Constraint the range from 0 to 255
magnitude=cv2.normalize(magnitude,None,0,255,cv2.NORM_MINMAX,cv2.CV_8UC1)

#Inverse DFT
idft=cv2.idft(fourier)

#Calculate the magnitude of the Inverse Fourier Transform
imag=20*np.log(cv2.magnitude(idft[:,:,0],idft[:,:,1]))

#Scale the magnitude for display
imagnorm=cv2.normalize(imag,None,0,255,cv2.NORM_MINMAX,cv2.CV_8UC1)

#Display the magnitude of the Fourier Transform
cv2.imshow("Original Image",gray)
cv2.imshow("Fourier Transform",magnitude)
cv2.imshow("Magnitude Spectrum",imagnorm)
cv2.waitKey(0)
cv2.destroyAllWindows()