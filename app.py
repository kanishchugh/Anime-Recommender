from urllib import request
from flask import Flask, render_template, request
from processing import Recommendation

reccomendations = Recommendation() #Creating an instance of the Reccomendation class
import os.path
if os.path.exists('Anime_Data.pkl'): #Checking if the pickle file exists or not
    app = Flask(__name__)
    @app.route('/')
    def index():
        return render_template('index.html') #Renders/Generate homepage based on Jinja2
    @app.route('/dashboard')
    def dashboard():
        return render_template('dashboard.html') #Renders/Generate Tableau dahsboard page
    @app.route('/', methods=['POST'])
    def getvalue():
        name = request.form['Name']
        data,name = reccomendations.recommended_anime(name) #Retrieving data from the 
        anime_name = data['Anime']
        anime_genre= data['Genre']
        anime_summary = data['Summary']
        return render_template('results.html',name=name[0], anime_name=anime_name,anime_genre=anime_genre,anime_summary=anime_summary) #Renders/Generate results page

    if __name__ == "__main__":
        app.run()
else: #If the pickle file does not exist we run the code to process the data as well as save the pickle file
    reccomendations.data_processing()
    reccomendations.recommendation_list()
