import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from numpy import genfromtxt

file = genfromtxt('dataset2.csv', delimiter=',')

squarer = lambda x: x ** 2

x = np.array(map(lambda x: x[0], file))
y = np.array(map(lambda x: x[1], file))

n = len(file)

x_mean = np.mean(x)
y_mean = np.mean(y)

x_sum = np.sum(x)
y_sum = np.sum(y)

x_sum_sqrd = np.sum(squarer(x))
y_sum_sqrd = np.sum(squarer(y))

xy_sum = np.sum(x * y)

sxx = x_sum_sqrd - ((x_sum ** 2) / n)
sxy = xy_sum - ((x_sum * y_sum) / n)

b1 = sxy / sxx
b0 = y_mean - (b1 * x_mean)

print('b0:', b0)
print('b1:', b1)

predicted_y = [b0  + b1 * xi for xi in x]
error = np.sum(map(lambda x: x ** 2, [y[i] - (b0 + b1 * x[i]) for i in range(n)]))
print('error:', error)

fig, ax = plt.subplots()
plt.figure(1)

ax.scatter(x, y)
ax.plot(x, predicted_y, 'r')

ax.set(xlabel='X', ylabel='Y', title='Ejercicio 2: X vs Y')
ax.grid()

fig.savefig("ejercicio2_xy.png")

fig_dispesion, ax_dispersion = plt.subplots()
plt.figure(2)
ax_dispersion.scatter(x, y)

ax_dispersion.set(xlabel='X', ylabel='Y', title='Dispersion de Puntos')
ax_dispersion.grid()

fig_dispesion.savefig("ejercicio2_dispersion.png")
plt.show()