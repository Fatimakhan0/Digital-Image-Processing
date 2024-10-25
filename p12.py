#Program to read Rgb pixel value at any location

import numpy as np
from PIL import Image

#Read an image file
img=Image.open("D:/7086/Resources/flowers.jpg")

#Create a PIL image object
red_image_rgb=img.convert("RGB")

#Convert to RGB colorspace
rgb_pixel_value=red_image_rgb.getpixel((10,15))

#Get color from (x,y) coordinates
print(rgb_pixel_value)
