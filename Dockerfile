FROM python:3.7.4

RUN apt-get update
RUN pip install flask
RUN mkdir /app