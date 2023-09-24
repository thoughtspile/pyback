# pyback

## Commands

Start app in dev mode:

```sh
poetry run uvicorn src.pyback.main:app --reload
```

Manually lint & format:

```sh
poetry run black src
poetry run flake8 src
```
