# Sample Dockerized API (Flask + Flask REST + SQLAlchemy + PostgreSQL)

### 1) Init PostgreSQL container:
```
  docker run --name postgresql -d -p 5432:5432 -itd --restart always \
  --env 'DB_USER=sportspots' --env 'DB_PASS=sportspotspass' \
  --env 'DB_NAME=spotsdb' \
  sameersbn/postgresql:9.6-2

```
### 2) Chage host in settings.py
POSTGRES = {
    'user': 'sportspots',
    'pw': 'sportspotspass',
    'db': 'spotsdb',
    'host': '!!! Postgres container IP here !!! ',
    'port': '5432',
}

### 3) Build container
```
docker build -t sport-spot:latest .
```

### 4) Run container
```
docker run --name sport-spot-postgres -d  -p 5000:5000 sport-spot
```