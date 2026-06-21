from flask import Flask

def create_app():
    app = Flask(__name__)

    from app.routes.web import web

    app.register_blueprint(web)

    return app
