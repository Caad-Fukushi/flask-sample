FROM python:3.7.4

RUN apt-get update
RUN pip install flask
RUN apt-get install -y sqlite3 libsqlite3-dev
RUN pip install sqlalchemy
RUN mkdir /app