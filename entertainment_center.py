# entertainment_center.py

import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story", 
	"The story of a boy and his toys that come to life.", 
	"https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg", 
	"https://youtube.com/watch?v=vwyZH85NQC4")

avatar = media.Movie("Avatar", 
	"A marine on an alient planet", 
	"https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg", 
	"https://youtube.com/watch?v=-9ceBgWV8io")

willy_wonka = media.Movie("Willy Wonka and the Chocolate Factory", 
	"The classic tale of an eccentric chocolatier -- and a little boy who comes to know him.", 
	"https://upload.wikimedia.org/wikipedia/en/7/7f/WillyWonkaMoviePoster.jpg", 
	"https://www.youtube.com/watch?v=osOMV5EP40Y")

movies = [toy_story, avatar, willy_wonka]

# willy_wonka.show_trailer()
fresh_tomatoes.open_movies_page(movies)


