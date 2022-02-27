import cv2
import  numpy as np

img1 = cv2.imread("immed_gray_inv.pgm", cv2.IMREAD_GRAYSCALE)
i = 1
kernel = np.ones((2*i+1,2*i+1), np.uint)
# closing : erosion(dilation)
dilation = cv2.dilate(img1,kernel,iterations=1)
closing1 = cv2.erode(dilation,kernel,iterations=1)
# test
imgTest = cv2.imread("immed_gray_inv_20051123_clo1.pgm",cv2.IMREAD_GRAYSCALE)
difference = cv2.subtract(closing1,imgTest)
result = not np.any(difference)
if result == True:
    print("closing1 are same with clo1")
    cv2.imwrite("excersice_04b_output_01.pgm", closing1)
else:
    print("closing1 are not same")


#######################################################################

i = 2
kernel = np.ones((2*i+1,2*i+1), np.uint)
# closing : erosion(dilation)
dilation = cv2.dilate(img1,kernel,iterations=1)
closing2 = cv2.erode(dilation,kernel,iterations=1)
# test
imgTest = cv2.imread("immed_gray_inv_20051123_clo2.pgm",cv2.IMREAD_GRAYSCALE)
difference = cv2.subtract(closing2,imgTest)
result = not np.any(difference)
if result == True:
    print("closing1 are same with clo2")
    cv2.imwrite("excersice_04b_output_02.pgm", closing2)
else:
    print("closing2 are not same")
