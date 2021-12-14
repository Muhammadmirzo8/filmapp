
from django.test import TestCase, Client
from films.models import *
from films.serializers import MovieListSerializer

class TestMovieListView(TestCase):
    def setUp(self): 
        self.actor = Actor.objects.create(name="Leonardo DiCaprio", gender="Male", birth_date="1970-12-12")  
        self.movie = Movie.objects.create(name='Squid Game', year="1970-12-12", imdb=3.2, genre="Drama")  
        self.movie.actor.add(self.actor)
        self.cl = Client() 

    def test_all_movies(self):
     movies = self.cl.get("/Netflix/films/").data
     self.assertEqual(len(movies), 1) 
     assert movies[0]['id'] is not None 
     assert movies[0]['name'] == 'Squid Game' 
     assert movies[0]['genre'] == 'Drama' 
     assert movies[0]['imdb']  == 3.2  
     assert movies[0]['actor']['name'] == "Leonardo DiCaprio"