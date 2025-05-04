FROM python:3.10-slim

RUN apt-get update \
 && apt-get install -y default-libmysqlclient-dev build-essential \
 && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY requirements.txt .
RUN pip install --upgrade pip \
 && pip install -r requirements.txt

COPY . .

RUN python manage.py collectstatic --noinput

EXPOSE 8000
CMD ["sh", "-c", "python manage.py migrate --noinput && gunicorn chivent_project.wsgi:application --bind 0.0.0.0:8000"]
