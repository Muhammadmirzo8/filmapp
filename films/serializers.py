from django.db.models import fields
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import Actor, Comment, Movie 

class MovieListSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Movie 
        fields = "__all__"  

    def validate_imdb(self, qiymat):
            if qiymat < 2.0:
                raise ValidationError(detail="Uzr kechirasiz bizda bunaqa past kinolar qabul qilinmaydi")
            return qiymat

class ActorSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Actor
        fields = "__all__"   

class CommentListSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Comment 
        fields = "__all__"  

        def validate_text(self, text): 
            a = "yaramas"
            if a in text:
                raise ValidationError(detail="Befarosat bo'lmang")
            return text
