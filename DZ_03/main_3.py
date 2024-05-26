# Необходимо спарсить цены на диваны с сайта divan.ru в csv файл,
# обработать данные, найти среднюю цену и вывести ее,
# а также сделать гистограмму цен на диваны

import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

# URL страницы с ценами на диваны
base_url = 'https://www.divan.ru/category/divany-i-kresla/'
total_pages = 35

# Отправляем GET-запрос и получаем содержимое страницы
def parse_page(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

# Находим все элементы с ценами на диваны
    prices = []
    for price_tag in soup.find_all('span', class_='ui-LD-ZU KIkOH'):
        price = price_tag.get_text()
        prices.append(float(price.replace(' ', '').replace('руб.', '').replace('.', '')))
    return prices

# Создаем список цен на диваны
prices = []
for page in range(1, total_pages + 1):
    url = f'{base_url}/?page={page}'
    prices.extend(parse_page(url))

# Создаем DataFrame для обработки данных
df = pd.DataFrame({'Цена': prices})

# Сохраняем данные в CSV-файл
df.to_csv('prices_divan_ru.csv', index=False)

# Находим среднюю цену
average_price = df['Цена'].mean()
print(f'Средняя цена на диваны: {average_price}')

# Строим гистограмму цен
plt.figure(figsize=(10, 6))
plt.hist(df['Цена'], bins=10, color='skyblue', edgecolor='black')
plt.xlabel('Цена')
plt.ylabel('Частота')
plt.title('Гистограмма цен на диваны')
plt.grid(axis='y', alpha=0.75)

# Отображаем гистограмму
plt.show()