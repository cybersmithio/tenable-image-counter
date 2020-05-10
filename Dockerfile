FROM python:alpine

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY tenable-image-counter.py ./

CMD [ "python", "tenable-image-counter.py" ]