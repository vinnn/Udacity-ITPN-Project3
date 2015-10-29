# Definition of Classes

# (code partially taken from Udacity Nanodegree 'Intro to Programming' Stage 3 lessons,
# https://www.udacity.com/course/intro-to-programming-nanodegree--nd000)


import webbrowser

class Movie():
    # This class contains movie data

    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube, movie_type, movie_year, movie_stars):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.movie_type = movie_type
        self.movie_year = movie_year
        self.movie_stars = movie_stars

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
        
        
