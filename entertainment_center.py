# -*- coding: utf-8 -*-
# The above comment allows Korean characters

from media import Movie
from fresh_tomatoes import open_movies_page
import pdb

fiftyfirst = Movie("50 First Dates", 
	"A haole playboy finds love due to unforeseen circumstances",
	"http://www.sonypictures.com/movies/50firstdates/assets/images/onesheet.jpg",
	"https://www.youtube.com/watch?v=ErjP5xMTc8I")

my_sassy_girl2 = Movie("엽기적인 그녀 2", 
	"The sequel to 엽기적인 그녀", 
	"http://asianwiki.com/images/3/39/My_New_Sassy_Girl-p01.jpeg", 
	"https://www.youtube.com/watch?v=97wMzHzsd8Y")

pets = Movie("Secret Life of Pets",
	"A story about what pets REALLY do when alone",
	"https://upload.wikimedia.org/wikipedia/en/6/64/The_Secret_Life_of_Pets_poster.jpg",
	"https://www.youtube.com/watch?v=i-80SGWfEjM")

suicide = Movie("Suicide Squad",
	"Criminals combat the real crimals",
	"http://cdn.collider.com/wp-content/uploads/2016/06/suicide-squad-imax-poster.jpg",
	"https://www.youtube.com/watch?v=CmRih_VtVAs")

up = Movie("Up!",
	"An unexpected travel to Paradise Lost",
	"http://www.tourismnewwestminster.com/wp-content/uploads/2014/06/Up-2009.jpg",
	"https://www.youtube.com/watch?v=pkqzFUhGPJg")

mad_king = Movie("광해",
	"The beggar and the mad king",
	"https://image-proxy.namuwikiusercontent.com/r/http%3A%2F%2Fimg.movist.com%2F%3Fimg%3D%2Fx00%2F04%2F40%2F40_p1.jpg",
	"https://www.youtube.com/watch?v=hQCns1AwlIA")

# Let's see what the documentation on Movie is...
print('\n'+Movie.__doc__+'\n')

# open_movies_page takes a list of movie objects and creates a web page
movies = [fiftyfirst, mad_king, up, my_sassy_girl2, pets, suicide]
open_movies_page(movies)
