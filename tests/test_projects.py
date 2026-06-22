from app import create_app


def test_create_project():

    app = create_app()

    client = app.test_client()

    response = client.post(
        "/api/v1/projects",
        json={
            "name": "Projeto Teste",
            "description": "Teste Automatizado"
        }
    )

    assert response.status_code == 201

    assert response.json["name"] == "Projeto Teste"



def test_get_projects():

    app = create_app()

    client = app.test_client()

    response = client.get(
        "/api/v1/projects"
    )

    assert response.status_code == 200

    assert isinstance(
        response.json,
        list
    )


def test_get_project_by_id():

    app = create_app()

    client = app.test_client()

    create = client.post(
        "/api/v1/projects",
        json={
            "name": "Projeto ID",
            "description": "Teste"
        }
    )

    project_id = create.json["id"]

    response = client.get(
        f"/api/v1/projects/{project_id}"
    )

    assert response.status_code == 200

    assert response.json["id"] == project_id


def test_update_project():

    app = create_app()

    client = app.test_client()

    create = client.post(
        "/api/v1/projects",
        json={
            "name": "Original",
            "description": "Original"
        }
    )

    project_id = create.json["id"]

    response = client.put(
        f"/api/v1/projects/{project_id}",
        json={
            "name": "Atualizado",
            "description": "Atualizado"
        }
    )

    assert response.status_code == 200

    assert response.json["name"] == "Atualizado"


def test_delete_project():

    app = create_app()

    client = app.test_client()

    create = client.post(
        "/api/v1/projects",
        json={
            "name": "Delete",
            "description": "Delete"
        }
    )

    project_id = create.json["id"]

    response = client.delete(
        f"/api/v1/projects/{project_id}"
    )

    assert response.status_code == 200
