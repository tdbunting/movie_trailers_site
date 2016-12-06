from lib import media_lookup
from lib import fresh_tomatoes

# Set your list of movies you want to show on your site
movies_to_fetch = [
    'Almost Famous',
    'The Producers',
    'Hook',
    'Young Frankenstein',
    'Dazed and Confused',
    'Memento',
    'What about Bob',
    'Deathtrap',
    'The Prestige',
    'Inception'
]

movies_to_display = []

# for each movie in the movies_to_fetch array, search for the movie,
# if the movie was found add returned movie to the list of movie objects to display
for movie_title in movies_to_fetch:
    movie = media_lookup.fetch_movie_information(movie_title)
    if movie != None:
        movies_to_display.append(movie)

# Pass movie objects into fresh_tomatoes Web server and open the page with the given list of movies
if len(movies_to_display) is not 0:
    fresh_tomatoes.open_movies_page(movies_to_display)
