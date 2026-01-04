# PolyVoice Development Dockerfile
# Multi-stage build for efficient image size

# Stage 1: Builder
FROM python:3.11-slim as builder

# Install Poetry
ENV POETRY_VERSION=1.8.4
ENV POETRY_HOME=/opt/poetry
ENV POETRY_VENV=/opt/poetry-venv
ENV POETRY_CACHE_DIR=/opt/.cache

RUN python -m venv $POETRY_VENV \
    && $POETRY_VENV/bin/pip install -U pip setuptools \
    && $POETRY_VENV/bin/pip install poetry==$POETRY_VERSION

# Set up project
WORKDIR /app
COPY pyproject.toml poetry.lock ./

# Install dependencies (no dev deps for production, with dev for development)
ARG INSTALL_DEV=true
RUN $POETRY_VENV/bin/poetry config virtualenvs.create false \
    && if [ "$INSTALL_DEV" = "true" ]; then \
         $POETRY_VENV/bin/poetry install --no-interaction --no-ansi; \
       else \
         $POETRY_VENV/bin/poetry install --no-interaction --no-ansi --only main; \
       fi

# Stage 2: Runtime
FROM python:3.11-slim as runtime

# Install system dependencies for audio processing (will be needed later)
RUN apt-get update && apt-get install -y --no-install-recommends \
    ffmpeg \
    libsndfile1 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy installed packages from builder
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

# Copy application code
COPY src/ ./src/
COPY scripts/ ./scripts/

# Set Python path
ENV PYTHONPATH=/app/src

# Default command
CMD ["python", "-c", "import polyvoice; print(f'PolyVoice v{polyvoice.__version__}')"]
