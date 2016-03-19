from flask import Flask


def create_app():
    from controller.index import endpoint
    app = Flask(__name__)
    app.register_module(endpoint, url_prefix='/')
    return app


app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
