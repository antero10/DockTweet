import tweepy
from config import Config


class Twitter(object):
    @staticmethod
    def home_timeline(account, count):
        auth = tweepy.OAuthHandler(Config.TWITTER_CONSUMER_KEY, Config.TWITTER_CONSUMER_SECRET)
        auth.set_access_token(Config.TWITTER_ACCESS_TOKEN,
                              Config.TWITTER_ACCESS_TOKEN_SECRET)

        api = tweepy.API(auth, wait_on_rate_limit=True)
        return api.user_timeline(screen_name=account, count=count)


class Tweet(object):
    def __init__(self, id, screen_name, text, retweeted, favorite_count, retweet_count, created_at):
        self.id = id
        self.screen_name = screen_name
        self.text = text
        self.retweeted = retweeted
        self.favorite_count = favorite_count
        self.retweet_count = retweet_count
        self.created_at = created_at

    def __repr__(self):
        return '<Tweet id=%s, screen_name=%s>' % (self.id, self.screen_name)
