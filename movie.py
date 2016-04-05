class Movie() :
    """This is movie information display class"""
        
    def __init__(self, movie_title, movie_storyline, star_cast, movie_rating, poster_image,trailer_youtube) :
        self.title = movie_title
        self.storyline = movie_storyline
        self.star = star_cast
        self.rating = movie_rating
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self) :
        webbrowser.open(self.trailer_youtube_url)
        
        
