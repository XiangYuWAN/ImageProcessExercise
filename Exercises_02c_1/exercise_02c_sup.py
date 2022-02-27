#Sup and Inf
import numpy as np
import cv2
img1 = cv2.imread("image1.pgm", cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread("image2.pgm", cv2.IMREAD_GRAYSCALE)

irow = img1.shape[0]
icol = img1.shape[1]
imgSup = img1;
imgInf = img1;

# supremum of img1 and img2
for i in range(0, irow):
    for j in range(0, icol):
        imgSup[i,j] = max(img1[i,j], img2[i,j])


#####################################################
#test
imgTest = cv2.imread("image1_sup_image2.pgm",cv2.IMREAD_GRAYSCALE)
difference = cv2.subtract(imgSup,imgTest)
result = not np.any(difference)
if result == True:
    print("sup sucess!")
    cv2.imwrite("exercise_02c_output_01.pgm", imgSup)
else:
    print("failed")