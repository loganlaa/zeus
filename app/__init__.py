from flask import Flask

def create_app():

    app = Flask(__name__)

    from app.routes.web import web
    from app.routes.api import api

    app.register_blueprint(web)
    app.register_blueprint(api)

    return app
