"""
top 100 dorams from https://vsedoramy.net/top100korean.html
"""
import requests
from bs4 import BeautifulSoup
import pandas as pd


url = 'https://vsedoramy.net/top100korean.html'
headers = {
    'Accept': '*/*',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
}
# req = requests.get(url, headers=headers)
# soup = BeautifulSoup(req.text, 'lxml')

# with open('topdorams.html', 'w', encoding='utf-8') as file:
#     file.write(req.text)


# можно работать с сохраненой страничкой, т.к. динамики на сайте нет
with open('topdorams.html', encoding='utf-8') as file:
    src = file.read()

soup = BeautifulSoup(src, 'lxml')
cards = soup.find('ol', class_='clearfix').find_all('li', class_='top100-item')
# сделал нумерование от 1 до 100 в первом вложенном списке
data_list = [[i for i in range(1, 101)], [], [], []]


# ищем и записываем данные в список
def data_search():
    for card in cards:
        title = card.find('img', alt=True)
        data_list[1].append(title['alt'])
        img = card.find('img', src=True)
        data_list[2].append('https://vsedoramy.net' + img['src'])
        link = card.find('a').get('href')
        data_list[3].append(link)


# записываем данные из списка в Excel файл
def list_to_excel():
    df = pd.DataFrame.from_dict({'Место: ': data_list[0], 'Название: ': data_list[1], 'Картинка: ': data_list[2], 'Ссылка: ': data_list[3]})
    df.to_excel('top_100_dorams.xlsx', header=True, index=False)


data_search()
list_to_excel()

"""
link at google docs with top 100 dorams:
https://docs.google.com/spreadsheets/d/1pC1hWyYc6YNKary4_NAzG4GQLaaUF5sCGrxToaxIyjU/edit#gid=1182540734
"""


