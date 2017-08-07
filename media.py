import webbrowser

"""Video will be the super class.
TV and Video will inherit from this class"""


class Video():
    # Class Variable / Global Variable
    VIDEO_RATINGS = ['G', 'PG', 'PG-13', 'R', 'MA']

    # constructor function for Video.
    # self as a convention, and the following Video arguments
    def __init__(
            self,
            title,
            story_line,
            poster_image_url,
            trailer_youtube_url,
            ratings
            ):
            # the following are instance variables
            self.title = title
            self.story_line = story_line
            self.poster_image_url = poster_image_url
            self.trailer_youtube_url = trailer_youtube_url

            self.ratings = ratings

    # method left in the Parent class.
    # Movie and Television will inherit the use of this method.
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)


"""Movie is a 'child' class to Video"""


class Movie(Video):
    # Movie constructor
    def __init__(
            self,
            title,
            story_line,
            poster_image_url,
            trailer_youtube_url,
            ratings,
            yr
            ):

        # Video constructor passed into
        Video.__init__(
            self,
            title,
            story_line,
            poster_image_url,
            trailer_youtube_url,
            ratings
            )

        # instance variables inherited from Video class
        self.title = title
        self.storyline = story_line
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
        self.ratings = ratings

        # Movie argument not inherited from Video
        self.year = yr


"""Television is a 'child' class to Video"""


class Television(Video):
    # Television Constructor
    def __init__(
            self,
            title,
            story_line,
            poster_image_url,
            trailer_youtube_url,
            ratings,
            tv_seasons
            ):
        # Video Constructor
        Video.__init__(
            self,
            title,
            story_line,
            poster_image_url,
            trailer_youtube_url,
            ratings
            )
        # instance variables inherited from Video class
        self.title = title
        self.story_line = story_line
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
        self.ratings = ratings

        # Television argument not inherited from Video
        self.seasons = tv_seasons
