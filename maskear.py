from os import listdir
import os
from os.path import isfile, join
import numpy
import cv2

DATASET_DIR = '../../DATASET'
AUGMENTED_DIR = '../../DATASET/Augmented/'
MASK_SOURCE = '../DATASET/TruthMask'
RESULTS_DIR = '../../DATASET/Augmented_Mask'

imglist = []
for dirName, subdirList, fileList in os.walk(AUGMENTED_DIR):
    for sub in subdirList:
        print sub
        for img in fileList:
            print img
            imatge = cv2.imread(os.join(AUGMENTED_DIR,sub,img))
            print imatge
            imglist.append(imatge)






