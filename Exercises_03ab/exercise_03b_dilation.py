import cv2
import numpy as np
img1 = cv2.imread("immed_gray_inv.pgm", cv2.IMREAD_GRAYSCALE)
i = 1
kernel = np.ones((2*i+1,2*i+1),np.uint8)
dilation1 = cv2.dilate(img1,kernel)

imgTest = cv2.imread("immed_gray_inv_20051123_dil1.pgm",cv2.IMREAD_GRAYSCALE)
difference = cv2.subtract(dilation1,imgTest)
result = not np.any(difference)
if result == True:
    print("dilation are same with dia1")
    cv2.imwrite("excersice_03b_output_01.pgm", dilation1)
else:
    print("dilation are not same")

i = 2
kernel = np.ones((2*i+1,2*i+1), np.uint8)
dilation2 = cv2.dilate(img1,kernel)

imgTest = cv2.imread("immed_gray_inv_20051123_dil2.pgm",cv2.IMREAD_GRAYSCALE)
difference = cv2.subtract(dilation2,imgTest)
result = not np.any(difference)
if result == True:
    print("dilation are same with dia2")
    cv2.imwrite("excersice_03b_output_02.pgm", dilation2)
else:
    print("dilation are not same")
