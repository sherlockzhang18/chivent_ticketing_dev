# Dockerfile

# Base image
FROM python:3.10-slim

# Don’t buffer stdout/stderr
ENV PYTHONUNBUFFERED=1

# Build‐time default for SECRET_KEY (overridden at runtime by your Render env var)
ARG DJANGO_SECRET_KEY="temporary-build-secret"
ENV DJANGO_SECRET_KEY=${DJANGO_SECRET_KEY}

# Runtime defaults
ENV DEBUG=False \
    ALLOWED_HOSTS="*"

# Set working directory
WORKDIR /app

# Install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip \
 && pip install -r requirements.txt

# Copy project code
COPY . .

# Collect static files
RUN python manage.py collectstatic --noinput

# Expose the port (Render will set $PORT for you)
EXPOSE 8000

# On container start:
#  1. run migrations
#  2. load your admin fixture
#  3. launch gunicorn
CMD ["sh", "-c", "\
    python manage.py migrate --noinput && \
    python manage.py loaddata fixtures/admin.json && \
    gunicorn chivent_project.wsgi:application --bind 0.0.0.0:${PORT:-8000}\
"]
