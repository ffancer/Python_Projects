"""
requests, beautifulsoup, lxml, json

собираем карточки фестивалей который будет джсон файлом
upd. for version 1.1:
-работа с карточкой фестиваля (плохо парсится не понятна причина)
-место проведения
-мб че еще
"""
import requests
from bs4 import BeautifulSoup
import json


# url = 'https://www.skiddle.com/festivals/'
test_url = 'https://www.skiddle.com/festivals/Baltic-Weekender/'
headers = {
    'Accept': '*/*',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
}


# def collect_links():
#     req = requests.get(url, headers=headers)
#     soup = BeautifulSoup(req.text, 'lxml')
#     tables = soup.find_all('table')
#     links_list = []
#
#     for table in tables:
#         for item in table.find_all('a'):
#             # collect urls in list
#             if item.get('href') is not None:
#                 links_list.append('https://www.skiddle.com' + item.get('href'))
#
#     return links_list
#
#
# def collect_infomation():
#     json_list = []
#
#     for url in collect_links():
#         req = requests.get(url=url, headers=headers)
#         soup = BeautifulSoup(req.text, 'lxml')
#         name = soup.find('h1', class_='MuiTypography-root MuiTypography-body1 css-r2lffm').text
#         date = soup.find('div', class_='MuiGrid-root MuiGrid-item MuiGrid-grid-xs-11 css-twt0ol').text
#         description = soup.find('div', class_='MuiBox-root css-1ebprri').text[:-10]
#         image = soup.find(class_='css-1x26sxc')['data']
#         ticket = url + '#tickets'
#
#         json_list.append(
#             {
#                 'Url': url,
#                 'Name': name,
#                 'Date': date,
#                 'Description': description,
#                 "Festival's image": image,
#                 'Buy ticket': ticket
#             }
#         )
#
#     return json_list
#
#
# def save_json_file():
#     with open('festivals.json', 'a', encoding='utf-8') as file:
#         json.dump(collect_infomation(), file, indent=4, ensure_ascii=False)
#
#
# save_json_file()

req = requests.get(test_url, headers=headers)
soup = BeautifulSoup(req.text, 'html.parser')



# основа карточки:
# divs = soup.find('div', class_='MuiContainer-root MuiContainer-maxWidthLg css-zd1mrw')

card = soup.find('div', class_='MuiGrid-root MuiGrid-container MuiGrid-spacing-xs-2 css-1ik2gjq')
print(card.text)