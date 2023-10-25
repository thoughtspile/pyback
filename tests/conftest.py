"""pytest fixtures."""

import httpx
import pytest


@pytest.fixture(scope="function")
def client():
    """Initialize test HTTP client."""
    with httpx.Client(base_url="http://api.localhost") as c:
        yield c


@pytest.fixture(scope="session")
def coffee_samples():
    """Sample coffee shops."""
    return {
        "spb1": {
            "lat": 59.910373,
            "lon": 30.284117,
            "title": "Sibaristica",
            "description": "Coffee factory",
        },
        "spb2": {
            "lat": 59.924744,
            "lon": 30.287771,
            "title": "Рид",
            "description": "Coffee and sanwich",
        },
        "devil": {
            "lat": 55.759811,
            "lon": 37.651844,
            "title": "Кооператив Черный",
            "description": "Coffee in the city of devil",
        },
    }
