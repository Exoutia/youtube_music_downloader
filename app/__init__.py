import os

from flask import Flask, render_template


def create_app(test_config=None):
    # Create app and configure it based on test or other situation
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY="dev", DATABASE=os.path.join(app.instance_path, "app.sqlite")
    )

    if test_config is None:
        # Load the instance config, if it exists when not testing
        app.config.from_pyfile("config.py", silent=True)
    else:
        # Load the test config if passed in
        app.config.from_mapping(test_config)

    # Ensure the instance folder exists
    if not os.path.exists(app.instance_path):
        os.makedirs(app.instance_path)

    @app.route("/")
    def index():
        return render_template("index.html")

    @app.route("/hello")
    def hello():
        return "Hello, world!"

    from . import music

    app.register_blueprint(music.bp)

    return app
