from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.database import Base, get_db
from app.main import app

TEST_DATABASE_URL = "sqlite:///./test_candidates.db"
engine = create_engine(
    TEST_DATABASE_URL,
    connect_args={"check_same_thread": False},
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)


def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db
client = TestClient(app)


def test_create_candidate_success():
    payload = {
        "name": "John Doe",
        "email": "john@example.com",
        "skill": "Python",
        "status": "applied",
    }

    response = client.post("/candidates", json=payload)

    assert response.status_code == 201
    data = response.json()
    assert data["name"] == payload["name"]
    assert data["email"] == payload["email"]
    assert data["status"] == payload["status"]


def test_create_candidate_invalid_email():
    payload = {
        "name": "Jane Doe",
        "email": "invalid-email",
        "skill": "Python",
        "status": "applied",
    }

    response = client.post("/candidates", json=payload)

    assert response.status_code == 422


def test_get_candidates_with_filter():
    client.post(
        "/candidates",
        json={
            "name": "Alice",
            "email": "alice@example.com",
            "skill": "Backend",
            "status": "interview",
        },
    )
    client.post(
        "/candidates",
        json={
            "name": "Bob",
            "email": "bob@example.com",
            "skill": "Frontend",
            "status": "applied",
        },
    )

    response = client.get("/candidates", params={"status": "interview"})

    assert response.status_code == 200
    data = response.json()
    assert len(data) >= 1
    assert all(item["status"] == "interview" for item in data)


def test_update_candidate_status_success():
    create_response = client.post(
        "/candidates",
        json={
            "name": "Charlie",
            "email": "charlie@example.com",
            "skill": "DevOps",
            "status": "applied",
        },
    )
    candidate_id = create_response.json()["id"]

    update_response = client.put(
        f"/candidates/{candidate_id}/status",
        json={"status": "selected"},
    )

    assert update_response.status_code == 200
    assert update_response.json()["status"] == "selected"


def test_update_candidate_not_found():
    response = client.put("/candidates/999999/status", json={"status": "rejected"})

    assert response.status_code == 404
