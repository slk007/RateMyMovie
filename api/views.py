from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.db.models import Avg
from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework import generics, permissions
from rest_framework import status
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .serializers import MovieSerializer, RatingSerializer
from .models import Movie, Rating

def get_average_rating():
    for movie in Movie.objects.all():
        all_ratings = Rating.objects.filter(for_movie=movie)
        if all_ratings:
            avg = all_ratings.aggregate(Avg('rating'))['rating__avg']
            movie.average_rating = avg
            movie.save()
        else:
            continue

@login_required
def movie_ratings(request):
    if request.user.is_staff:
        get_average_rating()
        movies = Movie.objects.all().order_by('-average_rating')
        return render(request, 'movie_ratings.html', {'movies': movies})
    else:
        return redirect('home')

# Create your views here.
def home(request):
    get_average_rating()
    return render(request, 'home.html')

def loginuser(request):
    if request.method == 'GET':
        return render(request, 'login.html', {'form':AuthenticationForm()})
    else:
        # user submits the details
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])

        if user is None:
            # authenticate returned a None i.e username or password is wrong
            return render(request, "login.html", {'form':AuthenticationForm(), 'error': "Username or password is wrong"})

        else:
            # username & password matched
            login(request, user)
            return redirect('home')

def signupuser(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {'form':UserCreationForm()})
    else:
        # whe request.method == "POST"
        # create a new user
        if request.POST['password1'] == request.POST['password2']:
            try:
                # if pass1 & pass2 match, then save user
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()

                # after saving user, login user
                login(request, user)

                # after login send user to his current page
                return redirect('home')

            except IntegrityError:
                # username is already present
                return render(request, 'signup.html', {'form': UserCreationForm(), 'error': "Username already present. Please choose any other"})
        else:
            # password1 and password 2 are not same
            return render(request, 'signup.html', {'form': UserCreationForm(), 'error': "Passwords didn't match"})

@login_required
def logoutuser(request):
    logout(request)
    return redirect('home')


class MovieListAPIView(generics.ListCreateAPIView):
    """ Generic API view for Movies Listing """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    authentication_classes = [BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]


class MovieRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """ Generic API view for Movies Detail, Update, Deletion """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    authentication_classes = [BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]


class RatingListAPIView(generics.ListAPIView):
    """ Generic API view for Listing Rating's Per Movie"""
    serializer_class = RatingSerializer
    authentication_classes = [BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        movie = Movie.objects.get(pk=self.kwargs['pk'])
        return Rating.objects.filter(for_movie=movie)


class RatingCreateAPIView(generics.CreateAPIView):
    """ Generic API view for Rating Movie"""
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    authentication_classes = [BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        movie = Movie.objects.get(pk=self.kwargs['pk'])
        return Rating.objects.filter(for_movie=movie)

    def perform_create(self, serializer):
        movie = Movie.objects.get(pk=self.kwargs['pk'])
        if movie.created_by == self.request.user:
            # movie was created by the current user himself
            raise ValidationError("You can't rate the movie created by yourself ...... !!! ")
        elif self.get_queryset().exists():
            # current user has already rated the movie
            raise ValidationError("You have already reviewed this Movie ...... !!!")
        else:
            # saving the rating given by current user
            serializer.save(given_by=self.request.user, for_movie=movie)
