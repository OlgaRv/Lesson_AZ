# Построй диаграмму рассеяния для двух наборов случайных данных, сгенерированных с помощью функции `numpy.random.rand`.

import numpy as np

random_array_1 = np.random.rand(5)  # массив из 5 случайных чисел
print(random_array_1)

random_array_2 = np.random.rand(5)  # массив из 5 случайных чисел
print(random_array_2)

import matplotlib.pyplot as plt

plt.scatter(random_array_1, random_array_2)
plt.show()
