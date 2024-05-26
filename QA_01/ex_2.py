import requests
from bs4 import BeautifulSoup
import selenium

url = 'https://www.divan.ru'

responce = requests.get(url)

print(responce.status_code)

print(responce.text)

soup = BeautifulSoup(responce.text, 'html.parser')
links = soup.find_all('a')

# for link in links:
#    print(link.get('href'))

for link in links:
    href = link.get('href')
    if href.startswith('/'):  # либо if href.startswith('http')
        print(url + href)