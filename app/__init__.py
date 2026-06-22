from flask import Flask

def create_app():

    app = Flask(__name__)

    from app.routes.web import web
    from app.routes.api import api
    from app.extensions import db
    from app.models.project import Project

    app.register_blueprint(web)
    app.register_blueprint(api)

    app.config["SQLALCHEMY_DATABASE_URI"] = \
    "sqlite:///zeus.db"

    db.init_app(app)

    return app
