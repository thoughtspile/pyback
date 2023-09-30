"""Poetry scripts for development."""
import sys

import pytest
import uvicorn


def dev():
    """Launch uvicorn from poetry script."""
    uvicorn.run("src.pyback.main:app", reload=True)


def test_integration():
    """Run pytest suite from poetry script."""
    sys.exit(pytest.main(["-v", "-m", "integration"]))
