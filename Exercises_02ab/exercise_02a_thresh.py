import cv2
img1 = cv2.imread("cam_74.pgm", cv2.IMREAD_GRAYSCALE)
print(img1.shape)

# 1st way:
value = 100 	#threshold value
img2 = img1.copy()
nrows = img1.shape[0]
ncols = img1.shape[1]

for pc in range(0, ncols):
    for pr in range(0,nrows):
        if img2[pc, pr] < value:
            img2[pc,pr] = 0
        else:
            img2[pc, pr] = 255



cv2.imwrite("cam_74_threshold100.pgm", img2);
cv2.imshow("cam_74_threshold100.pgm", img2)
cv2.waitKey(0)  # waiting for a key must use after imshow

'''
# 2st way:
value = 100

# print(cv2.__version__)
img2 = img1.copy()
ret,img2 = cv2.threshold(img1,value,255,cv2.THRESH_BINARY)
print("Showing image in window... Press a key to finish.")

cv2.imshow("output.png", img2)
cv2.waitKey(0) # waiting for a key must use after imshow

'''
