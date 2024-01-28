# IMDb Rating Retrieval Script

This Python script uses the IMDbPY library to retrieve IMDb ratings for a list of movies.

## Prerequisites

- Python installed on your system.
- IMDbPY library installed. You can install it using:

  ```bash
  pip install IMDbPY

**How to Use**
Copy and paste the provided Python script into your Python environment.

Run the script.

bash
python imdb_rating_script.py
The script will search for IMDb ratings for a static list of 10 movies and display the results.

**Script Overview**
The script uses the IMDbPY library to search for movies and retrieve their ratings from IMDb.

It includes a static list of 10 movie names.

The get_imdb_rating function takes a movie name as input, searches for it on IMDb, and returns the IMDb rating.

The script then iterates through the static list of movies, retrieves and displays IMDb ratings.

**Note**
IMDb ratings are obtained using the IMDbPY library, and the accuracy of ratings depends on the data available on IMDb.

Ensure that you have an internet connection while running the script as it fetches data from IMDb.
