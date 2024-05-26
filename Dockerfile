FROM python:latest

RUN mkdir code
WORKDIR /code

ADD . /code/
ADD .env.docker /code/.env

ENV APP_NAME=PLACESREMEMBER

RUN pip install -r requirements.txt

CMD gunicorn placesremember.wsgi:application -b 0.0.0.0:8000