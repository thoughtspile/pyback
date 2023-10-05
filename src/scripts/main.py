"""Poetry scripts for development."""
import sys

import pytest
import uvicorn


def dev():
    """Launch uvicorn from poetry script."""
    uvicorn.run("src.pyback.main:app", reload=True)


def test_unit():
    """Run pytest units from poetry script."""
    sys.exit(pytest.main(["-v", "--cov=pyback", "-m", "not integration"]))


def test_integration():
    """Run integration suite from poetry script."""
    sys.exit(pytest.main(["-v", "--cov=pyback", "-m", "integration"]))
