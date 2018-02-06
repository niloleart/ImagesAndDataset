import cv2 as cv
import numpy as np
import os

src = '/home/nil/PycharmProjects/ears/less_images/3100.png'
dst = '/home/nil/Desktop/'

img = cv.imread(src)
h, w, channels = img.shape
large_edge = max(img.shape[:2])
small_edge = min(img.shape[:2])
black_image = np.zeros((large_edge,large_edge,3), np.uint8)
pos = large_edge - (small_edge + int(round(large_edge-small_edge)/2))
print pos

for c in range(0, 3):
    black_image[0:h,pos:pos+w,c] = black_image[0:h,pos:pos+w,c] + img[:,:,c]

