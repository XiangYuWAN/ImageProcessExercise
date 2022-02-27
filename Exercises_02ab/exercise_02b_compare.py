import cv2
img1 = cv2.imread("cam_74.pgm", cv2.IMREAD_GRAYSCALE)
# print(img1.shape)
irow = img1.shape[0]
icol = img1.shape[1]
img2 = cv2.imread("cam_74_threshold100.pgm", cv2.IMREAD_GRAYSCALE)
img3 = cv2.imread("cam_74（copy）.pgm", cv2.IMREAD_GRAYSCALE)
compare = 1
for i in range(0, irow):
    for j in range(0, icol):
        if img2[i,j] != img1[i,j]:
            compare = 0;

file = open("exercise_02b_output_01.txt","a")
file.write(f'compare result is:{compare}\n')
#define a method os that can use
def img_compare(img1, img2):
    row1 = img1.shape[0]
    col1 = img1.shape[1]
    compare = True
    for i in range(0, row1):
        for j in range(0, col1):
            if img2[i, j] != img1[i, j]:
                compare = False
    return compare