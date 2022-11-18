"""
IMDb Top 250 Movies
"""

import requests
from bs4 import BeautifulSoup
import json
import pandas as pd

URL = 'https://www.imdb.com/chart/top/'
headers = {
    'Accept': '*/*',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
}

dct = {}
json_list = []
req = requests.get(URL, headers=headers)
soup = BeautifulSoup(req.text, 'lxml')

# films = soup.find(class_='lister-list').find_all('tr')
#
# for film in films:
#     name = film.find('td', class_='titleColumn').a.text
#     rank = film.find('td', class_='titleColumn').text.strip().split('.')[0]
#     year = film.find('td', class_='titleColumn').span.text.replace('(', '').replace(')', '')
#     rating = film.find('td', class_='ratingColumn imdbRating').strong.text
#     print(rating)



# lst = []
# rating = soup.find_all(class_='ratingColumn imdbRating')
# for place in rating:
#     lst.append(place.text.strip())
#
#


def collecting_info():
    films = soup.find(class_='lister-list').find_all('tr')
    for film in films:
        place = film.find(class_='titleColumn').text.split('.')[0].strip()
        # name = film.find(class_='titleColumn').a.text
        # year = film.find(class_='titleColumn').span.text
        # rating = film.find(class_='ratingColumn imdbRating').strong.text
        # return place, name, year, rating
        return place


print(collecting_info())

# def save_json_file():
#     with open('top 250 films.json', 'a', encoding='utf-8') as file:
#         json.dump(lst, file, indent=4, ensure_ascii=False)


# def from_json_to_excel():
#     with open('top 250 films.json', encoding='utf-8') as json_file:
#         data = json.load(json_file)
#
#     df = pd.DataFrame(data)
#     return df.to_excel('top 250 films.xlsx')


# save_json_file()
# from_json_to_excel()
