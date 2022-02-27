import numpy as np
import pandas as pd

anime = pd.read_csv('./data/AnimeData.csv')

def PreProcessing(anime):
    #Cleaning data
    #Deleting null ratings
    anime['Weighted_Score'] = anime['Weighted_Score'].apply(lambda x: np.nan if x==0 else x)
    anime['Genre'] = anime['Genre'].apply(lambda x: np.nan if x==0 or x=='[]' else x)
    anime.dropna(inplace=True)
    #setting index
    anime['index'] = range(len(anime))
    anime['Index'] = range(len(anime))
    anime.set_index('index', inplace = True)

    #Converting Genre from str to list
    for i in range(len(anime)):
        try:
            # anime['Themes'][i] = ast.literal_eval(anime['Themes'][i])
            anime['Genre'][i] = ast.literal_eval(anime['Genre'][i])
        except:
            pass

    unique_genres = ['None', 'action', 'adventure', 'comedy', 'drama', 'erotica', 'fantasy', 'horror', 'magic', 'mystery', 
                        'psychological', 'romance', 'science fiction', 'slice of life', 'supernatural', 'thriller', 'tournament']
    anime['Joined'] = ' '
    for i in range(len(anime)):  
        anime['Joined'][i] = ' '.join(anime['Genre'][i])+ ' ' + str(anime['Weighted_Score'][i])
    return anime