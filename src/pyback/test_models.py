"""Tests for app models."""
from pyback.models import Greeting


def test_greeting():
    """Greeting.from_receiver generates a greering."""
    assert Greeting.from_receiver("buddy").message == "Hello, buddy"
