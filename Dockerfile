# Use the official slim Python image
FROM python:3.10-slim

# Ensure stdout/stderr is unbuffered (so logs appear immediately)
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Copy only requirements, install dependencies (cached if requirements.txt doesn’t change)
COPY requirements.txt .
RUN pip install --upgrade pip \
 && pip install -r requirements.txt

# Copy the rest of the application code
COPY . .

# Collect static files into /app/staticfiles
RUN python manage.py collectstatic --noinput

# Expose port 8000 (mapped to $PORT by your host/platform)
EXPOSE 8000

# Run migrations then launch Gunicorn binding to 0.0.0.0:$PORT (default 8000)
CMD ["sh", "-c", "python manage.py migrate && gunicorn chivent_project.wsgi:application --bind 0.0.0.0:${PORT:-8000}"]
