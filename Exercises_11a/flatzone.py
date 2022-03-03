import numpy as np
from queue import Queue

Img = np.array([[1,1,1,2],
                [3,3,3,2],
                [3,4,4,2],
                [3,4,4,2]])

img = np.array([[0,0,0,0],
                [0,0,0,0],
                [0,0,0,0],
                [0,0,0,0]])

LABEL_FZ = np.array([1,2])
def produceFlatzone(Img, img, LABEL_FZ):
    x,y = LABEL_FZ[0],LABEL_FZ[1]
    img[x][y] = 1
    flatzone = Queue(maxsize=0)
    flatzone.put([x,y])
    while not flatzone.empty():
        p = flatzone.get()
        px,py = p[0],p[1]
        for i in range(px-1, px+1+1):
            for j in range(py-1, py+1+1):
                if i>=0 and i<4 and j>=0 and j<4:
                        if Img[i][j]==Img[px][py] and img[i][j] != 1:
                            img[i][j] = 1
                            flatzone.put([i,j])
    return img
output = produceFlatzone(Img,img,LABEL_FZ)
print(output)

