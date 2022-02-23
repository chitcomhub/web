from typing import Generator

import pytest
from fastapi.testclient import TestClient
from requests.models import Response

from main import app


@pytest.fixture(scope="module")
def client() -> Generator:
    with TestClient(app) as c:
        yield c


def test_get_members_request(client):
    """
    GET request to endpoint /api/members
    :param client: fixture that return HTTP Client for tests.
    :return: None
    """
    response: Response = client.get("/api/members")
    assert response.status_code == 200
    assert type(response.json()) == list


def test_post_members_request(client):
    """
    GET request to endpoint /api/members
    :param client: fixture that return HTTP Client for tests.
    :return: None
    """
    json_data = {
        "first_name": "AbduLlah",
        "last_name": "Tester",
        "short_bio": "Python backend.",
        "long_bio": "I like Django",
        "birthday": "2010-02-19",
        "telegram": "t.me/chitcom",
        "github": "http://github.com/chitcomhub/web",
    }
    response: Response = client.post("/api/members", json=json_data)
    assert response.status_code == 201
    for key in json_data:
        assert response.json()[key] == json_data[key]
