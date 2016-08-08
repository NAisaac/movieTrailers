# Movie Trailer Website 

A server-side code to store a list of my favorite movies, with poster images and a movie trailer URL + serve this data as a web page allowing visitors to review the movies and watch the trailers.
* entertainment_center.py: this is the main code that uses modules (media.py & fresh_tomatoes.py) to create movie objects and display them on a website
`python entertainment_center.py`
* media.py: this module defines a class(data structure) to store movies' data (i.e. title, storyline, poster image, trailer)
* fresh_tomatoes.py: this module has a function called *open_movies_page* that takes in one argument, which is a list of movie objects, and creates an HTML file which visualizes all of those movies

