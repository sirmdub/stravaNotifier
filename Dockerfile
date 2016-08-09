FROM python:2-alpine

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
RUN pip install -t . stravalib==0.6.0 redis==2.10.5
COPY . /usr/src/app

RUN apk add --no-cache --virtual zip
RUN zip -r stravaNotifier.zip .

CMD [ "python", "./run.py" ]