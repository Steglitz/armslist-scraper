FROM python:2.7
RUN apt-get update && apt-get install -y parallel

COPY requirements.txt /usr/src/app/
RUN pip install -r /usr/src/app/requirements.txt
COPY . /usr/src/app/

ENV PYTHONPATH=/usr/src/app

WORKDIR /usr/src/app

CMD ["./scrape.sh"]
