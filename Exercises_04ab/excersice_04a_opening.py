import cv2
import  numpy as np

img1 = cv2.imread("immed_gray_inv.pgm", cv2.IMREAD_GRAYSCALE)
i = 1
#i = 2
kernel = np.ones((2*i+1,2*i+1), np.uint)
# openning : dilation(erosion)
erosion = cv2.erode(img1,kernel,iterations=1)
openning1 = cv2.dilate(erosion,kernel,iterations=1)
# test
imgTest = cv2.imread("immed_gray_inv_20051123_ope1.pgm",cv2.IMREAD_GRAYSCALE)
difference = cv2.subtract(openning1,imgTest)
result = not np.any(difference)
if result == True:
    print("opening1 are same with open1")
    cv2.imwrite("excersice_04a_output_01.pgm", openning1)
else:
    print("opening1 are not same")

# cv2.imshow("output.png", openning)
# cv2.waitKey(0)


#######################################################################
i = 2
kernel = np.ones((2*i+1,2*i+1), np.uint)
# openning : dilation(erosion)
erosion = cv2.erode(img1,kernel,iterations=1)
openning2 = cv2.dilate(erosion,kernel,iterations=1)

imgTest = cv2.imread("immed_gray_inv_20051123_ope2.pgm",cv2.IMREAD_GRAYSCALE)
difference = cv2.subtract(openning2,imgTest)
result = not np.any(difference)
if result == True:
    print("opening2 are same with open2")
    cv2.imwrite("excersice_04a_output_02.pgm",openning2)
else:
    print("opening2 are not same")
