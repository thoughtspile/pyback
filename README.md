# pyback

This FastAPI server can greet anyone and store greetings with unique id in-memory for later use.

## Local development

Clone the repo, then install [poetry:](https://python-poetry.org/)

```sh
curl -sSL https://install.python-poetry.org | python3 -
```

And configure the project:

```sh
poetry install
poetry run pre-commit install
```

Happy hacking!

## Commands

Start app in dev mode:

```sh
poetry run dev
```

Manually lint & format:

```sh
poetry run pre-commit run --all-files
```
