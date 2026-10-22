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
