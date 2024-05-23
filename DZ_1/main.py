import pandas as pd
# Выведите первые 5 строк данных, чтобы получить представление о структуре данных.
# Выведите информацию о данных (.info()) и статистическое описание (.describe()).

df = pd.read_csv('apple.csv')

print(df.head())
print(df.info())
print(df.describe())

# Определите среднюю зарплату (Salary) по городу (City) - используйте файл приложенный к дз - dz.csv

df = pd.read_csv('dz.csv')
group = df.groupby('City')['Salary'].mean()
print(group)