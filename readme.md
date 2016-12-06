# tdbunting's Movie Trailers
  ==========================

This script takes a collection of movie title strings,  
attempts to find movie information and trailer for each movie title provided,   
then generates and opens a webpage displaying each movie and its trailer.

# Requirements

- Python v2.7
- Requests v2.12.3
- themoviedb.org API Key


### To Setup

1. Clone the repository  
  ```
     git clone https://github.com/tdbunting/random-quote-generator
  ```
2. Make sure requests module is installed  
  ``` pip install requests ```<i>or</i> ``` easy_install requests ```
3. Sign up for an API Key at https://www.themoviedb.org/
4. Either:

  a. Store your api key in an Env Variable as THE_MOVIE_DB_API_KEY

  or

  b. Replace tmdb_api_key in config.json with your API KEY

5. If you would like to use this to populate your own favorite movies,
simply change the <i><b>movies_to_fetch</b></i> list inside of <b>movie_trailer_site.py</b> 
to contain your list of favorite movies.

### To Run
  Navigate into the project directory and run
  ```
     python movie_trailer_site.py
  ```

