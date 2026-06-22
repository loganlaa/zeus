from flask import Blueprint

from app.services.system import get_system_info

api = Blueprint(
    "api",
    __name__,
    url_prefix="/api/v1"
)

@api.route("/health")
def health():

    return {
        "status": "ok"
    }

@api.route("/version")
def version():

    return {
        "version": "1.0.0"
    }

@api.route("/system")
def system():

    return get_system_info()
