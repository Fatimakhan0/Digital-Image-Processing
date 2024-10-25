#Program to read RGB pixel value of whole image

import numpy as np
from PIL import Image

#Read an image file
img=Image.open("D:/7086/Resources/Forest.jpg")

#Create a PIL image object
image_rgb=img.convert("RGB")

#Convert to RGB colorspace
rgb_pixel_value=image_rgb.getpixel((10,15))

#Get width and height of image
width,height=image_rgb.size

#Iterate through all pixels of image and get R,G,B values from that
for x in range(0,width):
    for y in range(0,height):
        r,g,b=image_rgb.getpixel((x,y))
        print(image_rgb.getpixel((x,y)))