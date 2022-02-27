#Fututre improvements- Improve the redundancy  
import csv
import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
n = [x+1 for x in range(50)]
anime = []
for x in range(508):
    index = '/'.join(map(str,n))
    url = 'https://cdn.animenewsnetwork.com/encyclopedia/nodelay.api.xml?title=%s}'%(index)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'xml')
    anime.append(soup.find_all('anime'))
    n = [x+50 for x in n]

with open('data/AnimeData.csv', 'w') as f:
    writer = csv.writer(f)
    Headers = ['MainTitle', 'Type','Genre', 'Weighted_Score', 'Themes', 'Summary']
    writer.writerow(Headers)
    for i in range(len(anime)):
        for j in range(len(anime[i])):
                #Titles
                try:
                    Title = anime[i][j].find_all(type = 'Main title')
                    Title = Title[0].text
                except IndexError:
                    pass
                #Types
                Type = anime[i][j].get('precision')
                #Genres
                Genres = []
                Genre = anime[i][j].find_all(type = 'Genres')
                for text in range(len(Genre)):
                    Genres.append(Genre[text].text)
                #Weighted score
                try:
                    Weighted_score = anime[i][j].find('ratings').get('weighted_score')
                except AttributeError:
                    Weighted_score = 0
                #Theme
                Theme = anime[i][j].find_all(type = 'Themes')
                if not Theme:
                    Theme = 'No Theme Found'
                try:
                    for Themes in range(len(Theme)):
                        Theme[Themes] = Theme[Themes].text
                except AttributeError:
                    Theme = 'No Theme Found'
                #Summary
                try:
                    Summary = anime[i][j].find(type = 'Plot Summary').text
                    if not Summary:
                        Summary = 'No summary found'
                except AttributeError:
                    Summary = 'No summary found'
                AnimeList = [Title, Type, Genres, Weighted_score, Theme, Summary]
                writer.writerow(AnimeList)
            