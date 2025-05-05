# Dockerfile
FROM python:3.10-slim

# Don’t buffer stdout/stderr
ENV PYTHONUNBUFFERED=1

# Build-time fallback secret (overridden at runtime by Render’s env var)
ARG DJANGO_SECRET_KEY="temporary-build-secret"
ENV DJANGO_SECRET_KEY=${DJANGO_SECRET_KEY}

# Build-time sensible defaults for these too
ARG DEBUG="False"
ARG ALLOWED_HOSTS="*"
ARG DATABASE_URL=""
ENV DEBUG=${DEBUG}
ENV ALLOWED_HOSTS=${ALLOWED_HOSTS}
ENV DATABASE_URL=${DATABASE_URL}

# Install system deps for MySQL/PostgreSQL client builds, if you need them
RUN apt-get update \
 && apt-get install -y --no-install-recommends \
      build-essential \
      default-libmysqlclient-dev \
      libpq-dev \
 && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy & install Python deps
COPY requirements.txt .
RUN pip install --upgrade pip \
 && pip install -r requirements.txt

# Copy your code in
COPY . .

# Collect static into /app/staticfiles
RUN python manage.py collectstatic --noinput

# Expose (Render will map $PORT)
EXPOSE 8000

# On container start:
#   1) apply all migrations
#   2) load your admin fixture
#   3) launch Gunicorn
CMD ["sh","-c","\
    python manage.py migrate --noinput && \
    python manage.py loaddata fixtures/admin.json && \
    gunicorn chivent_project.wsgi:application --bind 0.0.0.0:${PORT:-8000}\
"]
