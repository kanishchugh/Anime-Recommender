import os 
import csv
import requests
import mysql.connector
from bs4 import BeautifulSoup

n = [x+1 for x in range(50)]
data = []
for x in range(528): #Getting all the pages from the api
    index = '/'.join(map(str,n))
    url = 'https://cdn.animenewsnetwork.com/encyclopedia/nodelay.api.xml?title=%s}'%(index)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'xml')
    data.append(soup.find_all(['anime','manga']))
    n = [x+50 for x in n]    

DATABASE = mysql.connector.connect( #Connecting to the MySQL database
  host="localhost",
  user="root",
  password=""#Enter your own password here
  database = "OTAKU_DATABASE"
)

OTAKUcursor = DATABASE.cursor() # Defining the cursor
OTAKUcursor.execute("CREATE TABLE IF NOT EXISTS Anime(Title VARCHAR(150), Type VARCHAR(100), Genre VARCHAR(700), Weighted_score FLOAT(3), Themes VARCHAR(150), Summary VARCHAR(3000))") #Creating Anime table
OTAKUcursor.execute("CREATE TABLE IF NOT EXISTS Manga(Title VARCHAR(150), Type VARCHAR(100), Genre VARCHAR(700), Weighted_score FLOAT(3), Themes VARCHAR(150), Summary VARCHAR(3000))") #Creating Manga table
with open('./data/OTAKU_Data.csv', 'w') as database:
    writer = csv.writer(database)
    Headers = ['MainTitle', 'Type','Genre', 'Weighted_Score', 'Themes', 'Summary']
    writer.writerow(Headers)
    for i in range(len(data)):
        for j in range(len(data[i])):
                #Titles
                try:
                    Title = data[i][j].find_all(type = 'Main title')
                    if Title == []:
                        Title = 'No title found'
                    else:
                        Title = Title[0].text
                except IndexError:
                    pass
                #Types
                Type = data[i][j].get('precision')
                #Genres
                Genres = ''
                Genre = data[i][j].find_all(type = 'Genres')
                for text in range(len(Genre)):
                    if Genre == '[]':
                        Genres = 'No Genre found'
                    else:
                        Genres += str(Genre[text].text) + ", "
                #Weighted score
                try:
                    Weighted_score = data[i][j].find('ratings').get('weighted_score')
                except AttributeError:
                    Weighted_score = 0
                #Theme
                Theme = data[i][j].find_all(type = 'Themes')
                if not Theme:
                    Theme = 'No Theme Found'
                try:
                    for Themes in range(len(Theme)):
                        Theme[Themes] = Theme[Themes].text
                except AttributeError:
                    Theme = 'No Theme Found'
                #Summary
                try:
                    Summary = data[i][j].find(type = 'Plot Summary').text
                    if not Summary:
                        Summary = 'No summary found'
                except AttributeError:
                    Summary = 'No summary found'
                input = [(Title, Type, str(Genres), Weighted_score, Themes, Summary)]
                #Inserting data into tables
                if Type == 'Manga':
                    insert = "INSERT INTO Manga(`Title`, `Type`, `Genre`, `Weighted_score`, `Themes`, `Summary`) VALUES (%s, %s, %s, %s, %s, %s)"
                else:
                    insert = "INSERT INTO Anime(`Title`, `Type`, `Genre`, `Weighted_score`, `Themes`, `Summary`) VALUES (%s, %s, %s, %s, %s, %s)"
                #Commiting data into database
                OTAKUcursor.executemany(insert, input) 
                writer.writerow([Title, Type, Genres, Weighted_score, Theme, Summary])
DATABASE.commit() #commiting to the database
DATABASE.close() #closing the database
os.system('cd data') #getting into the data directory
os.system('mysqldump -u root -p%s OTAKU_DATABASE > OTAKU_DATABASE.sql'%'') #Enter password here  
