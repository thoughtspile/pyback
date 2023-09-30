"""Poetry scripts for development."""
import uvicorn


def dev():
    """Launch uvicorn from poetry script."""
    uvicorn.run("src.pyback.main:app", reload=True)
