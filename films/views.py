from rest_framework import generics
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Actor, Comment, Movie
from .serializers import CommentListSerializer, MovieListSerializer , ActorSerializer 
from django.contrib.postgres.search import TrigramSimilarity


class MovieList(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieListSerializer
    filter_backends = [OrderingFilter]
    ordering_fields = ['imdb', ]

    def get_queryset(self):
        queryset = Movie.objects.all()
        ism = self.request.query_params.get('search')
        if ism is not None:
            queryset = Movie.objects.annotate(
                    similarity=TrigramSimilarity(
                        'name',ism
                    )).filter(similarity__gt=0.3)
        return queryset



class MovieDetailView(generics.RetrieveAPIView): 
    queryset = Movie.objects.all() 
    serializer_class = MovieListSerializer   

class MovieUpdateView(generics.RetrieveUpdateAPIView): 
    queryset = Movie.objects.all() 
    serializer_class = MovieListSerializer  

class ActorCreateListView(generics.ListCreateAPIView): 
    queryset = Actor.objects.all() 
    serializer_class = ActorSerializer  
    filter_backends = [SearchFilter, OrderingFilter, ]  
    search_fields = ["name", "id", ]
    ordering_fields = ["birth_date", ]

class ActorDetailView(generics.RetrieveAPIView): 
    queryset = Actor.objects.all() 
    serializer_class = ActorSerializer  

class ActorDeleteView(generics.RetrieveDestroyAPIView): 
    queryset = Actor.objects.all() 
    serializer_class = ActorSerializer 

class CommentListCreateView(generics.ListCreateAPIView): 
    queryset = Comment.objects.all() 
    serializer_class = CommentListSerializer  


    