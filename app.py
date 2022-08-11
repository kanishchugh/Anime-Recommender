from crypt import methods
from typing_extensions import Self
from urllib import request
from flask import Flask, render_template, request
from processing import Recommendation
app = Flask(__name__)

reccomendations = Recommendation()
reccomendations.data_processing()
reccomendations.recommendation_list()
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def getvalue():
    name = request.form['Name']
    data = reccomendations.recommended_anime(name)
    anime_one = data[0]
    print(len(data))
    return render_template('results.html',name=name, data=data)

if __name__ == "__main__":
    app.run()