import pandas as pd

data = {
    'Возраст' : [23, 22, 21, 27, 23, 20, 29, 28, 26, 24],
    'Зарплата' : [54000, 58000, 60000, 52000, 55000, 59000, 51000, 49000, 53000, 61000]
}

df = pd.DataFrame(data)

print(df.describe())

print(f"Средний возраст: {df['Возраст'].mean()}")
print(f"Медиана возраста: {df['Возраст'].median()}")
print(f"Стандартное отклонение возраста: {df['Возраст'].std()}")

print(f"Средняя зарплата: {df['Зарплата'].mean()}")
print(f"Медиана зарплаты: {df['Зарплата'].median()}")
print(f"Стандартное отклонение зарплаты: {df['Зарплата'].std()}")

