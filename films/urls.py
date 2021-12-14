from django.urls import path  
from films.views import *

urlpatterns = [

    path("films/", MovieList.as_view()),  
    path("film/<int:pk>", MovieDetailView.as_view()),    
    path("film/update/<int:pk>", MovieUpdateView.as_view()),   
    path("actors/", ActorCreateListView.as_view()),   
    path("actor/<int:pk>", ActorDetailView.as_view()),   
    path("actor/delete/<int:pk>", ActorDeleteView.as_view()),  
    path("comments/", CommentListCreateView.as_view()), 
    

]