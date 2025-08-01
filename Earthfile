VERSION 0.8
FROM python:3.10.18-slim
WORKDIR /earthy-ci

pip:
    ENV PIP_ROOT_USER_ACTION=ignore
    RUN pip install --upgrade pip && pip install poetry

poetry:
    FROM +pip
    COPY . .
    RUN poetry install

ruff-check:
    FROM +poetry
    RUN poetry run ruff check --fix
    RUN --no-cache poetry run ruff check .

build:
    FROM +poetry
    RUN poetry run python3 src

pytest:
    FROM +build
    RUN --no-cache poetry run pytest test -v



all:
    BUILD +build
    BUILD +pytest
    BUILD +ruff-check