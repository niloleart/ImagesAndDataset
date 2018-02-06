import glob
import os
import cv2

newSize = 227
read_path = '/home/nil/PycharmProjects/ears/images/Ori/*.png'
write_path = '/home/nil/DATASETS/EAR_TRAIN_NoAspectRatio/train/images'

for image in glob.glob(read_path):
    print image
    a,b,c,d,e,f,g,image_name = image.split("/")
    img = cv2.imread(image)
    img = cv2.resize(img, (newSize, newSize))
    cv2.imwrite(os.path.join(write_path, image_name), img)
