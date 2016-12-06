import webbrowser
from video import Video

class Movie(Video):
    """ This class provides a way to store movie related information,
        inherits from video class """

    VALID_RATINGS = ["G", "PG", "PG-13", "R", "NR"]

    def __init__(self, movie_title, movie_duration, movie_storyline,
                 poster_image, trailer_youtube):
        Video.__init__(self, movie_title, movie_duration, movie_storyline)
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
