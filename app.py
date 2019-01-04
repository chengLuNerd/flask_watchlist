from flask import Flask, render_template

name = "Lucheng"

movies = [
        {'title': 'My neighbor totoro', 'year': '1988'},
        {'title': 'The pork of music', 'year': '2012'},
        {'title': 'WALL-E', 'year':'2008'}
]


app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html', name=name, movies=movies)

