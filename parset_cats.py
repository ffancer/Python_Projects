"""
Соберем породы кошек в список
breed - порода по англ.
"""
import requests
from bs4 import BeautifulSoup


URL = 'https://hvost.news/animals/cats-breeds/'
headers = {
    'Accept': '*/*',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
}

req = requests.get(URL, headers=headers)
soup = BeautifulSoup(req.text, 'lxml')
json_list = []

all_cats = soup.find_all('a', class_='breeds-list-i')
for cat in all_cats:
    breed = cat.find(class_='breeds-list-i__name').text.strip()
    character = cat.find(class_='breeds-list-i__label').text
    link = 'https://hvost.news/' + cat['href']

    json_list.append(
        {
            'Порода': breed,
            'Характер': character,
            'Более подробная информация по ссылке': link
        }
    )

