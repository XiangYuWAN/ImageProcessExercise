import cv2
import numpy as np

img1 = cv2.imread("immed_gray_inv.pgm", cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread("immed_gray_inv_20051123_ero2.pgm", cv2.IMREAD_GRAYSCALE)
# ret,img = cv2.threshold(img1, 100, 1, cv2.THRESH_BINARY)
#this is a function of erode
i = 2
kernel = np.ones(shape=(2*i+1, 2*i+1))
def erode_image(image, kernel, ki):
    kernel_size = kernel.shape[0]
    image = np.array(image)
    if (kernel_size%2 == 0) or kernel_size<1:
        raise ValueError("kernel size must be odd and bigger than 1")
    if (image.max() != 255) or (image.min() != 0):
        raise ValueError("input image's pixel value must be grade")

    e_image = image.copy()
    center_move = int(ki)

    for i in range(center_move, image.shape[0]-kernel_size+1):
        for j in range(center_move, image.shape[1]-kernel_size+1):
            e_image[i, j] = np.min(image[i-center_move:i+center_move, j-center_move:j+center_move])
    return e_image

################
e_image = erode_image(img1, kernel, i)

difference = cv2.subtract(img2, e_image)
result = not np.any(difference)
print(result)
cv2.imshow("erode", e_image)
cv2.waitKey(0)
##################
'''
#Using OpenCv function
import cv2
import numpy as np
img1 = cv2.imread("immed_gray_inv.pgm",cv2.IMREAD_GRAYSCALE)
i = 1
kernel = np.ones((2*i+1,2*i+1), np.uint8)
erosion1 = cv2.erode(img1,kernel,iterations=1)

imgTest = cv2.imread("immed_gray_inv_20051123_ero1.pgm",cv2.IMREAD_GRAYSCALE)
difference = cv2.subtract(erosion1,imgTest)
result = not np.any(difference)
if result == True:
    print("erosion are same with ero1")
    cv2.imwrite("excersice_03a_output_01.pgm", erosion1)
else:
    print("erosion are not same")
######################################################
i = 2
kernel = np.ones((2*i+1,2*i+1), np.uint8)
erosion2 = cv2.erode(img1,kernel,iterations=1)

imgTest = cv2.imread("immed_gray_inv_20051123_ero2.pgm",cv2.IMREAD_GRAYSCALE)
difference = cv2.subtract(erosion2,imgTest)
result = not np.any(difference)
if result == True:
    print("erosion are same with ero2")
    cv2.imwrite("excersice_03a_output_02.pgm", erosion2)
else:
    print("erosion are not same")
'''
