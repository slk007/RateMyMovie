from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models import Avg

# signals for automating token generation
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings


class Movie(models.Model):
    title = models.CharField(max_length=300, null=False, unique=True)
    story = models.TextField()
    genre = models.CharField(max_length=10)
    released_year = models.CharField(max_length=4)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    average_rating = models.FloatField(default=0.0)

    def __str__(self):
        return str(self.title)


class Rating(models.Model):
    given_by = models.ForeignKey(User, on_delete=models.CASCADE)
    for_movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(10)])

    def __str__(self):
        return str(self.given_by.username) + " rated " + str(self.for_movie) + " - " + str(self.rating) + " stars"


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def createAuthToken(sender, instance, created, **kwargs):
    if created:
        Token.objects.create(user=instance)


def cal_average():
    for movie in Movie.objects.all():
        all_ratings = Rating.objects.filter(for_movie=movie)
        if all_ratings:
            avg = all_ratings.aggregate(Avg('rating'))['rating__avg']
            movie.average_rating = avg
            movie.save()
        else:
            movie.average_rating = 0.0
            movie.save()


@receiver(post_save, sender=Rating)
def calculateAverageRating(sender, instance, **kwargs):
    cal_average()

@receiver(post_delete, sender=Rating)
def calculateAverageRatingAfterDeletion(sender, instance, **kwargs):
    cal_average()