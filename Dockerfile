FROM python:3.8.1-slim

# install netcat
RUN apt-get update \
  && apt-get -y install netcat \
  && apt-get clean

# set working directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# add requirements
COPY requirements.txt /usr/src/app/requirements.txt

# install requirements
RUN pip install -r requirements.txt

# add app
COPY . /usr/src/app

# expose the port
EXPOSE 8080:8080

# run server
CMD ["./entrypoint.sh"]
