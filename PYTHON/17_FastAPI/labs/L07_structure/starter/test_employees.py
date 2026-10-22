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


# TODO: test_ananya_has_no_extra_fields: GET E-1042 is 200, the name is Ananya Rao,
# and "salary" is not in the JSON.


# TODO: test_missing_employee_is_404: GET E-9999 is 404.
