import numpy as np
import cv2
from queue import Queue
def Reflatzone(Img1, Img2, x, label_fz):
    Img1.shape[0],Img2.shape[1] = label_fz[0],label_fz[1]
    flatzone = Queue(maxsize=0)
    while not flatzone.empty():
        p = flatzone.get()  # p is a pixel
        prow,pcol = p[0],p[1]
        for i in range(prow-1,prow+1+1):
            for j in range(pcol-1,pcol+1+1):
                if Img2[i][j] == Img2[prow][pcol] and Img1[i][j] != label_fz:
                    Img1[i][j] = label_fz
                    flatzone.put([i,j])




