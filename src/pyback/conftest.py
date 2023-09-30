"""pytest fixtures."""

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from .database import Base
from .main import app, get_db


@pytest.fixture(scope="session")
def db_engine():
    """Initialize test database engine."""
    engine = create_engine(
        "sqlite:///./db_test.db", connect_args={"check_same_thread": False}
    )
    yield engine
    engine.dispose()


@pytest.fixture(scope="function")
def db(db_engine):
    """Initialize test database session, clear between runs."""
    Base.metadata.create_all(bind=db_engine)
    yield Session(autocommit=False, autoflush=False, bind=db_engine)
    Base.metadata.drop_all(bind=db_engine)


@pytest.fixture(scope="function")
def client(db):
    """Initialize test HTTP client."""
    app.dependency_overrides[get_db] = lambda: db

    with TestClient(app) as c:
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
