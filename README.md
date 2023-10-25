# pyback

This FastAPI server can greet anyone and store greetings with unique id in-memory for later use.

## Local development

Clone the repo, then install [poetry](https://python-poetry.org/) and [docker](https://docs.docker.com/engine/install/).

Configure the project:

```sh
poetry install
poetry run pre-commit install
```

Happy hacking!

## Commands

Start app in dev mode:

```sh
docker-compose up --build
```

API runs on [http://api.localhost](http://api.localhost)

Run tests:

```sh
# Unit tests
poetry run test_unit

# Integration tests
docker-compose up -d
poetry run test_integration
```

Manually lint & format:

```sh
poetry run pre-commit run --all-files
```
