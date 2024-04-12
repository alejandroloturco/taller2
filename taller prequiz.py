import numpy as np

matriz = np.random.randint(100, size=(40,30,100,10))

new_matriz = matriz.copy()[:,:,:,0]

print(f"Dimension: {new_matriz.ndim}")
print(f"Tamaño: {new_matriz.size}")
print(f"Forma: {new_matriz.shape}")
print(f"Tipo: {new_matriz.dtype}")
print(f"Tamaño en bytes de cada elemento en el array: {new_matriz.itemsize}")
print(f"Tamaño de los bytes: {new_matriz.nbytes}")

new2_matriz = np.reshape(new_matriz,(new_matriz.shape[0],new_matriz.shape[1]*new_matriz.shape[2]))
