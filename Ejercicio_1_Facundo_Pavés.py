#importo la libreria numpy que me permite trabajar con matrices y vectores
import numpy as np

# Defino la matriz
A = np.array([[2.0, 1.0, -1.0],
              [-3.0, -1.0, 2.0],
              [-2.0, 1.0, 2.0]])

#defino el vector b 
b = np.array([8.0, -11.0, -3.0])

# Formamos la matriz aumentada , uno la matriz a y el vector b como una columna extra en la derecha
Ab = np.column_stack((A, b))
n = len(b) #obtengo el tamanio del sistema

#Eliminacion con Gauss (hacia adelante)
for i in range(n):
    # Hacer ceros por debajo del pivote actual
    for j in range(i+1, n):
        multiplicador = Ab[j, i] / Ab[i, i]
        Ab[j] = Ab[j] - multiplicador * Ab[i] #Realizo la operacion elemental por fila (un ejemplo es F2-->F2-multiplicador*F1)

#Sustitución regresiva (hacia atras)
x = np.zeros(n) #creo un vector con ceros para almacenar la solucion del sistema
for i in range(n-1, -1, -1):
    # Despejo cada incognita 
    x[i] = (Ab[i, -1] - np.dot(Ab[i, i+1:n], x[i+1:n])) / Ab[i, i]

print("Matriz escalonada resultante:")
print(Ab)
print("\nSolución del sistema:")
print(f"x1 = {x[0]:.0f}")
print(f"x2 = {x[1]:.0f}")
print(f"x3 = {x[2]:.0f}")
