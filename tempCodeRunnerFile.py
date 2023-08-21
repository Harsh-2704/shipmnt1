# Routes
# @app.route('/')
# def index():
#     movies = db.movies.find()
#     return render_template('index.html', movies=movies)

# @app.route('/create_user', methods=['POST'])
# def create_user():
#     # Handle user registration logic using MongoDB
#     return redirect(url_for('index'))

# @app.route('/create_genre', methods=['POST'])
# def create_genre():
#     # Handle genre creation logic using MongoDB
#     return redirect(url_for('index'))

# @app.route('/create_movie', methods=['POST'])
# def create_movie():
#     # Handle movie creation logic using MongoDB
#     return redirect(url_for('index'))

# @app.route('/update_movie/<string:movie_id>', methods=['GET', 'POST'])
# def update_movie(movie_id):
#     # Handle movie update logic using MongoDB
#     return redirect(url_for('index'))

# @app.route('/list_movies', methods=['GET', 'POST'])
# def list_movies():
#     # Handle movie listing and filtering logic using MongoDB
#     return render_template('movie_list.html', movies=movies)

# @app.route('/add_review/<string:movie_id>', methods=['POST'])
# def add_review(movie_id):
#     # Handle review creation logic using MongoDB
#     return redirect(url_for('index'))

# @app.route('/fetch_reviews/<string:movie_id>')
# def fetch_reviews(movie_id):
#     # Handle fetching reviews for a movie using MongoDB
#     return render_template('reviews.html', reviews=reviews)

# if __name__ == '__main__':
#     app.run(debug=True)
