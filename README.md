# Website: movie favorites.
Simple movie trailer website to exercise some programming foundations with python.

![](http://image-store.slidesharecdn.com/c88c88e8-af48-4586-9290-c5faf39499b5-large.jpeg)


## Detailed Description
The website shows nine of my favorite movies with additional infos pulled from the [OMDb API][3]:
- Poster image
- Title
- Year
- List of genres separated by dashes
- Plot with maximum of 150 characters (if longer, truncated with '...').
- imdb-Rating

Additionally to the OMDb-Infos, an English trailer from [YouTube][4] is added for each of the movies.

## Requirements
[Python 2.7][5] installed

## Running Instructions
Generate the file `fresh_tomatoes.html`by running `$ python entertainment_center.py` from the command prompt. By clicking on the movies, a modal opens up and the trailer is played.

[1]: https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004 "Udacity Nanodegree: Full Stack Web Developer"
[2]: https://www.udacity.com/course/programming-foundations-with-python--ud036-nd "Udacity Course: Programming Foundations with Python"
[3]: http://www.omdbapi.com/ "OMDb API - The Open Movie Database"
[4]: https://www.youtube.com/ "YouTube Website"
[5]: https://www.python.org/downloads/ "Download Python"
