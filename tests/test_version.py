from app import create_app


def test_version():

    app = create_app()

    client = app.test_client()

    response = client.get(
        "/api/v1/version"
    )

    assert response.status_code == 200

    assert "version" in response.json
