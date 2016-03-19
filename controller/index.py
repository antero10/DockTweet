from flask import Module, render_template

endpoint = Module(__name__)


@endpoint.route('/', methods=['GET'])
def index():
    return render_template('index.html.jinja2')
