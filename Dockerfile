# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /app

COPY mycodingsite/requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY mycodingsite .

EXPOSE 8000

CMD [ "python","manage.py", "runserver", "0.0.0.0:8000"]