# Usar uma imagem base do Python
FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

COPY ../../requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY ../../django .

EXPOSE 8000

ENV DJANGO_SETTINGS_MODULE=digital_collection.settings

CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
