#Sup and Inf
import cv2
import numpy as np
img1 = cv2.imread("image1.pgm", cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread("image2.pgm", cv2.IMREAD_GRAYSCALE)

irow = img1.shape[0]
icol = img1.shape[1]
imgSup = img1;
imgInf = img1;

# infimum of img1 and img2
for i in range(0, irow):
    for j in range(0, icol):
        imgInf[i,j] = min(img1[i,j], img2[i,j])


########################################
# test
imgTest = cv2.imread("image1_inf_image2.pgm",cv2.IMREAD_GRAYSCALE)
difference = cv2.subtract(imgInf,imgTest)
result = not np.any(difference)
if result == True:
    print("inf sucess!")
    cv2.imwrite("exercise_02c_output_02.pgm", imgInf)
else:
    print("failed")