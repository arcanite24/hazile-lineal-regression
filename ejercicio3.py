# -*- coding: utf-8 -*-
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from numpy import genfromtxt

# Leer archivo con los datos, basicamente, es un archivo como si fuera una tabla simplificada
file = genfromtxt('dataset3.csv', delimiter=',')

# Una funcion lambda es una funcion anonima, la usamos para elevar al cuadrado cada elemento de una lista
squarer = lambda x: x ** 2

# La funcion "map" ejecuta una lambda function para cada elemento de una lista, el valor de retorno es el nuevo
# valor que toma en dicha posicion, por ejemplo:
# lista_nueva = map(lambda x: x * 2, [1, 2, 3, 4, 5])
# print(lista_nueva) -> [2, 4, 6, 8, 10]
# Es un equivalente a lo siguiente
"""
def squarer(n)
  return n ** 2

lista = [1, 2, 3, 4, 5]

for n, index in lista:
  lista[index] = squarer(n)

"""

# En esta parte, pasa algo similar, aplica la funcion a cada elemento en la lista
# Donde la lista es el archivo que acabamos de leer, hacemos esto para obtener la primer
# columna como X y la segunda como Y
x = np.array(map(lambda x: x[0], file))
y = np.array(map(lambda x: x[1], file))

# Cuantos registros hay en el archivo
n = len(file)

# Calcular la media de valores en X y Y respectivamente
x_mean = np.mean(x)
y_mean = np.mean(y)

# Calcular la suma de los valores en X y Y respectivamente
x_sum = np.sum(x)
y_sum = np.sum(y)

# Calcular la suma de todos los valores elevados al cuadrado para X y Y
x_sum_sqrd = np.sum(squarer(x))
y_sum_sqrd = np.sum(squarer(y))

# Suma de todos los valores X * Y
xy_sum = np.sum(x * y)

# Calcular SSX y SXY acorda a la info que me pasaste
sxx = x_sum_sqrd - ((x_sum ** 2) / n)
sxy = xy_sum - ((x_sum * y_sum) / n)

# Calcular b0 y b1 de acuerdo a los apuntes
b1 = sxy / sxx
b0 = y_mean - (b1 * x_mean)

print('b0:', b0)
print('b1:', b1)

# Crear la lista con valores de Y de la recta de regresion predecida
predicted_y = [b0  + b1 * xi for xi in x]

# Calcular el error de acuerdo a la formula
error = np.sum(map(lambda x: x ** 2, [y[i] - (b0 + b1 * x[i]) for i in range(n)]))
print('error:', error)

# Iniciar PyPlot para graficar y guardar la imagen
fig, ax = plt.subplots()
plt.figure(1)

# Dispersion de X y Y
ax.scatter(x, y)
# Grafica de Regresion
ax.plot(x, predicted_y, 'r')

# Poner el titulo
ax.set(xlabel='X', ylabel='Y', title='Ejercicio 3: X vs Y')
# Poner una grilla
ax.grid()

# Guardar el archivo
fig.savefig("ejercicio3_xy.png")

fig_dispesion, ax_dispersion = plt.subplots()
plt.figure(2)
ax_dispersion.scatter(x, y)

ax_dispersion.set(xlabel='X', ylabel='Y', title='Dispersion de Puntos')
ax_dispersion.grid()

fig_dispesion.savefig("ejercicio2_dispersion.png")
plt.show()