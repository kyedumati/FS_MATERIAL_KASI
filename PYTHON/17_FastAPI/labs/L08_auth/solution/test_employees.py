import os
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

os.environ["DATABASE_URL"] = "sqlite:///./test_acme.db"
Path("test_acme.db").unlink(missing_ok=True)

from main import app


@pytest.fixture(scope="module")
def client():
    with TestClient(app) as test_client:
        yield test_client


def test_health(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_ananya_has_no_extra_fields(client):
    response = client.get("/employees/E-1042")
    assert response.status_code == 200
    body = response.json()
    assert body["name"] == "Ananya Rao"
    assert "salary" not in body


def test_missing_employee_is_404(client):
    response = client.get("/employees/E-9999")
    assert response.status_code == 404


def test_me_without_token_is_401(client):
    response = client.get("/me")
    assert response.status_code == 401


def test_hr_can_delete_and_employee_cannot(client):
    ananya = client.post(
        "/login",
        data={"username": "ananya.rao@acme.example", "password": "Acme#1042"},
    )
    assert ananya.status_code == 200
    denied = client.delete(
        "/employees/E-1044",
        headers={"Authorization": f"Bearer {ananya.json()['access_token']}"},
    )
    assert denied.status_code == 403

    rahul = client.post(
        "/login",
        data={"username": "rahul.sharma@acme.example", "password": "Acme#1045"},
    )
    assert rahul.status_code == 200
    deleted = client.delete(
        "/employees/E-1044",
        headers={"Authorization": f"Bearer {rahul.json()['access_token']}"},
    )
    assert deleted.status_code == 204


def test_anonymous_cannot_change_an_employee(client):
    assert client.patch("/employees/E-1042", json={"designation": "Intern"}).status_code == 401
    assert client.get("/employees/E-1042").json()["designation"] == "Senior Software Engineer"
