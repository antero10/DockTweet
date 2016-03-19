# DockTweet
Docker app is to get tweets from a certain account. Saved in a .csv file


# Instructions 

# 1 Build docker 
Build docker `docker build -t docktweet .`

# 2 Run docker

This docker export a .csv file so you may need to run the docker with a volume to get the csv data.

A simple way just run `docker run -d --name dockertweet docktweet` (You always need -it flag because this is a command line interface docker)

# 3 Enter web interface

Connect to `127.0.0.0.1` and use the app


