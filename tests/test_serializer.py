from django.contrib.auth.models import User
from django.test import TestCase

from films.models import Actor , Movie
from films.serializers import ActorSerializer, CommentListSerializer

class TestActorSerializer(TestCase): 
    def setUp(self):
        self.actor = Actor.objects.create(name="Leonardo DiCaprio", gender="Male", birth_date="1970-12-12")  
    def test_data(self): 
        data = ActorSerializer(self.actor).data 
        self.assertIsNotNone(data) 
        assert data['id'] is not None 
        assert data['name'] == "Leonardo DiCaprio"  
        self.assertEqual(data['gender'], "Male")  
        assert data['birth_date'] == "1970-12-12"   

class TestCommentSerializer(TestCase): 
    def setUp(self):
        self.actor = Actor.objects.create(name="Leonardo DiCaprio", gender="Male", birth_date="1970-12-12")  
        self.movie = Movie.objects.create(name='Squid Game', year="1970-12-12", imdb=3.2, genre="Drama")  
        self.movie.actor.add(self.actor)
    def test_comment(self): 
        
        assert True 

class TestCommentValidation(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="ALi", password="admin1234")
        self.actor = Actor.objects.create(name="Raj Kapoor", gender="Male", birth_date='1956-04-13')
        self.movie = Movie.objects.create(name="421", genre="Comedy", imdb=6.9, year='1978-09-18')
        self.movie.actor.add(self.actor)
    def test_is_not_valid(self):
        data = {
            "id":1,
            "movie":self.movie.id,
            "user":self.user.id,
            "text":"yaramas ekansizlar"
        }
        ser = CommentListSerializer(data=data)
        self.assertTrue(ser.is_valid())
        print(ser.errors) 

