import numpy as np
import matplotlib.pyplot as plt


N = 8
jcnt = 18
isSYM = True
ia = [1,5,8,10,12,15,17,18,19]
ja = [1,3,6,7, 2,3,5,3,8,4,7,5, 6,7,6,8, 7,8]
A =  [7,1,2,7,-4,8,2,1,5,7,9,5,-1,5,0,5,11,5]

AA = np.zeros([N,N])
isSYM = False
N = 8
jcnt = 20
ia = [1,5,8,10,12,13,16,18,21]
ja = [1,3,6,7, 2,3,5,3,8,4,7, 2,3,6,8, 2, 7, 3,7,8]
A  = [7,1,2,7,-4,8,2,1,5,7,9,-4,7,3,5,17,11,-3,2,5]

i = 1
if (isSYM):
    for j in range (jcnt):
        y = ja[j] - 1
        if j+1 > (ia[i]-1):
            i += 1
        x = i-1
        AA[x][y] = A[j]
        AA[y][x] = A[j]
        print (x,y,A[j])
else:
    for j in range (jcnt):
        y = ja[j] - 1
        if j+1 > (ia[i]-1):
            i += 1
        x = i-1
        AA[x][y] = A[j]
        print (x,y,A[j])
    
plt.matshow(AA)
plt.show()
plt.matshow(AA[0:10,0:10])
plt.show()
