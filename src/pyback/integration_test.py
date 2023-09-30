"""Integration tests for funfinder app."""

import pytest
from fastapi.testclient import TestClient


@pytest.fixture(scope="function")
def seed_poi(coffee_samples: dict, client: TestClient):
    """Register all coffee shops from sample data."""
    for sample in coffee_samples.values():
        client.post("/poi/", json=sample)


@pytest.mark.integration
def test_add_poi(coffee_samples: dict, client: TestClient):
    """Can add & retreive point."""
    target = coffee_samples["spb1"]
    create_response = client.post("/poi/", json=target)
    assert create_response.status_code == 200

    id = create_response.json()["id"]
    get_response = client.get(f"/poi/{id}")
    assert get_response.json() == {**target, "id": id}


@pytest.mark.integration
def test_missing_poi(client: TestClient):
    """Getting missing PoI returns 404."""
    get_response = client.get("/poi/1")
    assert get_response.status_code == 404


@pytest.mark.integration
def test_suggest(coffee_samples: dict, client: TestClient, seed_poi):
    """Suggests close coffee, sorted by proximity."""
    res = client.get("/suggest?lat=59.917931&lon=30.286723")
    assert res.status_code == 200
    data = res.json()
    for seggestion in data:
        del seggestion["id"]
    assert data == [coffee_samples["spb2"], coffee_samples["spb1"]]
