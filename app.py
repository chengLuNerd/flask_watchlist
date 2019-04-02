import os
import click
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

'''
name = "Lucheng"

movies = [
        {'title': 'My neighbor totoro', 'year': '1988'},
        {'title': 'The pork of music', 'year': '2012'},
        {'title': 'WALL-E', 'year':'2008'}
]
'''

app = Flask(__name__)
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(app.root_path, 'data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(20))


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(60))
    year = db.Column(db.String(4))


@app.cli.command()
@click.option('--drop', is_flag=True, help='Create after drop.')
def initdb(drop):
    """Initialize the database."""
    if drop:
        db.drop_all()
    db.create_all()
    click.echo('Initialized database.')


@app.cli.command()
def forge():
    """Generate fake data"""
    db.create_all()

    name = 'cheng.lu'

    movies = [
        {'title': 'My neighbor totoro', 'year': '1988'},
        {'title': 'The pork of music', 'year': '2012'},
        {'title': 'WALL-E', 'year':'2008'}
    ]

    user = User(name=name)
    db.session.add(user)
    for m in movies:
        movie = Movie(title=m['title'], year=m['year'])
        db.session.add(movie)

    db.session.commit()
    click.echo('Done.')


@app.route("/")
def index():
    user = User.query.first()
    movies = Movie.query.all()
    return render_template('index.html', user=user, movies=movies)


@app.errorhandler(404)
def page_not_found(e):
    user = User.query.first()
    return render_template('404.html', user=user), 404
