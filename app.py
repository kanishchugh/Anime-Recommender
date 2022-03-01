from crypt import methods
from urllib import request
from flask import Flask, render_template, request
from anime import similar_anime
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def getvalue():
    name = request.form['Name']
    data = similar_anime(name)
    anime_one = data[1:]
    print(len(data))
    return render_template('results.html',name=name, anime_one=anime_one)

if __name__ == "__main__":
    app.run()