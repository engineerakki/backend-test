# backend-test

This code can be deployed in following two ways:-
# 1 : Running the application on a macine with python3 installed.:

### 1.1.1 : Clone the repo
```
git clone https://github.com/engineerakki/backend-test
```

### 1.1.2 : Install dependencies
```python
pip3 install -r requirements.txt
```

### 1.1.3 : Run the App
```python
python3 app.py
```

### 1.1.4: 
This should start the code server on port 8080

# 1.2 : Build and deploy a docker container

### 1.2.1 : Clone the repo
```
git clone https://github.com/engineerakki/backend-test
```

### 1.2.2 : Build the docker image
```
docker build -t backend-test .
```

### 1.2.3 : Run the container
```
docker run -itd -p 8080:8080 backend-test:latest
```




# 2 : Backend-Test APIs Solution

# 2.1 Login / Auth

## Get a key valid for 5 mins API:
Perform an GET call on following endpoint:
```
http://localhost:8080/<userid>/login

e.g:
http://localhost:8080/100/login/
http://localhost:8080/101/login/
```

#### Respone:
```
{
  "100": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE2MTM0MDEwNDUsIm5iZiI6MTYxMzQwMTA0NSwianRpIjoiMjRjYzJlMTItYmU1Yi00NjJlLWE3ZmQtOWUwMmVmZDM0MmMxIiwiZXhwIjoxNjEzNDAxMTA1LCJpZGVudGl0eSI6MTAwLCJmcmVzaCI6ZmFsc2UsInR5cGUiOiJhY2Nlc3MifQ.9uzrz8LJ1w1vCdST8Swt3VbrmaHamjl1gn2jqFtu9Tg"
}
```
Note: This token is valid for 10 mins


# 2.2 Post user's score to level

## API (POST Call)
#### Sample Request
```
http://localhost:8080/<<level_id>>/score?sessionkey=<<key_from_2.1>>

http://localhost:8080/1/score?sessionkey=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE2MTM0MTkyOTksIm5iZiI6MTYxMzQxOTI5OSwianRpIjoiNmUwOTM0NTMtZDJkNi00YTA0LTgyMDgtZjQwZmY4YzM1NTAyIiwiZXhwIjoxNjEzNDE5NTk5LCJpZGVudGl0eSI6MTAwLCJmcmVzaCI6ZmFsc2UsInR5cGUiOiJhY2Nlc3MifQ.uQJBKrB8rwRji47pCc7X02LJ5y51UYOdQdNw3wbEfQY
```

#### Sample Body:
```
{
    "score": 101
}
```

#### Sample Response:
```
{
    "status": "Score Updated for the user"
}
```

# 2.3 Get High Score list

## API (GET Call):

#### Sample Request:
```
http://localhost:8080/<<levelid>>/highscorelist?sessionkey=<<key_from_2.1>>

http://localhost:8080/5/highscorelist?sessionkey=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE2MTM0MjE5NzcsIm5iZiI6MTYxMzQyMTk3NywianRpIjoiYTg5Yzc4NGEtYWUwZC00M2Y0LWJhODgtOGRhMDEzNGMyZDVmIiwiZXhwIjoxNjEzNDIyMjc3LCJpZGVudGl0eSI6NTAwLCJmcmVzaCI6ZmFsc2UsInR5cGUiOiJhY2Nlc3MifQ.jKb7-VOlEGq2tEg6dcv7lTAC52pe67VreJCG1UXqtos
```

#### Sample Response:
```
{
    "score": 202,
    "user": 500
}
```


{
    "score": 101,
    "user": 100
}

# 2.4 Get Our UserData

#### Sample Request (GET call)
```
http://localhost:8080/get_user_model?sessionkey=<<key_from_2.1>>
```

#### Sample Response:
```
{
    "users": [
        {
            "level": 1,
            "score": 5,
            "userid": 100
        },
        {
            "level": 2,
            "score": 5,
            "userid": 101
        },
        {
            "level": 2,
            "score": 5,
            "userid": 100
        },
        {
            "level": 1,
            "score": 2,
            "userid": 103
        },
        {
            "level": 0,
            "score": 0,
            "userid": 500
        },
        {
            "level": 5,
            "score": 202,
            "userid": 500
        }
    ]
}
```