from data_processing import PreProcessing
from similarity import similarity
import pandas as pd
#Defining Variables

anime = pd.read_csv('./data/AnimeData.csv')

anime = PreProcessing(anime)
cosine_sim = similarity(anime)
anime_user_likes = input('Enter anime')

def get_index_from_title(MainTitle):
    return anime[anime.MainTitle == MainTitle]['Index'].values[0]

def get_data_from_index(index):
     Title = anime[anime.index == index]['MainTitle'].values[0]
     Type = anime[anime.index == index]['Type'].values[0]
     Genre	= anime[anime.index == index]['Genre'].values[0]
     Summary = anime[anime.index == index]['Summary'].values[0]
     return Title,Type, Genre, Summary
def similar_anime(anime_user_likes):
    anime_index = get_index_from_title(anime_user_likes)
    similaranime = list(enumerate(cosine_sim[anime_index]))
    sorted_similar_anime = sorted(similaranime, key=lambda x:x[1], reverse=True)
    i=0
    for movie in sorted_similar_anime:
        print(get_data_from_index(movie[0]))
        i=i+1
        if i>4:
            break
similar_anime(anime_user_likes)