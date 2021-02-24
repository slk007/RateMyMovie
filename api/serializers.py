from rest_framework import serializers
from .models import Movie, Rating


class MovieSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Movie
        fields = "__all__"
        extra_kwargs = {
            'created_by' :{ 'read_only': True },
            'average_rating' :{ 'read_only': True },
        }


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['given_by', 'for_movie', 'rating']
        extra_kwargs = {
            'given_by' :{ 'read_only': True },
            'for_movie' :{ 'read_only': True },
        }