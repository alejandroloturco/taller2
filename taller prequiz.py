import numpy as np

matriz = np.random.randint(100, size=(40,30,100,10))

new_matriz = matriz.copy()[:,:,:,0]
print(new_matriz.size)