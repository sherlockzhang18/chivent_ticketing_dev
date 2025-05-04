# Dockerfile
FROM python:3.10-slim

# Don’t buffer stdout/stderr
ENV PYTHONUNBUFFERED=1

# Provide a build‐time default secret key so collectstatic (and any import of settings)
# doesn’t blow up. This will be overridden at runtime by your Render env var.
ARG DJANGO_SECRET_KEY="temporary-build-secret"
ENV DJANGO_SECRET_KEY=${DJANGO_SECRET_KEY}

# Also set sensible defaults for these at build time
ENV DEBUG=False \
    ALLOWED_HOSTS="*"

WORKDIR /app

# Install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip \
 && pip install -r requirements.txt

# Copy all your code
COPY . .

# Collect static files
RUN python manage.py collectstatic --noinput

# Expose port (on Render, $PORT will be set automatically)
EXPOSE 8000

# On start: run migrations then launch Gunicorn
CMD ["sh","-c","python manage.py migrate --noinput && gunicorn chivent_project.wsgi:application --bind 0.0.0.0:${PORT:-8000}"]
