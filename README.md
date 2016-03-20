# DockTweet
Docker app is to get tweets from a certain account. Saved in a .csv file


# Instructions 

# 1 Create twitter app
To use this docker you need to create an app on [Twitter](https://apps.twitter.com/) to provide app key

# 2 Build docker 
Build docker `docker build -t docktweet .`

# 3 Run docker

This docker export a .csv file so you may need to run the docker with a volume to get the csv data.

A simple way just run `docker run -d --name dockertweet docktweet` (You always need -it flag because this is a command line interface docker)

## Environment Variables
    * `-e TWITTER_CONSUMER_KEY` app consumer key provided by twitter
    * `-e TWITTER_CONSUMER_SECRET` app consumer secret  key provided by twitter
    * `-e TWITTER_ACCESS_TOKEN` app access token key provided by twitter
    * `-e TWITTER_ACCESS_TOKEN_SECRET` app access token secret provided by twitter

# 4 Enter web interface

Connect to `127.0.0.0.1` and use the app


