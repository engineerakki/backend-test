# backend-test

This code can be deployed in following two ways:-
# 1.1 : Running the application on a macine with python3 installed.:

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




# 4.1 : Login
## Get a key valid for 5 mins:
http://localhost:8080/<userid>/login
e.g:
http://localhost:8080/100/login/
http://localhost:8080/101/login/

Respone:
{
  "100": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE2MTM0MDEwNDUsIm5iZiI6MTYxMzQwMTA0NSwianRpIjoiMjRjYzJlMTItYmU1Yi00NjJlLWE3ZmQtOWUwMmVmZDM0MmMxIiwiZXhwIjoxNjEzNDAxMTA1LCJpZGVudGl0eSI6MTAwLCJmcmVzaCI6ZmFsc2UsInR5cGUiOiJhY2Nlc3MifQ.9uzrz8LJ1w1vCdST8Swt3VbrmaHamjl1gn2jqFtu9Tg"
}


# 4.2 Post user's score to level

## Repo




# 4.3 Get HighScore of a level