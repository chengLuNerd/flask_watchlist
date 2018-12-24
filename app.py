from flask import Flask, url_for, render_template

name = "Lucheng"

movies = [
        {'title': 'My neighbor totoro', 'year': '1988'},
        {'title': 'The pork of music', 'year': '2012'}
]



app = Flask(__name__)

@app.route("/home")
@app.route("/")
@app.route("/index")
def hello():
    return render_template('index.html', name=name, movies=movies)


@app.route('/user/<name>')
def user_page(name):
    return 'User: %s' % name

@app.route('/test')
def test_url_for():
    print(url_for('hello'))
    print(url_for('user_page', name='greyli'))


    return 'Test page'

