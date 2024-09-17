# Dockerfile for the Python application
FROM python:3.9-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir mysql-connector-python requests python-dotenv

CMD ["python", "book_fetcher.py"]
