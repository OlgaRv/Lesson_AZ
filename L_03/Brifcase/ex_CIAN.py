from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import csv

driver = webdriver.Chrome()

url = 'https://www.cian.ru/snyat-kvartiru-1-komn-ili-2-komn/'

# открытие страницы
driver.get(url)

# ждём загрузку страницы
time.sleep(5)

# парсинг цен
prices = driver.find_elements(By.XPATH,"//span[@data-mark='MainPrice']/span")

# открытие csv-файла для записи
with open('prices.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Цена']) # Запись названий столбцов

 # Запись цен в файл
    for price in prices:
        writer.writerow([price.text])

# закрытие браузера
driver.quit()
