# API Endpoints


To Obtain Your Token(Method: POST):
```
http://127.0.0.1:8000/get-token/
```
The request should have below fields:
```
{
    "username": "<string>",
    "password": "<string>"
}
```
---
List all Movies(Method: GET):  
```
http://127.0.0.1:8000/api/movies
```
Create New Movie(Method: POST):
The request should have below fields:
```
{
    "title": "<string><max_length=300>",
    "story": "<text>",
    "genre": "<string><max_length=10>",
    "released_year": "<string><max_length=4>"
}
```
---
Get Movie with Movie id=pk (Method: GET):
```
http://127.0.0.1:8000/api/movies/<int:pk>
```
---
Get all the Ratings for Movie with id=pk(Method: GET):
```
http://127.0.0.1:8000/api/movies/<int:pk>/ratings
```
---
Rate a Movie with Movie id=pk (Method: POST):
```
http://127.0.0.1:8000/api/movies/<int:pk>/rate
```
The request should have below fields:
```
{
    "rating": "<int>"
}
```
---