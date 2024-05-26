import pandas as pd
import matplotlib.pyplot as plt

# Загрузка измененного CSV-файла
df = pd.read_csv('prices_upgrade.csv')

# Построение гистограммы
plt.figure(figsize=(10, 6))
plt.hist(df['Цена'], bins=10, color='skyblue', edgecolor='black')
plt.xlabel('Значения')
plt.ylabel('Частота')
plt.title('Гистограмма данных')
plt.grid(axis='y', alpha=0.75)

# Отображение гистограммы
plt.show()
