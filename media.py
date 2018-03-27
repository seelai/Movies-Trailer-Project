import webbrowser

class Movie():
    """ This class provides a way to store movie related information

        Attributes:
            title - Movie title
            storyline - About this movie
            poster_image_url - URL to image that displays the movie poster
            trailer_youtube_url - URL to youtube video showing the trailer

        Functions:
            show_trailer - open the trailer in new window using given url 
    """
    
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url =  poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
        
