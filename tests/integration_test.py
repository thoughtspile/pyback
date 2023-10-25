"""Integration tests for funfinder app."""

import httpx
import pytest


@pytest.fixture(scope="function")
def seed_poi(coffee_samples: dict, client: httpx.Client):
    """Register all coffee shops from sample data."""
    for sample in coffee_samples.values():
        client.post("/poi/", json=sample)


@pytest.mark.integration
def test_add_poi(coffee_samples: dict, client: httpx.Client):
    """Can add & retreive point."""
    target = coffee_samples["spb1"]
    create_response = client.post("/poi/", json=target)
    assert create_response.status_code == 200

    id = create_response.json()["id"]
    get_response = client.get(f"/poi/{id}")
    assert get_response.json() == {**target, "id": id}


@pytest.mark.integration
def test_missing_poi(client: httpx.Client):
    """Getting missing PoI returns 404."""
    get_response = client.get("/poi/-1")
    assert get_response.status_code == 404


@pytest.mark.integration
def test_suggest(coffee_samples: dict, client: httpx.Client):
    """Suggests close coffee, sorted by proximity."""
    res = client.get("/suggest?lat=59.917931&lon=30.286723")
    assert res.status_code == 200
    data = res.json()
    for seggestion in data:
        del seggestion["id"]
    assert coffee_samples["spb2"] in data
    assert coffee_samples["spb1"] in data


@pytest.mark.integration
def test_upload(client: httpx.Client):
    """Uploads image."""
    fname = "tests/book.png"
    files = {"file": open(fname, "rb")}
    upload = client.post("/upload", files=files)
    assert upload.status_code == 200
    key = upload.json()["key"]
    res = httpx.get(f"http://images.localhost/{key}")
    assert res.content == open(fname, "rb").read()
