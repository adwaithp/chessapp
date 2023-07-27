FROM python:3

ENV PYTHONUNBUFFERED 1
RUN mkdir /chess_api
WORKDIR /chess_api
COPY . /chess_api/
RUN pip install -r requirements.txt
