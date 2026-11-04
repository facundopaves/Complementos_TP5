
import numpy as np

# Definimos la matriz A 
A = np.array([
    [0.0001, 1],
    [1, 1]
], dtype=float)


#Defino el vector B
B = np.array([1.0001, 2], dtype=float)

# Armamos la matriz ampliada
matriz_ampliada = np.column_stack([A, B])
n = len(matriz_ampliada)

print("Matriz ampliada original:")
print(matriz_ampliada)
print("--------------------------------")

#Eliminacion hacia delante con el pivoteo parcia 
for i in range(n - 1):

    # Buscamos el mayor elemento de la columna
    maximo_valor = i + np.argmax(np.abs(matriz_ampliada[i:, i]))

    # Intercambio filas si encuentro un pivote mayor
    if maximo_valor != i:
        matriz_ampliada[[i, maximo_valor]] = matriz_ampliada[[maximo_valor, i]]

        print(f"Intercambio de filas {i} y {maximo_valor}:")
        print(matriz_ampliada)
        print("--------------------------------")

    # Eliminacion gaussiana
    for j in range(i + 1, n):
        factor = matriz_ampliada[j, i] / matriz_ampliada[i, i] # Calculo el factor de eliminacion
        matriz_ampliada[j] = matriz_ampliada[j] - factor * matriz_ampliada[i] #multiplico la fila pivote por el factor y la resto a la fila actual para hacer cero el elemento debajo del pivote

# Sustitucion regresiva
x = np.zeros(n)

for i in range(n - 1, -1, -1):
    x[i] = matriz_ampliada[i, -1]

    for j in range(i + 1, n):
        x[i] -= matriz_ampliada[i, j] * x[j]

    x[i] /= matriz_ampliada[i, i]

# Muestro los resultados al usuario
print("Matriz triangulada:")
print(matriz_ampliada)

print("--------------------------------")

print("\nSolución final:")
print("x1 =", x[0])
print("x2 =", x[1])
