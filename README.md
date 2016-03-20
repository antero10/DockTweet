# DockTweet
Docker app is to get tweets from a certain account. Saved in a .csv file

<p align="center">
  <img src="http://giphy.com/gifs/docktweet-xThuVYHFQbZvAQU22Y" width="350"/>
</p>

# Instructions 

# 1 Create twitter app
To use this docker you need to create an app on [Twitter](https://apps.twitter.com/) to provide app key

# 2 Build docker 
Build docker `docker build -t docktweet .`

# 3 Run docker

A simple way just run `docker run -d  --name dockertweet docktweet -p HOST_PORT:80` 

## Environment Variables
    * `-e TWITTER_CONSUMER_KEY` app consumer key provided by twitter
    * `-e TWITTER_CONSUMER_SECRET` app consumer secret  key provided by twitter
    * `-e TWITTER_ACCESS_TOKEN` app access token key provided by twitter
    * `-e TWITTER_ACCESS_TOKEN_SECRET` app access token secret provided by twitter

# 4 Enter web interface

Connect to `127.0.0.0.1:HOST_PORT` and use the app


