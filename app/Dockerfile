FROM python:3.11-slim AS builder

# Install build tools and git for cloning dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
      build-essential \
      libpq-dev \
      git && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/app

# Copy requirements and build wheels
COPY requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /wheels -r requirements.txt

# ─────────────────────────────────────────────

FROM python:3.11-slim

# Install runtime dependencies (including git for GitPython at runtime)
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
      libpq5 \
      git && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /opt/defectdojo

# Install pre-built wheels from the builder stage
COPY --from=builder /wheels /wheels
RUN pip install --no-cache-dir /wheels/*

# Copy application source code
COPY . .

# Remove development-only local_settings to prevent tuple/list merge error
RUN rm -f dojo/settings/local_settings.py

# Use production Django settings module
ENV DJANGO_SETTINGS_MODULE=dojo.settings.settings

# Expose the port uWSGI listens on
EXPOSE 8000

# Launch uWSGI via uwsgi.ini configuration
CMD ["uwsgi", "--ini", "uwsgi.ini"]
