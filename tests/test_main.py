from fastapi.testclient import TestClient

from main import app


client = TestClient(app)


def test_root():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {
        "message": "Student Management API is running"
    }


def test_health_check():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {
        "status": "healthy"
    }


def test_create_student():
    response = client.post(
        "/students",
        json={
            "name": "Alice",
            "age": 20,
            "course": "Computer Science",
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["name"] == "Alice"
    assert data["age"] == 20
    assert data["course"] == "Computer Science"


def test_get_students():
    response = client.get("/students")

    assert response.status_code == 200
    assert isinstance(response.json(), list)
