# recommendation_service

Python HTTP service for recommendation and algorithm runtime workloads.

This service starts as infrastructure only: health endpoints, typed settings,
Docker, CI/CD, and tests. Recommendation algorithms are added later behind typed
adapters.

## Stack

- Python 3.12
- Poetry
- FastAPI
- Uvicorn
- Pydantic
- Pytest
- Ruff
- Mypy
- Docker

## Local Development

Install dependencies:

```bash
poetry install
```

Start the development server:

```bash
poetry run uvicorn recommendation_service.main:app --reload --host 0.0.0.0 --port 8000
```

## Common Commands

```bash
poetry check --lock
poetry run ruff check .
poetry run ruff format .
poetry run mypy src
poetry run pytest
```

## Environment

Create a local `.env` from:

```text
.env.example
```

Important variables:

```text
APP_ENV
HOST
PORT
LOG_LEVEL
SERVICE_NAME
```

## Health Checks

```http
GET /v1/health
GET /v1/health/ready
GET /v1/meta
```

The Gateway should call this service through the private Docker network, not
through a public internet route.

