from imdb import IMDb

def get_imdb_rating(movie_name):
    ia = IMDb()
    movies = ia.search_movie(movie_name)

    if not movies:
        return None  # Movie not found

    first_movie = movies[0]
    ia.update(first_movie)

    return first_movie.data['rating']

# Static list of 10 movie names
movie_names = [
    "Inception",
    "The Shawshank Redemption",
    "The Godfather",
    "Pulp Fiction",
    "The Dark Knight",
    "Forrest Gump",
    "The Matrix",
    "Titanic",
    "Avatar",
    "Interstellar"
]

# Get and display IMDb ratings for each movie
for movie_name in movie_names:
    rating = get_imdb_rating(movie_name)
    
    if rating is not None:
        print(f"The IMDb rating of '{movie_name}' is: {rating}")
    else:
        print(f"Sorry, '{movie_name}' not found on IMDb.")
