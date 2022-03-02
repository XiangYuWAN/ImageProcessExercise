import cv2
import numpy as np
from queue import Queue

q = Queue(maxsize=0)
iA1 = np.array([[1,1,1,2],
                [3,3,3,2],
                [3,4,4,2],
                [3,4,4,2]])

iA2 = np.array([[0,0,0,0],
                [0,0,0,0],
                [0,0,0,0],
                [0,0,0,0]])

iw = iA1.shape[0]
ih = iA1.shape[1]
# kernel: 4 nabour
sp = [3,3]
value = iA1[3][3]
q.put(sp)
# print(q.empty())

# ogic is not right
for i in range(0,iw):
    for j in range(0,ih):
        if not q.empty():
            print(q.qsize())
            p = q.get()
            iA2[p[0]][p[1]] = 1
            for pi in range(i-p[0], i+p[0]+1):
                for pj in range(j-p[1], j+p[1]+1):
                    if pi>=0 and pi<iw and pj>=0 and pj<ih:
                        if iA1[pi][pj] == value:
                            q.put([pi, pj])
print(iA2)