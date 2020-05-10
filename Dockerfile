FROM python:alpine

WORKDIR /usr/src/app

COPY requirements.txt ./

COPY tenable-image-counter.py ./

CMD [ "python", "tenable-image-counter.py" ]