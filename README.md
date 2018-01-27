# Meloshare
Collaborative music sketching web application.
Built using Python Flask, Flask-Flash, Celery and Redis.

### Quickstart
Let's clone the repo, create a virtualenv, install the pip requirements and run our services.
```
git clone https://github.com/xavierfav/meloshare
mkvirtualenv meloshare # create virtualenv using virtualenvwrapper library. You can also use the command `virtualenv venv`.
pip install -r requirements.txt # install pip dependencies
apt install redis-server # install Redis
supervisord -c supervisord.conf # run all services
supervisorctl # administrate services (stop, start, restart, reload, ...)
```

## Installation
### Clone the repository
```
git clone https://github.com/xavierfav/meloshare
```

### Install the dependencies
```
pip install -r requirements.txt
```

### Install and run Redis
```
apt install redis-server
redis-server
```

### Run the UI
```
FLASK_APP=meloshare/ui/app.py flask run
```

### Run the API
```
FLASK_APP=meloshare/api/app.py flask run
```

### Run the worker
```
celery worker -A meloshare.celeryapp:app -l info
```
