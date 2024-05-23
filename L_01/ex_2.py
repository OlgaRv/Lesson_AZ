import pandas as pd

df = pd.read_csv('hh.csv')
print(df.info())

# добавление столбца

df['Test'] = [str(new) for new in range(25)]
print(df)

# удаление столбца
df.drop('Test', axis=1, inplace=True)
print(df)

# удаление строки
df.drop(24, axis=0, inplace=True)
print(df)