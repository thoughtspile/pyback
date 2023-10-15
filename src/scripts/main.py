"""Poetry scripts for development."""
import sys

import pytest


def test_unit():
    """Run pytest units from poetry script."""
    sys.exit(pytest.main(["src/pyback", "-v", "--cov=pyback"]))


def test_integration():
    """Run integration suite from poetry script."""
    sys.exit(pytest.main(["tests", "-v"]))
