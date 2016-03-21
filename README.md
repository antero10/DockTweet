# DockTweet
Docker app allows you to export user's tweets into a CSV file.

## [Dockerhub](https://hub.docker.com/r/antero/docktweet/)

<p align="center">
  <img src="https://media.giphy.com/media/xThuVYHFQbZvAQU22Y/giphy.gif" width="350"/>
</p>

# Instructions 

# 1 Create a twitter app
To use this docker you need to create an app on [Twitter](https://apps.twitter.com/) to provide app key

# 2 Pull Image 
`docker pull antero/docktweet`

# 3 Run docker

A simple way just run `docker run -d  --name dockertweet docktweet -p HOST_PORT:80` 

## Environment Variables

This docker need to provide some enviroment variables to be used by any account:

* `-e TWITTER_CONSUMER_KEY` app consumer key provided by twitter
* `-e TWITTER_CONSUMER_SECRET` app consumer secret  key provided by twitter
* `-e TWITTER_ACCESS_TOKEN` app access token key provided by twitter
* `-e TWITTER_ACCESS_TOKEN_SECRET` app access token secret provided by twitter
* `-e APP_PORT` define port for app ex: `80`
* `-e APP_HOST` define host for app ex: `0.0.0.0` (localhost)

# 4 Enter web interface

Connect to `127.0.0.0.1:HOST_PORT` and use the app


