import pandas as pd

# Загрузка CSV-файла
df = pd.read_csv('prices.csv')

# Убираем текст "₽/мес." из столбца и преобразуем данные в числовой тип
df['Цена'] = df['Цена'].str.replace(' ₽/мес.', '').str.replace(' ', '').astype(int)

# Сохранение измененного DataFrame обратно в CSV-файл
df.to_csv('prices_upgrade.csv', index=False)