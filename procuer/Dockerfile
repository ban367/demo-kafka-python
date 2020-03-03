FROM python:3.7.6-slim

ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./

RUN pip install -r requirements.txt --no-cache-dir
