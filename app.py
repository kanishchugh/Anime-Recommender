from crypt import methods
from urllib import request
from flask import Flask, render_template, request
from processing import Recommendation


reccomendations = Recommendation()
reccomendations.data_processing()
reccomendations.recommendation_list()

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def getvalue():
    name = request.form['Name']
    data,name = reccomendations.recommended_anime(name)
    anime_name = data['Anime']
    anime_genre= data['Genre']
    anime_summary = data['Summary']
    return render_template('results.html',name=name[0], anime_name=anime_name,anime_genre=anime_genre,anime_summary=anime_summary)

if __name__ == "__main__":
    app.run()