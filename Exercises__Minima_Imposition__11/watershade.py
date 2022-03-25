import cv2
from Util import util

I = cv2.imread("micro24.pgm", cv2.IMREAD_GRAYSCALE)
I2 = cv2.imread("micro24_20060309_grad.pgm", cv2.IMREAD_GRAYSCALE)
compare = util.compareImages(I, I2)
print(compare)


cv2.imshow("display", I)
cv2.imshow("I2",I2)
cv2.waitKey(0)

