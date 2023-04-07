from flask import Flask

from .routes import blueprint


def create_app() -> Flask:
    app = Flask(__name__)
    app.register_blueprint(blueprint)

    @app.route("/")
    def hello():
        return "It Works!"

    return app
