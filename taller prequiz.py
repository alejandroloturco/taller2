import numpy as np
import pandas as pd
import scipy.io

matriz = np.random.randint(100, size=(40,30,100,10))

new_matriz = matriz.copy()[:,:,:,0]

print(f"Dimension: {new_matriz.ndim}")
print(f"Tamaño: {new_matriz.size}")
print(f"Forma: {new_matriz.shape}")
print(f"Tipo: {new_matriz.dtype}")
print(f"Tamaño en bytes de cada elemento en el array: {new_matriz.itemsize}")
print(f"Tamaño de los bytes: {new_matriz.nbytes}")

new2_matriz = np.reshape(new_matriz,(new_matriz.shape[0],new_matriz.shape[1]*new_matriz.shape[2]))

def conversion(matriz):
    return pd.DataFrame(matriz)

def cargar(ruta):
    if ruta.endswith('.mat'):
        return scipy.io.loadmat(ruta)
    elif ruta.endsith('.csv'):
        return pd.read_csv(ruta)
    else:
        print("tipo de archivo no reconocido")

def calculadora(matriz, operacion,eje = None):
    if operacion == 'sum':
        return np.sum(matriz, axis = eje)
    elif operacion == 'rest':
        return np.subtract.reduce(matriz, axis = eje)
    elif operacion == 'mul':
        return np.prod(matriz, axis = eje)
    elif operacion == 'div':
        return np.divide.reduce(matriz, axis = eje)
    elif operacion == 'log':
        return np.log(matriz)
    elif operacion == 'prom':
        return np.mean(matriz, axis = eje)
    elif operacion == 'desvesta':
        return np.std(matriz, axis = eje)

