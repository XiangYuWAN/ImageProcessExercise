import cv2
import numpy as np
img1 = cv2.imread("immed_gray_inv.pgm", cv2.IMREAD_GRAYSCALE)
ret,img = cv2.threshold(img1, 100, 1, cv2.THRESH_BINARY)
# print(type(img1))
# print(type(img))
# cv2.imshow("asd", img)
# cv2.waitKey(0) # waiting for a key
i =2
kernel = np.ones(shape=(2*i+1, 2*i+1))
def erode_bin_image(bin_image, kernel):
    """
    erode bin image
    Args:
        bin_image: image with 0,1 pixel value
    Returns:
        erode image
    """
    kernel_size = kernel.shape[0]
    bin_image = np.array(bin_image)
    if (kernel_size%2 == 0) or kernel_size<1:
        raise ValueError("kernel size must be odd and bigger than 1")
    if (bin_image.max() != 1) or (bin_image.min() != 0):
        raise ValueError("input image's pixel value must be 0 or 1")
    d_image = np.zeros(shape=bin_image.shape)
    center_move = int((kernel_size-1)/2)
    for i in range(center_move, bin_image.shape[0]-kernel_size+1):
        for j in range(center_move, bin_image.shape[1]-kernel_size+1):
            d_image[i, j] = np.min(bin_image[i-center_move:i+center_move,
                                             j-center_move:j+center_move])
    return d_image

################
e_image = erode_bin_image(img, kernel)
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
