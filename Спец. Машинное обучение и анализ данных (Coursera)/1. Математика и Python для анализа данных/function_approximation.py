"""Приблизить данную функцию многочленом первой, второй, третей степени."""

import numpy as np
import math
from scipy.linalg import solve
import matplotlib.pyplot as plt

def f(x):
	return math.sin(x / 5) * math.exp(x / 10) + 5 * math.exp(-x / 2)

A = np.array([[1, 1], [1, 15]])
b = np.array([f(1), f(15)])
n = solve(A,b)

fig = plt.figure()
scatter = plt.scatter(0.0, 16.0)
x = np.arange(0, 16)
y = n[0] + n[1]*x
plt.plot(x, y)
plt.grid(True)
plt.show()

A1 = np.array([[1, 1, 1], [1, 8, 64], [1, 15, 15**2]])
b1 = np.array([f(1), f(8), f(15)])
n1 = solve(A1,b1)

fig1 = plt.figure()
scatter1 = plt.scatter(0.0, 16.0)
x1 = np.arange(0, 16)
y1 = n1[0] + n1[1]*x + n1[2]*x**2
plt.plot(x1, y1)
plt.grid(True)
plt.show()

A2 = np.array([[1, 1, 1, 1], [1, 4, 16, 4**3], [1, 10, 100, 1000], [1, 15, 15**2, 15**3]])
b2 = np.array([f(1), f(4), f(10), f(15)])
n2 = solve(A2,b2)

fig2 = plt.figure()
scatter2 = plt.scatter(0.0, 16.0)
x2 = np.arange(0, 16)
y2 = n2[0] + n2[1]*x + n2[2]*x**2 + n2[3]*x**3
plt.plot(x2, y2)
plt.grid(True)
plt.show()
