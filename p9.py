#Program to convert the image into RGB

import numpy as np
from PIL import Image
img = Image.OPEN("D:/7086/Outputs/p5.png")
red_image_rgb = img.convert("RGB")
rgb_pixel_value=red_image_rgb.getpixel((10,15))
print(rgb_pixel_value)