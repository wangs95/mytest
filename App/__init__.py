from flask import Flask

from App.ext import init_ext


def create_app(ENV_NAME):
    app = Flask(__name__)
    init_ext(app)
    app.config.from_object(ENV_NAME)
    return app