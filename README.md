# hodl-rider

Make a .env file
```sh
TIINGO_API_KEY=<< GO GET ONE OF THESE >>
APP_NAME="hodl-flask"
APP_SETTINGS="project.server.config.DevelopmentConfig"
FLASK_DEBUG=1
```
get python3.8 (jks any python 3, we couldnt find a reason to use walrus)

run pip install -r requirements.txt

to start the app as a local webserver run `python manage.py run`

to just access the API via CLI run `python .`

to run the full prod webserver build & run the dockerfile

