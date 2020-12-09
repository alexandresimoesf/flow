import numpy as np
import matplotlib.pyplot as plt

np.set_printoptions(suppress=True)

nx = 100
ny = 100

u,v = np.linspace(0,nx,nx),np.linspace(0,ny,ny)

T = np.ones((nx, ny))                         # I.C (U = Velocity)



T[0, :] = 0         #  B.C
T[-1,:] = 20        #  B.C
T[1:-1, 0] = 20       #  B.C
T[1:-1,-1] = 0        #  B.C



for k in range(1000):
    for indexx, i in enumerate(T[1:-1]):
        for indexy, j in enumerate(i[1:]):
            try:
              T[indexx+1][indexy+1] = (T[indexx+1][indexy+2] + T[indexx+1][indexy] + T[indexx+2][indexy+1] + T[indexx][indexy+1])/4
            except:
                T[indexx + 1][indexy + 1] = (T[indexx][indexy+1] + T[indexx + 1][indexy] + T[indexx + 2][indexy+1])/3


plt.quiver(u,v, T[:,:], 0)
plt.show()
