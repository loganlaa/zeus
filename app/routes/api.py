from flask import Blueprint
from config import Config

from app.services.system import get_system_info
import flask
from app.services.projects import create_project
from app.services.projects import get_projects
from app.services.projects import get_project
from app.services.projects import update_project
from app.services.projects import delete_project

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
        "version": Config.APP_VERSION
    }



@api.route("/system")
def system():

    return {
        "app": Config.APP_NAME,
        "version": Config.APP_VERSION
    }



@api.route("/projects", methods=["POST"])
def create_project_route():

    data = flask.request.get_json()

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


@api.route("/projects/<int:project_id>", methods=["GET"])
def get_project_route(project_id):

    project = get_project(project_id)

    if not project:
        return {"error": "Project not found"}, 404

    return {
        "id": project.id,
        "name": project.name,
        "description": project.description
    }


@api.route("/projects/<int:project_id>", methods=["PUT"])
def update_project_route(project_id):

    data = flask.request.get_json()

    project = update_project(
        project_id,
        data
    )

    if not project:
        return {
            "error": "Project not found"
        }, 404

    return {
        "id": project.id,
        "name": project.name,
        "description": project.description
    }



@api.route("/projects/<int:project_id>", methods=["DELETE"])
def delete_project_route(project_id):

    project = delete_project(project_id)

    if not project:
        return {
            "error": "Project not found"
        }, 404

    return {
        "message": "Project deleted"
    }
