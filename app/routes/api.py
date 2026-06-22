from flask import Blueprint

from app.services.system import get_system_info
from flask import request
from app.services.projects import create_project
from app.services.projects import get_projects

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
@api.route("/projects", methods=["POST"])
def create_project_route():

    data = request.get_json()

    project = create_project(
        data["name"],
        data["description"]
    )

    return {
        "id": project.id,
        "name": project.name
    }, 201



@api.route("/projects", methods=["GET"])
def get_projects_route():

    projects = get_projects()

    return [
        {
            "id": project.id,
            "name": project.name,
            "description": project.description
        }
        for project in projects
    ]
