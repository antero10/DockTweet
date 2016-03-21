import os
class Config(object):
    APP_PORT = os.environ['APP_PORT']
    APP_HOST = os.environ['APP_HOST']
    DEBUG = False
    FILES_PATH = '/app/static/files/'
    TWITTER_CONSUMER_KEY = os.environ['TWITTER_CONSUMER_KEY']
    TWITTER_CONSUMER_SECRET = os.environ['TWITTER_CONSUMER_SECRET']
    TWITTER_ACCESS_TOKEN = os.environ['TWITTER_ACCESS_TOKEN']
    TWITTER_ACCESS_TOKEN_SECRET = os.environ['TWITTER_ACCESS_TOKEN_SECRET']
