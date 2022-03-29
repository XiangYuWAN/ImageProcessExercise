import sys
import cv2
from Util import util

ORIGINAL = "micro24.pgm"
MARKER = "micro24_20060309_markersfond.pgm"

try:
    ORIGINAL = sys.argv[1]
    MARKER = sys.argv[2]
except Exception as e:
    print(sys.argv)
    print(e)
    sys.exit()

# I is an original image
I = cv2.imread(ORIGINAL, cv2.IMREAD_GRAYSCALE)
#Maker of image
M = cv2.imread(MARKER, cv2.IMREAD_GRAYSCALE)

ret, M = cv2.threshold(M, 100, 255, cv2.THRESH_BINARY)
Minv = cv2.bitwise_not(M)
Iinf = util.imageInf(I, Minv)
Minv_i = Minv
i = 0
while True:
    Minv_i1 = util.imageSup(util.erode(Minv_i,1), Iinf)
    i = i+1
    Minv_i = Minv_i1
    if util.compareImages(Minv_i, Minv_i1) : break
Minv_final = Minv_i
picture = Minv_final

cv2.imshow("display", picture)
cv2.waitKey(0)
