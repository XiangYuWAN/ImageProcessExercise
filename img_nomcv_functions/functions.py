import cv2
import numpy as np
# define a method of compare
def img_compare(img1, img2):
    row1 = img1.shape[0]
    col1 = img1.shape[1]
    compare = True
    for i in range(0, row1):
        for j in range(0, col1):
            if img2[i, j] != img1[i, j]:
                compare = False
    return compare