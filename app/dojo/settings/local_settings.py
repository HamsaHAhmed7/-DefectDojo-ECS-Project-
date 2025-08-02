import os

SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY", "changeme-please")

DEBUG = True

# Enable message middleware workaround (redundant if already in settings)
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django_prometheus.middleware.PrometheusBeforeMiddleware",
    "django_prometheus.middleware.PrometheusAfterMiddleware",
]

INSTALLED_APPS = list(INSTALLED_APPS) + ["django_prometheus"]

DATABASES["default"]["ENGINE"] = DATABASES["default"]["ENGINE"].replace("django.", "django_prometheus.", 1)

LOGIN_EXEMPT_URLS += (r"^django_metrics/",)
