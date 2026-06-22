from flask import Flask
from config import Config

def create_app():

    app = Flask(__name__)
    app.config.from_object(Config)

    from app.routes.web import web
    from app.routes.api import api
    from app.extensions import db
    from app.models.project import Project

    app.register_blueprint(web)
    app.register_blueprint(api)

    db.init_app(app)

    return app
