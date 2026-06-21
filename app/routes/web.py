from flask import Blueprint

web = Blueprint("web", __name__)

@web.route("/")
def index():

    return """
    <h1>Zeus</h1>
    <p>Servidor Flask funcionando.</p>
    """
