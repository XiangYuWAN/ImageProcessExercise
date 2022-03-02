import cv2
import img_nomcv_functions.functions as inff

img = cv2.imread("immed_gray_inv.pgm", cv2.IMREAD_GRAYSCALE)
test = cv2.imread("immed_gray_inv_20051123_dil2.pgm", cv2.IMREAD_GRAYSCALE)
imgOutput = img.copy()
rows, cols = img.shape[0],img.shape[1]
k = 2

for i in range(0, rows):
    for j in range(0, cols):
        max = 0
        for x in range(i-k, i+k+1):
            for y in range(j-k, j+k+1):
                if x>=0 and x < rows and y>=0 and y < cols:
                    pixel = img[x,y]
                    if(pixel > max):
                        max = pixel
        imgOutput[i,j] = max

result = inff.img_compare(test, imgOutput)
print(result)