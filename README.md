# Rate My Movie with REST API

![RATEMYMOVIE](https://github.com/slk007/RateMyMovie/blob/master/images/home.png)

* Inside this Project:
    * Django
    * Generic API Views
    * Bootstrap
    * PostgreSQL/SQLite
    * Signals
    * Authentication
    * [API.md](https://github.com/slk007/RateMyMovie/blob/master/API.md)
    * [ER Diagram](https://drawsql.app/personal-116/diagrams/ratemymovie#)
    * [Heroku Website](https://ratemymoviedj.herokuapp.com/)
    * [API Endpoints](https://github.com/slk007/RateMyMovie/blob/master/API.md)
    * [Django REST Framework](https://ratemymoviedj.herokuapp.com/api/movies)


* Assumptions:
    * User can only SIGNUP from the [Home page](https://ratemymoviedj.herokuapp.com/signup/).
    * Admins can view the list of all Movies with Ratings from [Notification](https://ratemymoviedj.herokuapp.com/movie_ratings/)

---

## API Endpoints:

* https://ratemymoviedj.herokuapp.com/get-token
* https://ratemymoviedj.herokuapp.com/api/movies
* https://ratemymoviedj.herokuapp.com/api/movies/int:movie_id
* https://ratemymoviedj.herokuapp.com/api/movies/int:movie_id/ratings
* https://ratemymoviedj.herokuapp.comapi/movies/int:movie_id/rate

---

## API Endpoints Usage: Postman

**Make a post request with username, password:**
![PostToken](https://github.com/slk007/RateMyMovie/blob/master/images/post_get_token.png)
You will get Token in response as below. Copy this Token as we need to use it for all our API Requests:
![ResponseToken](https://github.com/slk007/RateMyMovie/blob/master/images/response_token%20.png)

---  

**GET: List of All Movies with details**
Header with Token:
![GetMovies](https://github.com/slk007/RateMyMovie/blob/master/images/get_movies.png)
Response:
![ResponseMovies](https://github.com/slk007/RateMyMovie/blob/master/images/response_movies.png)

---

**GET: Details of specific Movie**
Header with Token:
![GetMovie](https://github.com/slk007/RateMyMovie/blob/master/images/get_a_movie.png)
Response:
![ResponseMovie](https://github.com/slk007/RateMyMovie/blob/master/images/response_a_movie.png)

---

**POST: Create a Movie**
Header with Token:
![PostMovie](https://github.com/slk007/RateMyMovie/blob/master/images/get_a_movie.png)
Body with Raw JSON Data:
![PostMovie2](https://github.com/slk007/RateMyMovie/blob/master/images/post_a_movie.png)
Response:
![ResponseCreateMovie](https://github.com/slk007/RateMyMovie/blob/master/images/response_a_movie.png)

---

**POST: Movie Ratings**
Header with Token:
![PostRating](https://github.com/slk007/RateMyMovie/blob/master/images/post_rating.png)
Body with Raw JSON Data:
![PostRating2](https://github.com/slk007/RateMyMovie/blob/master/images/post_rating_rating.png)
Response:
![ResponseRating](https://github.com/slk007/RateMyMovie/blob/master/images/response%20rating.png)

---

**GET: Ratings of a specific movie**
Header with Token:
![GetRatings](https://github.com/slk007/RateMyMovie/blob/master/images/get_%20a_movie_ratings.png)
Response:
![ResponseRatings](https://github.com/slk007/RateMyMovie/blob/master/images/response_a_movie_ratings.png)

---

## API Endpoints Usage: Django Rest Framework Interface

We can use all the same above API Endpoints in Django REST Framework Interface
![DRF](https://github.com/slk007/RateMyMovie/blob/master/images/drf.png)