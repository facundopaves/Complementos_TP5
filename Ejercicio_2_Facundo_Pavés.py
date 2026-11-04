import numpy as np

#Defino la matriz de coeficientes A 
A = np.array([[0.0, 2.0, 1.0],
              [1.0, -2.0, -3.0],
              [2.0, 3.0, 1.0]])

#Defino el vector independiente b
b = np.array([3.0, 0.0, 7.0])

# Formamos la matriz aumentada , uno la matriz a y el vector b como una columna extra en la derecha
Ab = np.column_stack((A, b))
n = len(b) #obtengo el tamanio del sistema

#imprimo la matriz aumentada original
print("---------------------------")
print("Matriz aumentada original:")
print(Ab)
print("---------------------------")

#Eliminación Gaussiana con pivoteo parcial (hacia adelante)
for i in range(n):
    # Buscar el índice de la fila con el mayor valor absoluto en la columna actual
    max_row = np.argmax(abs(Ab[i:n, i])) + i #Reviso la columna actual para encontrar el pivote máximo y sumo i para obtener el índice correcto en la matriz completa
    
    # Intercambiar la fila actual con la fila del pivote máximo si son distintas
    if i != max_row:
        Ab[[i, max_row]] = Ab[[max_row, i]]
        print(f"Intercambio de Fila {i+1} con Fila {max_row+1}:")
        print(Ab)
        print("---------------------------")
        
    # Hacer ceros por debajo del pivote actual
    for j in range(i+1, n):
        multiplicador = Ab[j, i] / Ab[i, i]
        Ab[j] = Ab[j] - multiplicador * Ab[i]

#Sustitución regresiva (hacia atras)
x = np.zeros(n)
for i in range(n-1, -1, -1):
    x[i] = (Ab[i, -1] - np.dot(Ab[i, i+1:n], x[i+1:n])) / Ab[i, i]

print("Matriz escalonada resultante:")
print(Ab)
print("\n--- SOLUCIÓN DEL SISTEMA ---")
print(f"x1 = {x[0]:.0f}")
print(f"x2 = {x[1]:.0f}")
print(f"x3 = {x[2]:.0f}")