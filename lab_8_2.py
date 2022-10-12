import numpy as np 
import random 

M = 4
N = 5

massiv = np.zeros((M, N), int) 

for i in range(M):     
    for j in range(N):         
        massiv[i][j] = random.randint(0, 1) 
   

sp = []

for i in massiv:
    if np.sum(i) % 2 == 0:
        sp.append(np.append(i, 0))
    else:
        sp.append(np.append(i, 1))


new_massiv = np.vstack(sp)

print(new_massiv)    