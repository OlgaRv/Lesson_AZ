import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
b = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(a + b)

a = np.zeros((3, 3))
print(a)

b = np.ones((2, 5))
print(b)

c = np.random.random((4, 5))
print(c)

d = np.arange(0, 10, 2)
print(d)

e = np.linspace(0, 13, 10)
print(e)

f = np.eye(3)
print(f)

g = np.diag([1, 2, 3, 4, 5])
print(g)

import matplotlib.pyplot as plt

x =  np.linspace(-10, 10, 100)
y = x**2

plt.plot(x, y)
plt.xlabel("ось X")
plt.ylabel("ось Y")
plt.title("График функции y = x^2 - пример")
plt.grid(True)
plt.show()