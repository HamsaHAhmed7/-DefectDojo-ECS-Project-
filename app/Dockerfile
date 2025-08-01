FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN apt-get -y update && \
  apt-get -y install --no-install-recommends \
    gcc \
    build-essential \
    dnsutils \
    libpq-dev \
    postgresql-client \
    xmlsec1 \
    git \
    uuid-runtime \
    # libcurl4-openssl-dev is required for installing pycurl python package
    libcurl4-openssl-dev \
    && \
  apt-get clean && \
  rm -rf /var/lib/apt/lists && \
  true

EXPOSE 8080

CMD ["python", "dojo/" "manage.py", "wsgi.py"]