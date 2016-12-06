from movie import Movie

import requests
import json
import random
import os

api_error_message = """

    This Module Requires an API Key from https://www.themoviedb.org/

    To use this module either:
        1. set THE_MOVIE_DB_API_KEY as an ENV variable,
        2. set tmdb_api_key in config.json
        
"""

def has_config():
    config_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "config.json"))
    if os.path.isfile(config_path):
        return True
    else:
        return False

def check_config_file_for_key():
    config_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "config.json"))
    config = json.load(open(config_path, "r"))
    if config['tmdb_api_key']:
        return config['tmdb_api_key']
    else:
        return None


# try to get tmdb_api_key from ENV variable first
tmdb_env_var = os.environ.get('THE_MOVIE_DB_API_KEY')

# if the ENV variable exists, set it to the api key
if tmdb_env_var is not None:
    tmdb_api_key = tmdb_env_var
#if the ENV variable doesnt exist, and has config file, check the config file for tmdb_api_key
elif tmdb_env_var is None and has_config():
    config_key = check_config_file_for_key()
    if config_key is not None:
        tmdb_api_key = config_key
    else:
        tmdb_api_key = None
else:
    raise Exception(api_error_message)

def fetch_movie_information(movie_title):
    """Takes movie_title as a string and fetches movie information from omdb api,
        Returns a Movie object"""

    omdb_url = 'http://www.omdbapi.com/?t=' + movie_title
    req = requests.get(omdb_url)
    movie = req.json()
    if req.json()['Response'] == "False":
        print("Sorry, we are having troubles finding " + movie_title)
        return None
    else:
        youtube_url = fetch_movie_trailer_url(movie['imdbID'])
        return create_movie(movie, youtube_url)

def fetch_movie_trailer_url(imdb_id):
    """Takes imdb_id as a string and fetches trailer information from tmdb api,
       returns a youtube url"""

    if not tmdb_api_key:
        raise Exception("tmdb_api_key is not present")

    tmdb_url = "https://api.themoviedb.org/3/movie/" + imdb_id + "/videos?api_key=" + tmdb_api_key
    req = requests.get(tmdb_url)

    # if the api key is invalid raise an error
    if(req.status_code == 401):
        raise Exception(req.json()['status_message'])
    # if the imdb_id is invalid, or a trailer cannot be found, return None
    elif (req.status_code == 404):
        print("Sorry we could not find a trailer for imdb #" + imdb_id)
        return None
    else:
        trailers = req.json()['results']
        # If there is only one trailer in the response, return created youtube url
        if len(trailers) == 1:
            return create_youtube_url(trailers[0]['key'])
        else:
            # choose a random one and return created youtube url
            trailer = choose_random_movie_trailer(trailers)
            return create_youtube_url(trailer['key'])

# takes in a list of trailer objects from tmdb for a movie and returns a random one
def choose_random_movie_trailer(trailers):
    for trailer in trailers:
        # if the object is not actully a trailer, remove it from the list
        if 'Trailer' not in trailer['name']:
            trailers.remove(trailer)
            print('Removing ' + trailer['name'] + ' from list of possible trailers')
    random_trailer = random.choice(trailers)
    return random_trailer

# takes in a youtube id string and returns full youtube url
def create_youtube_url(youtube_id):
    return 'https://www.youtube.com/watch?v=' + youtube_id

# takes a movie object from omdb along with a youtube url and returns a new movie object
def create_movie(movie, youtube_url):
    return Movie(movie["Title"], movie["Runtime"], movie["Plot"], movie["Poster"], youtube_url)
