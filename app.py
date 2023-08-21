from flask import Flask, render_template, request, redirect, url_for, session
from pymongo import MongoClient
from datetime import datetime

app = Flask(__name__)

mongo_uri = "mongodb+srv://bahetiharsh04:harsh2704@cluster0.znbfwzv.mongodb.net/"
client = MongoClient(mongo_uri)
db = client['movie_app']
dbmovies = db.movies
userLogin = db.register
genres = db.genre
dbreviews = db.reviews

# Routes

@app.route('/')
def index():
    movies = dbmovies.find()
    return render_template('index.html', movies=movies)


@app.route('/create_user', methods=['POST'])
def create_user():
    message = ''
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")

        email_found = userLogin.find_one({"email": email})
        if email_found:
            message = 'This email already exists in the database'
            return redirect(url_for('index', message=message))
        else:
            user_input = {'email': email, 'password': password}
            userLogin.insert_one(user_input)
            return redirect(url_for('logged_in'))
    return redirect(url_for('index'))

@app.route('/create_genre', methods=['POST'])
def create_genre():
    enter_genre = request.form.get("genre")
    genre_found = genres.find_one({"genre": enter_genre})
    if genre_found:
        message = 'Genre already available.'
        return redirect(url_for('index', message=message))
    else:
        genres.insert_one({"genre": enter_genre})
        return redirect(url_for('index'))

@app.route('/create_movie', methods=['POST'])
def create_movie():
    if request.method == "POST":
        movie_id = request.form.get("mid")
        name = request.form.get("name")
        description = request.form.get("description")
        genre = request.form.get("genre")
        releaseDate = request.form.get("releaseDate")

    movie_input = {'mid': movie_id, 'name': name,
                   'description': description, 'genre': genre, 'releaseDate': releaseDate}
    dbmovies.insert_one(movie_input)
    return redirect(url_for('index'))


@app.route('/update_movie', methods=['GET', 'POST'])
def update_movie(movie_id):
    update = request.form.get("update")
    if update:
        movie_id = request.form.get("mid")
        udescription = request.form.get("updateDescription")
        ugenre = request.form.get("updateGenre")
        ureleaseDate = request.form.get("updateReleaseDate")
        dbmovies.update({'mid': movie_id}, {'$set': {
                        'description': udescription, 'genre': ugenre, 'releaseDate': ureleaseDate}})
    return redirect(url_for('index'))


@app.route('/list_movies', methods=['GET'])
def list_movies():
    genre = request.form.get("genre")
    date = request.form.get("releaseDate")
    movies = dbmovies.find({'genre': genre, 'releaseDate': date})
    return render_template('movie_list.html', movies=movies)


@app.route('/add_review', methods=['POST'])
def add_review(movie_id):
    review = request.form.get('review')
    movie_id = request.form.get("mid")
    reviews = {'mid': movie_id, 'review': review}
    dbreviews.insert_one(reviews)
    return redirect(url_for('index'))


@app.route('/fetch_reviews', methods=['GET'])
def fetch_reviews(movie_id):
    name = request.form.get("name")
    id = request.form.get("mid")
    review = dbreviews.find_one({"mid": id})
    return render_template('reviews.html', reviews=review.reviews)


if __name__ == '__main__':
    app.run(debug=True)