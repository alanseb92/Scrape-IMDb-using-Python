from imdb import IMDb
movie = IMDb().get_movie('012346')
print(movie)


#Now let’s see how to scrape IMDb using Python. I will start this task by searching for a movie id randomly to see which movie is associated with the id:
for i in movie["directors"]:
    print(i)
    
 #Now let’s have a look at the directors of this movie:   
movies = IMDb().get_top250_movies()
for i in movies:
    print(i)
    
