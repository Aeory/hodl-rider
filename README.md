# hodl-rider


## Installation
Requires Python 3.8 (thats right, we snuck one walrus in there 😉)

### Install dependencies 
```sh
$ pip install -r requirements.txt
```

### Generate a .env file
```shell script
$ cat << EOF > .env
TIINGO_API_KEY=<< GO GET ONE OF THESE >>
APP_NAME="hodl-flask"
APP_SETTINGS="project.server.config.DevelopmentConfig"
FLASK_DEBUG=1
GOOGLE_ANALYTICS_ID=
EOF
```

## Running
### As a webserver
```
$ python manage.py run
```

### Just the API
```
$ python .
```
