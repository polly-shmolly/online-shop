FROM python:3.10.2

ENV PYTHONBUFFERED 1
ENV DJANGO_SUPERUSER_PASSWORD=17022002Polly

WORKDIR /app

COPY requirements.txt ./

RUN pip3 install -r requirements.txt

COPY . .

