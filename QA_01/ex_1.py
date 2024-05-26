import pandas as pd

df = pd.read_csv('movies.csv')
print(df.info())

# 5 первых строк
print(df.head())

# Количество строк и столбцов
rows, columns = df.shape
print(rows, columns)

# сортировка по столбцу
print(df.sort_values('Worldwide Gross', ascending=False).head(10))


