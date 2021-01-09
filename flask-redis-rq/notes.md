### What is Redis
An open source in-memory data structure store, used as a database, cache, and message broker.

### What is RQ
RQ is a simple Python library for queueing jobs and processing them in the background with workers. It is backed by Redis (and only supports Redis). It is a lightweight alternative to existing queueing frameworks (Celery, Resque), with a low barrier to entry.

----------------------------------------------

### venv
```
$ python3 -m venv venv
$ . venv/bin/activate
```

### flask development server setup 
```
$ pip install Flask
$ export FLASK_ENV=development
$ flask run
```

### redis & rq setup 
download redis (https://redis.io/), compile, and start the server
```
$ src/redis-server
```

in virtual env, install python libraries
```
$ pip install redis rq
```

### rq worker
To start executing enqueued function calls in the background, run
```
$ rq worker
```

