# Base image
FROM python:3.11-slim


# Create a non-root user for security
RUN useradd -m appuser

# Set working directory
WORKDIR /app

# Install system dependencies required for building Python packages and PostgreSQL client
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    gcc \
    build-essential \
    dnsutils \
    libpq-dev \
    postgresql-client \
    xmlsec1 \
    git \
    uuid-runtime \
    libcurl4-openssl-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Copy only requirements first to leverage Docker layer caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy app source code
COPY . .

EXPOSE 8080

# Run the Django app with Gunicorn using WSGI entry point
CMD ["gunicorn", "dojo.wsgi:application", "--bind", "0.0.0.0:8080"]
