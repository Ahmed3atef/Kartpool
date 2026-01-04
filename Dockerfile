FROM python:3.12-slim-bookworm

# Install system dependencies required for GeoDjango and GDAL
RUN apt-get update && apt-get install -y \
    binutils \
    libproj-dev \
    gdal-bin \
    libgdal-dev \
    python3-gdal \
    && rm -rf /var/lib/apt/lists/*

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

# Install uv for dependency management
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

# Copy dependency files
COPY pyproject.toml uv.lock ./

# Install dependencies
RUN uv sync --frozen --no-dev

# Copy project files
COPY . .

# Start command: Collect static files then run gunicorn
CMD ["sh", "-c", "uv run python manage.py collectstatic --noinput && uv run gunicorn kartpool.wsgi:application --bind 0.0.0.0:8000"]
