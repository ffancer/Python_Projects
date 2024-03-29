"""
top 100 dorams from https://vsedoramy.net/top100korean.html
+++++++++++++++++++++++++++++++++++++++++++
link at google docs with top 100 dorams:
https://docs.google.com/spreadsheets/d/1pC1hWyYc6YNKary4_NAzG4GQLaaUF5sCGrxToaxIyjU/edit#gid=1182540734
+++++++++++++++++++++++++++++++++++++++++++
upd. for version 1.02:
- need more sites (2-3 or more)
- no duplicates
"""
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

#
#
# url = 'https://vsedoramy.net/top100korean.html'

headers = {
    'Accept': '*/*',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
}
#
# req = requests.get(url, headers=headers)
# soup = BeautifulSoup(req.text, 'lxml')
# # сделал нумерование от 1 до 100 в первом вложенном списке
# data_list = [[i for i in range(1, 101)], [], [], []]
#
#
# # ищем и записываем данные в список
# def data_search():
#     cards = soup.find('ol', class_='clearfix').find_all('li', class_='top100-item')
#     for card in cards:
#         title = card.find('img', alt=True)
#         data_list[1].append(title['alt'])
#         img = card.find('img', src=True)
#         data_list[2].append('https://vsedoramy.net' + img['src'])
#         link = card.find('a').get('href')
#         data_list[3].append(link)
#
#
# # записываем данные из списка в Excel файл
# def list_to_excel():
#     df = pd.DataFrame.from_dict({'Место: ': data_list[0], 'Название: ': data_list[1], 'Картинка: ': data_list[2], 'Ссылка: ': data_list[3]})
#     df.to_excel('top_100_dorams.xlsx', header=True, index=False)
#
#
# data_search()
# list_to_excel()


# ++++++++++++++++++++++++++++++++++  site number 2  ++++++++++++++++++++++++++++++++++++++++++++++++
# count = 1
# url_2 = f'https://doramy.club/top/page/{count}'
# data_list_2 = [[], [], [], [], []]
#
#
# def take_data():
#     req = requests.get(url_2, headers=headers)
#     soup = BeautifulSoup(req.text, 'lxml')
#     cards = soup.find_all('div', class_='post-home')
#
#     for card in cards:
#         score = card.find('div', class_='average').text
#         data_list_2[0].append(score)
#         name = card.find('a').find('span').text
#         # print(name)
#         # if name not in data_list_2[1]:
#         data_list_2[1].append(name)
#
#
#         # работа с <td>
#         columns = card.find_all('td')
#         columns = [i.text.strip() for i in columns]
#
#         # выясняем сериал или фильм
#         film_or_serial = 'Сериал'
#         if columns[0] == 'Страна:':
#             film_or_serial = 'Фильм'
#         data_list_2[2].append(film_or_serial)
#
#         try:
#             genres = columns[columns.index('Жанр:') + 1]
#             data_list_2[3].append(genres)
#         except ValueError:
#             data_list_2[3].append(' ')
#
#         episodes_count = 1
#         if columns[1][0].isdigit():
#             episodes_count = columns[1]
#         data_list_2[4].append(episodes_count)
#
#
# def list_to_excel():
#     df = pd.DataFrame.from_dict({'Рейтинг: ': data_list_2[0], 'Название: ': data_list_2[1], 'Фильм или сериал: ': data_list_2[2], 'Жанр: ': data_list_2[3], 'Кол-во эпизодов: ': data_list_2[4]})
#     df.to_excel('top_100_dorams_3.xlsx', header=True, index=False)
#
#
# for count in range(239):
#     url_2 = f'https://doramy.club/top/page/{count}'
#     time.sleep(1)
#     take_data()
#
# list_to_excel()
"""
https://docs.google.com/spreadsheets/d/1fxWDW7y5kF3itNztAsY9T12vh6-_EyLpyM2mbe_Qc0k/edit#gid=867375299
"""

# how delete duplicates in excel file and make new
data = pd.read_excel("remove.xlsx")
data.drop_duplicates(subset='Название: ', keep=False, inplace=True, ignore_index=True)
df = data
df.to_excel('output.xlsx')


"""
Was 2389 and now 2204... more clear
new link:
https://docs.google.com/spreadsheets/d/16_yXQjZK4W9SFjgZgF9D1T_q3ZY7M-Ry/edit?usp=sharing&ouid=118018907937942825608&rtpof=true&sd=true

"""
