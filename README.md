# pyback

This FastAPI server can greet anyone and store greetings with unique id in-memory for later use.

## Commands

Start app in dev mode:

```sh
poetry run uvicorn src.pyback.main:app --reload
```

Manually lint & format after:

```sh
poetry run pre-commit run --all-files
```
