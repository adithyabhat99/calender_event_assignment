# calender_event_assignment

## Deployed in Heroku
### Production URL = https://adieventmanagement.herokuapp.com/

<hr />
<br />

### Setup in local machine(linux)
```
chmod +x start.sh
./start.sh
```
<br />
<br />

## API Docs

### /api/user  POST
##### creates a new user

- Example input
```
{
    "name":"adithya",
    "email":"adithyabhatoct@gmail.com",
    "password":"123"
}
```
- Example output
```
{
    "Token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6IjEiLCJuYW1lIjoiYWRpdGh5YSIsImV4cCI6MTU5ODYxODI5Mn0.ksdPq6leEylx8dNupFo4NgFL32aWeWMU5hA3ozllR-w",
    "message": "user created",
    "success": true
}
```


<hr />

### /api/user/auth POST
##### get auth token
- Example input
###### Set authorization header(Basic Auth) with email as "username" and password
![auth](https://user-images.githubusercontent.com/30742449/90519442-a7c7a380-e185-11ea-898d-0a1c1e7e1b03.png)

- Example output
```
{
    "Token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6IjEiLCJuYW1lIjoiYWRpdGh5YSIsImV4cCI6MTU5ODYyMTg1M30.fG7ckZEaMVjHu2104O7F-HmzWUzT2Dby9mOXu5pjVxQ",
    "message": "authentication successful",
    "success": true
}
```

#### Example usage of Auth Token(token is standard JWT)
![example usage](https://user-images.githubusercontent.com/30742449/90519455-aa29fd80-e185-11ea-9a6a-1920a42efc49.png)

<hr />
<br />

### /api/user  PUT
##### updates user(name,email,password)
- requires auth token
- Example input
```
{
    "name":"adithya-updated"
}
```
- Example output
```
{
  "message": "user update successful",
  "success": true
}
```

<hr />

### /api/user  GET
##### get user details
- requires auth token
- Example output
```
{
    "data": {
        "email": "adithyabhatoct@gmail.com",
        "name": "adithya"
    },
    "message": "user exists",
    "success": true
}
```

<hr />

### /api/user DELETE
##### deletes user account
- requires auth token

<hr />

### /api/event POST
##### creates event
- requires auth token
- Example input
```
{
    "title":"birthday",
    "description":"happy birthday adithya",
    "start_date":"2020-08-18 20:00:02",
    "end_date":"2020-08-18 20:31:10"
}
```
- Example output
```
{
    "data": {
        "end_date": "2020-08-18 20:31:10",
        "id": 1,
        "start_date": "2020-08-18 20:00:02",
        "title": "birthday"
    },
    "message": "Event created",
    "success": true
}
```
<hr />

### /api/event/:id GET
##### get event by id
- requires auth token
- Example output
```
{
    "data": {
        "description": "happy birthday adithya",
        "end_date": "2020-08-18 20:31:10",
        "id": 1,
        "start_date": "2020-08-18 20:00:02",
        "title": "birthday"
    },
    "message": "event exists",
    "success": true
}
```

<hr />

### /api/event GET
##### get all events of a user
- requires auth token
- Example output
```
{
    "data": [
        {
            "description": "happy birthday adithya",
            "end_date": "2020-08-18 20:31:10",
            "id": 1,
            "start_date": "2020-08-18 20:00:02",
            "title": "birthday"
        },
        {
            "description": "happy birthday adithya",
            "end_date": "2020-08-18 20:31:10",
            "id": 2,
            "start_date": "2020-08-18 20:00:02",
            "title": "birthday"
        }
    ],
    "message": "events list",
    "success": true
}
```
<hr />

### /api/event/:id DELETE
##### delete event by id
- requires auth token
- Example output
```
{
    "message": "event deleted",
    "success": true
}
```

<hr />

