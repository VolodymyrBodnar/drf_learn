FROM python:3.7-slim

ENV PYTHONUNBUFFERED 1

RUN mkdir /src
WORKDIR /src

COPY . /src/

RUN pip install -r requirements.txt 