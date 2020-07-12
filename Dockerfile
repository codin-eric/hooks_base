FROM python:3.8

RUN apt-get update -y
RUN pip install -U pip
ADD requirements.txt /requirements.txt
RUN pip install -r requirements.txt