from flask import Module, render_template, request, send_from_directory
from config import Config
import os

twitter_endpoint = Module(__name__)


@twitter_endpoint.route('/', methods=['GET'])
def index():
    return render_template('index.html', files=File.get_files())


@twitter_endpoint.route('tweets/', methods=['POST'])
def tweets():
    from models.Twitter import Twitter
    from models.Twitter import Tweet
    twitter_account = request.form['twitter_account']
    twitter_ammount = request.form['twitter_ammount']
    tweet_list = []
    for tweet in Twitter.home_timeline(twitter_account, twitter_ammount):
        tweet = Tweet(str(tweet.id), twitter_account, tweet.text, str(tweet.retweeted), str(tweet.favorite_count),
                      str(tweet.retweet_count),
                      tweet.created_at.strftime('%Y-%m-%d %H:%M'))
        tweet_list.append(tweet.__dict__)

    if File.save(twitter_account, tweet_list):
        return render_template('index.html', files=File.get_files())


@twitter_endpoint.route('download/<path:filename>', methods=['GET'])
def download(filename):

    return send_from_directory('static/files', filename, as_attachment=True)


class File(object):
    def __init__(self, entry):
        self.name = entry

    @staticmethod
    def save(twitter_account, tweet_list):
        import csv
        import datetime
        file_name = twitter_account + datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
        with open(Config.FILES_PATH + file_name, 'wb') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            writer.writerow(tweet_list[0].keys())
            for x in tweet_list:
                writer.writerow([s.encode('utf8') for s in x.values()])
        return True

    @staticmethod
    def get_files():
        return [File(entry) for entry in os.listdir(Config.FILES_PATH)]
