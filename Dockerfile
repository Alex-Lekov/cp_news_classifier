# =============================================================================
# Build environment
FROM python:3.8-slim as build

# Install Poetry
RUN pip install poetry

# Create Poetry environment
COPY poetry.lock pyproject.toml /
RUN POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=true \
    poetry install \
    python setup.py develop

# =============================================================================
# Runtime environment
FROM python:3.8-slim as runtime

# Copy Poetry environment
COPY --from=build .venv .venv

# Update PATH
ENV PATH="/.venv/bin:$PATH"