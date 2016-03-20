# Maintainer antero10

FROM ubuntu:latest

#Intall packages
RUN apt-get -yqq update
RUN apt-get -yqq install libpq-dev python python-dev python-distribute python-pip

# Install Tweetpy
RUN pip install tweepy

# Install flask
RUN pip install Flask

# Install jinja2
RUN pip install Jinja2

# Install flask boostrap
RUN pip install flask-bootstrap

COPY ./ /app

WORKDIR /app

EXPOSE 80 500

CMD ["python","app.py"]