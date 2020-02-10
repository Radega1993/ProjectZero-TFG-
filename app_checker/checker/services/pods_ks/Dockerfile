FROM python:alpine3.7

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt


EXPOSE 8000
ENTRYPOINT gunicorn --bind 0.0.0.0:8000 wsgi:app
