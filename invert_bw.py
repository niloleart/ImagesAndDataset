import os
import cv2 as cv
import glob

DATASET_DIR = '/home/nil/Desktop/Masks/*.png'
RESULTS_DIR = '/home/nil/Desktop/Masks_OK/'

if not os.path.exists(RESULTS_DIR):
    os.makedirs(RESULTS_DIR)

for image in glob.glob(DATASET_DIR):
    img = cv.imread(image)
    a,b,c,d,e,image_name = image.split("/")
    img_ok = 255 - img
    cv.imwrite(os.path.join(RESULTS_DIR, image_name), img_ok)