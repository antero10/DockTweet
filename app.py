from flask import Flask
from config import Config
from flask_bootstrap import Bootstrap
def create_app():
    from controller.twitter import twitter_endpoint
    app = Flask(__name__)
    Bootstrap(app)
    app.register_module(twitter_endpoint, url_prefix='/')
    return app


app = create_app()

if __name__ == '__main__':
    app.run(host=Config.APP_HOST, port=Config.APP_PORT, debug=Config.DEBUG)
