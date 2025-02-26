"""RateMyMovie URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from api.views import home, loginuser, signupuser, movie_ratings, logoutuser, MovieListAPIView, MovieRetrieveUpdateDestroyAPIView, RatingCreateAPIView, RatingListAPIView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    # admin
    path('admin/', admin.site.urls),

    # app
    path("", home, name="home"),
    path("login/", loginuser, name="loginuser" ),
    path("signup/", signupuser, name="signupuser" ),
    path("logout/", logoutuser, name="logoutuser" ),
    path("movie_ratings/", movie_ratings, name="movie_ratings" ),

    # api
    path("api/movies", MovieListAPIView.as_view(), name="movies"),
    path("api/movies/<int:pk>", MovieRetrieveUpdateDestroyAPIView.as_view(), name="movie"),
    path("api/movies/<int:pk>/ratings", RatingListAPIView.as_view(), name="ratings"),# might delete this later, as this one is not needed
    path("api/movies/<int:pk>/rate", RatingCreateAPIView.as_view(), name="rate"),

    #obtaining auth token
    path("get-token/", obtain_auth_token, name="get-token"),

]
