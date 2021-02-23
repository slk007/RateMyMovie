from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

# movie
class Movie(models.Model):
    title = models.CharField(max_length=300, null=False, unique=True)
    story = models.TextField()
    genre = models.CharField(max_length=10)
    released_year = models.CharField(max_length=4)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    average_rating = models.FloatField(default=0.0)

    def __str__(self):
        return str(self.title)

# rating
class Rating(models.Model):
    given_by = models.ForeignKey(User, on_delete=models.CASCADE)
    for_movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(10)])

    def __str__(self):
        return str(self.given_by.username) + " rated " + str(self.for_movie) + " - " + str(self.rating) + " stars"
