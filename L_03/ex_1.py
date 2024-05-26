import matplotlib.pyplot as plt

# линейный график
x = [1, 2, 6, 8, 14, 17, 20, 22]
y = [6, 4, 10, 12, 18, 25, 30, 32]

plt.plot(x, y)
plt.title("Линейный график - пример")
plt.xlabel("ось X")
plt.ylabel("ось Y")
plt.show()

# гистограмма
data = [5, 6, 7, 4, 6, 5, 7, 8, 5, 6, 7, 8, 9, 10, 11, 8, 9, 10, 7, 6, 5, 7, 8, 9, 10, 7, 6, 5]

plt.hist(data, bins=3, color="green")

plt.title("Гистограмма - пример")
plt.xlabel("часы сна")
plt.ylabel("количество людей")
plt.show()

# диаграмма рассеивания
x = [1, 2, 6, 8, 14, 17, 20, 22]
y = [3, 8, 10, 12, 18, 25, 30, 32]

plt.scatter(x, y, color="green")
plt.title("Диаграмма рассеивания - пример")
plt.xlabel("ось X")
plt.ylabel("ось Y")
plt.show()

