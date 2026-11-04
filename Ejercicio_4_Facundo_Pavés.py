
import numpy as np
from scipy.linalg import lu

print("======================================================")
print("  RESOLUCIÓN DE SISTEMAS MEDIANTE FACTORIZACIÓN LU")
print("======================================================\n")

# Defino la matriz que me dieron en el ejercicio (Matriz A)
A = np.array([
    [4, 1, 1],
    [2, 5, 1],
    [1, 1, 3]
], dtype=float)

# Defino los tres vectores independientes del ejercicio (b1, b2, b3)
b1 = np.array([9, 15, 12], dtype=float)
b2 = np.array([-2, 0, 5], dtype=float)
b3 = np.array([8, 0, 4], dtype=float)

#guardo los vectores en una lista
vectores = [b1, b2, b3]

#Muestro la matriz al usuario
print("Matriz A:")
print(A)

print("-----------------------")

# 3. Factorización LU
# A = P @ L @ U  #Utilizo el @ debido a que no es lo mismo multiplicar matrices que multiplicar numeros, el @ es para multiplicar matrices
P, L, U = lu(A)

print("\n--- MATRICES DE FACTORIZACIÓN ---")
print("\nMatriz P:")
print(P)

print("\nMatriz L (Triangular inferior):")
print(L)

print("\nMatriz U (Triangular superior):")
print(U)

#Resolución de los tres sistemas
for i, b in enumerate(vectores, start=1):

    print("\n======================================")
    print(f" RESOLUCIÓN DEL SISTEMA {i}")
    print("======================================")

    print("\nVector independiente:")
    print(b)

    # Sustitución progresiva: L @ y = P.T @ b
    pb = P.T @ b
    y = np.linalg.solve(L, pb)

    print("\nResultado de sustitución progresiva (y):")
    print(y)

    # Sustitución regresiva: U @ x = y
    x = np.linalg.solve(U, y)

    print("\nSolución final:")
    for j in range(len(x)):
        print(f"x{j+1} = {x[j]:.4f}")
