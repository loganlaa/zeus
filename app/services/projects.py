from app.extensions import db
from app.models.project import Project

def create_project(name, description):

    project = Project(
        name=name,
        description=description
    )

    db.session.add(project)
    db.session.commit()

    return project


def get_projects():

    return Project.query.all()

def get_project(project_id):

    return Project.query.get(project_id)
