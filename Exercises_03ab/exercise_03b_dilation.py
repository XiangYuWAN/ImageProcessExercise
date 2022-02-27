import cv2
import numpy as np

img1 = cv2.imread("immed_gray_inv.pgm", cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread("immed_gray_inv_20051123_dil2.pgm", cv2.IMREAD_GRAYSCALE)
# ret,img = cv2.threshold(img1, 100, 1, cv2.THRESH_BINARY)
#this is a function of erode
i = 2
kernel = np.ones(shape=(2*i+1, 2*i+1))
def dilate_image(image, kernel, ki):
    kernel_size = kernel.shape[0]
    image = np.array(image)
    if (kernel_size%2 == 0) or kernel_size<1:
        raise ValueError("kernel size must be odd and bigger than 1")
    if (image.max() != 255) or (image.min() != 0):
        raise ValueError("input image's pixel value must be grade")

    d_image = image.copy()
    center_move = int(ki)

    for i in range(center_move, image.shape[0]-kernel_size+1):
        for j in range(center_move, image.shape[1]-kernel_size+1):
            d_image[i, j] = np.max(image[i-center_move:i+center_move, j-center_move:j+center_move])
    return d_image

################
d_image = dilate_image(img1, kernel, i)

difference = cv2.subtract(d_image, img2)
result = not np.any(difference)
print(result)
cv2.imshow("dilate", d_image)
cv2.waitKey(0)
##################

'''
#using opencv function
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
'''