# import fres_tomatoes, media
import fresh_tomatoes
import media

# movies
# toy_story, school_of_rock will be instantiated as Movie objects.
# take in as arg (title, movie_story, poster, trailer, ratings, and year)
toy_story = media.Movie(
    "Toy Story",
    "A story of a boy and his toys",
    "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
    "https://www.youtube.com/watch?v=KYz2wyBy3kc",
    media.Video.VIDEO_RATINGS[0],
    1955)

school_of_rock = media.Movie(
    "School Of Rock",
    "A musician pretends to be a substitute music teacher",
    "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
    "https://www.youtube.com/watch?v=XCwy6lW5Ixc",
    media.Video.VIDEO_RATINGS[2],
    2003)

# television
# seinfeld and the_cosby_show will be instantiated as Television objects.
# Arguements, (title, story, poster, trailer, ratings, and seasons)
seinfeld = media.Television(
    "Seinfeld",
    "A show about 4 friends and nothing else.",
    "http://www.sonypictures.com/tv/seinfeld/assets/images/onesheet.jpg",
    "https://www.youtube.com/watch?v=dHh_ddv-dBE",
    media.Video.VIDEO_RATINGS[3],
    9)

the_cosby_show = media.Television(
    "The Cosby Show",
    "A doctor and lawyer raise their family in Brooklyn",
    "http://www.carseywerner.net/images/cosbyshow_main_max.jpg",
    "https://www.youtube.com/watch?v=NcodNEyTiSE",
    media.Video.VIDEO_RATINGS[2],
    8)

# To run the program, store the movie/television objects in an array
videos = [toy_story, school_of_rock, seinfeld, the_cosby_show]

# Call open_movies_page which will create the 'fresh_tomatoes' html file
fresh_tomatoes.open_movies_page(videos)
