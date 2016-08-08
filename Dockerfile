FROM python:2-slim

RUN pip install stravalib==0.6.0 redis==2.10.5
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY . /usr/src/app

CMD [ "python", "./run.py" ]