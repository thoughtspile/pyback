"""Integration tests for funfinder app."""

import pytest
from fastapi.testclient import TestClient


@pytest.mark.integration
def test_add_poi(client: TestClient):
    """Can add & retreive point."""
    data = {
        "lat": 43,
        "lon": 120,
        "title": "Funky Coffee",
        "description": "Good coffee and cakes",
    }
    create_response = client.post("/poi/", json=data)
    assert create_response.status_code == 200

    id = create_response.json()["id"]
    get_response = client.get(f"/poi/{id}")
    assert get_response.json() == {**data, "id": id}
