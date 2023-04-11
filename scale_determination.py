import matplotlib.pyplot as plt
import numpy as np
import cv2 as cv

image_name =  r"C:\Users\edoua\Desktop\Soft Robotics\Python Bending\Images_Bis\0.jpg"

img = cv.imread(image_name)
height, width = img.shape[:2]
scale_percent = 40
# Calculer les nouvelles dimensions de l'image
new_width = int(width * scale_percent / 100)
new_height = int(height * scale_percent / 100)
dim = (new_width, new_height)

# Redimensionner l'image
resized = cv.resize(img, dim, interpolation = cv.INTER_AREA)

print(resized.shape)
cv.imshow('Initial_Picture',resized)

img_crop_scale = resized[225:680,0:102]
cv.imshow("Cropped_Picture_scale",img_crop_scale)

print(img_crop_scale.shape)


