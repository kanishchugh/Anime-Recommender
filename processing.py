import numpy as np
from sentence_transformers import SentenceTransformer
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import difflib
from joblib import Parallel, delayed
import joblib

class Recommendation:
    def __init__(self, location ='./data/OTAKU_Data.csv'): #Loading the database
        self.data = pd.read_csv(location)
        
    def data_processing(self): 
        self.model = SentenceTransformer('distilbert-base-nli-mean-tokens') #Using sentence transformers 
        self.X = np.array(self.data.Summary)
        self.data = self.data[['MainTitle','Genre','Summary']] #Filtering out data
        text_data = self.X
        embeddings = self.model.encode(text_data)
        embed_data = embeddings
        self.X = np.array(embed_data) 
        self.cos_sim_data = pd.DataFrame(cosine_similarity(self.X)) #Calculating cosine similarity 

    def give_recommendations(self, index): #Giving reccommendations based on index
        index_recomm = self.cos_sim_data.loc[index].sort_values(ascending=False).index.tolist()[1:8]
        anime_name =  self.data['MainTitle'].loc[index_recomm].values
        anime_summary = self.data['Summary'].loc[index_recomm].values
        anime_genre = self.data['Genre'].loc[index_recomm].values
        self.result = [{'Anime':anime_name,'Index':index_recomm, 'Summary': anime_summary, 'Genre': anime_genre}]
        return self.result 

    def recommendation_list(self):
        self.recomm_list = []
        for i in range(len(self.X)):
            recomm_i = self.give_recommendations(i)
            self.recomm_list.append(recomm_i)
        self.recomm_data = pd.DataFrame(self.recomm_list)
        self.recomm_data['Watched_Anime'] = self.data['MainTitle']
        joblib.dump(self.recomm_data,'Anime_Data.pkl')

    def recommended_anime(self,name): #Driver code that gives the specific recommendation
        data = joblib.load('Anime_Data.pkl')
        names = data['Watched_Anime']
        closest_name = difflib.get_close_matches(name,names)
        self.anime_data = data.loc[(data.Watched_Anime == closest_name[0])].values[0][0]
        return self.anime_data, closest_name
        
