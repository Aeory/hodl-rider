#!/bin/sh

gunicorn --chdir /usr/src/app manage:app -w 3 --threads 2 -b 0.0.0.0:8080
