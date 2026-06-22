from app import create_app


def test_system():

    app = create_app()

    client = app.test_client()

    response = client.get(
        "/api/v1/system"
    )

    assert response.status_code == 200

    assert "app" in response.json

    assert "version" in response.json
