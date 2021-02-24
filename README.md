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
    * User needs to login/signup from the home page of the website


* API Endpoints:
    * /get-token
    * /api/movies
    * /api/movies/<int:movie_id>
    * /api/movies/<int:movie_id>/ratings
    * api/movies/<int:movie_id>/rate
---

## API:

Open Postman  

**Make a post request with username, password:**
![PostToken](https://github.com/slk007/RateMyMovie/blob/master/images/post_get_token.png)
You will get Token in response as below. Copy this Token as we need to use it for all our API Requests:
![ResponseToken](https://github.com/slk007/RateMyMovie/blob/master/images/response_token.png)
