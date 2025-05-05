# Dockerfile
FROM python:3.10-slim

ENV PYTHONUNBUFFERED=1

# Build-time defaults (overridden at runtime by Render env)
ARG DJANGO_SECRET_KEY="temporary-build-secret"
ENV DJANGO_SECRET_KEY=${DJANGO_SECRET_KEY}
ARG DEBUG="False"
ENV DEBUG=${DEBUG}
ARG ALLOWED_HOSTS="*"
ENV ALLOWED_HOSTS=${ALLOWED_HOSTS}
ARG DATABASE_URL=""
ENV DATABASE_URL=${DATABASE_URL}

# Install client libs
RUN apt-get update \
 && apt-get install -y --no-install-recommends \
      build-essential \
      default-libmysqlclient-dev \
      libpq-dev \
 && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip \
 && pip install -r requirements.txt

COPY . .

# collect static at build time
RUN python manage.py collectstatic --noinput

EXPOSE 8000

# on start: migrate → load our fixture → serve
CMD ["sh","-c","\
    python manage.py migrate --noinput && \
    python manage.py loaddata fixtures/admin.json && \
    gunicorn chivent_project.wsgi:application --bind 0.0.0.0:${PORT:-8000}\
"]
