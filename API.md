# API Endpoints


Obtain Token (Method: POST):
```
http://127.0.0.1:8000/get-token/
```

List all Movies(Method: GET):, Create new Movie(Method: POST):
```
http://127.0.0.1:8000/api/movies
```

Get Movie with Movie id=pk (Method: GET):
```
http://127.0.0.1:8000/api/movies/<int:pk>
```

Get all the Ratings for Movie with id=pk(Method: GET):
```
http://127.0.0.1:8000/api/movies/<int:pk>/ratings
```

Rate a Movie with Movie id=pk (Method: POST):
```
http://127.0.0.1:8000/api/movies/<int:pk>/rate
```