# Sample Dockerized API (Flask + Flask REST + SQLAlchemy + PostgreSQL)

## Set-up
Using Docker

### 1) Init PostgreSQL container:
```
  docker run --name postgresql -d -p 5432:5432 -itd --restart always \
  --env 'DB_USER=sportspots' --env 'DB_PASS=sportspotspass' \
  --env 'DB_NAME=spotsdb' \
  sameersbn/postgresql:9.6-2

```
### 2) Chage host in settings.py
```
POSTGRES = {
    'user': 'sportspots',
    'pw': 'sportspotspass',
    'db': 'spotsdb',
    'host': '!!! Postgres container IP here !!! ',
    'port': '5432',
}
```

### 3) Build container
```
docker build -t sport-spot:latest .
```

### 4) Run container
```
docker run --name sport-spot-postgres -d  -p 5000:5000 sport-spot
```

## API Demo
### http://0.0.0.0:5000/spots | GET
Returns the list of spots:
```
[
  {
    "address": "2222 plymouth ave, San Francisco, CA",
    "id": 1,
    "title": "Sport location on Plymouth"
  },
  {
    "address": "100 Ocean Ave., San Francisco, CA",
    "id": 2,
    "title": "City College Gym"
  }
]
```

### http://0.0.0.0:5000/spots | POST
Adds a new location:
```
{
  "address": "100 Ocean Ave, San Francisco, CA",
  "id": 3,
  "title": "The new location"
}
```

### http://0.0.0.0:5000/spots/1 | GET
Returns the location by ID:
```
  {
    "address": "2222 plymouth ave, San Francisco, CA",
    "id": 1,
    "title": "Sport location on Plymouth"
  }
```

### http://0.0.0.0:5000/spots/1 | PUT
Updates the location by ID:
```
  {
    "address": "2222 plymouth ave, San Francisco, CA",
    "id": 1,
    "title": "Sport location on Plymouth, Updated"
  }
```

### http://0.0.0.0:5000/spots/1 | DELETE
Deletes the location by ID