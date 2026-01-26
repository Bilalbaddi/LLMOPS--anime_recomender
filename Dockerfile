## Parent image
FROM python:3.10-slim

## 1. INSTALL UV (The modern way)
# We copy the 'uv' binary directly from Astral's official image.
# This is much cleaner/safer than running a curl install script.
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

## Essential environment variables
# UV_SYSTEM_PYTHON=1 tells uv to install packages into the system python
# (instead of forcing you to create a virtual environment inside the container).
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    UV_SYSTEM_PYTHON=1

## Work directory inside the docker container
WORKDIR /app

## Installing system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

## Copying all contents from local to app
COPY . .

## Run setup.py using UV
# --system: Installs into the main python environment (no venv needed in Docker)
# -e .: Installs your project in editable mode
RUN uv pip install --system -e .

# Used PORTS
EXPOSE 8501

# Run the app 
CMD ["streamlit", "run", "app/app.py", "--server.port=8501", "--server.address=0.0.0.0", "--server.headless=true"]