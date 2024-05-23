import pandas as pd

df = pd.read_csv('animal.csv')
print(df)

print(df['Животное'].tolist())
print(df.columns.tolist())

# Группировка по столбцу

group = df.groupby('Пища')['Средняя продолжительность жизни'].mean()
print(group)

# Заполнение пропусков - 1 вариант

df.fillna(0, inplace=True)
print(df)

# Удаление пропусков - 2 вариант

df.dropna(inplace=True)
print(df)
