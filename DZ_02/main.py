# Исследование оценок учеников
# Представьте, что у вас есть таблица из 10 учеников с оценками учеников по 5 разным предметам.
# Вам нужно выполнить несколько шагов, чтобы проанализировать эти данные:
# 1. Самостоятельно создайте DataFrame с данными
# 2. Выведите первые несколько строк DataFrame, чтобы убедиться, что данные загружены правильно
# 3. Вычислите среднюю оценку по каждому предмету
# 4. Вычислите медианную оценку по каждому предмету
# 5. Вычислите Q1 и Q3 для оценок по математике:
#    Q1_math = df['Математика'].quantile(0.25)
#    Q3_math = df['Математика'].quantile(0.75)
#    можно также попробовать рассчитать IQR
# 6. Вычислите стандартное отклонение

import pandas as pd
import matplotlib.pyplot as plt

data = {
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Ivan', 'John', 'Kate', 'Linda', 'Mike'],
    'maths': [4, 5, 3, 5, 4, 5, 3, 4, 3, 5],
    'geography': [5, 3, 5, 4, 5, 3, 5, 4, 5, 4],
    'physics': [5, 4, 3, 4, 5, 4, 4, 3, 5, 4],
    'computer science': [4, 5, 4, 5, 4, 5, 4, 5, 4, 5],
    'biology': [4, 3, 5, 4, 5, 3, 5, 4, 5, 4]
}

df = pd.DataFrame(data)

print(df)
print()

df.boxplot(column=['maths', 'geography', 'physics', 'computer science', 'biology'])
plt.show()

print(f"Средняя оценка по математике: {df['maths'].mean()}")
print(f"Средняя оценка по географии: {df['geography'].mean()}")
print(f"Средняя оценка по физике: {df['physics'].mean()}")
print(f"Средняя оценка по программированию: {df['computer science'].mean()}")
print(f"Средняя оценка по биологии: {df['biology'].mean()}")
print()
print(f"Медианная оценка по математике: {df['maths'].median()}")
print(f"Медианная оценка по географии: {df['geography'].median()}")
print(f"Медианная оценка по физике: {df['physics'].median()}")
print(f"Медианная оценка по программированию: {df['computer science'].median()}")
print(f"Медианная оценка по биологии: {df['biology'].median()}")
print()

Q1_math = df['maths'].quantile(0.25)
Q3_math = df['maths'].quantile(0.75)

print(f"Q1_math: {Q1_math}")
print(f"Q3_math: {Q3_math}")
print()

IQR = Q3_math - Q1_math

print(f"Стандартное отклонение по математике: {df['maths'].std()}")
print(f"Стандартное отклонение по географии: {df['geography'].std()}")
print(f"Стандартное отклонение по физике: {df['physics'].std()}")
print(f"Стандартное отклонение по программированию: {df['computer science'].std()}")
print(f"Стандартное отклонение по биологии: {df['biology'].std()}")