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

Start app in dev mode on [http://localhost:8001](http://localhost:8001):

```sh
docker-compose up --build
```

Run tests:

```sh
# All tests
poetry run test
# Report coverage
poetry run test --cov=pyback --cov-report=html
# Integration tests
poetry run test_integration
# Unit tests
poetry run test_unit
```

Manually lint & format:

```sh
poetry run pre-commit run --all-files
```
