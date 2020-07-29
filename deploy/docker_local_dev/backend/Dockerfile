FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /var/log/backend
RUN touch /var/log/backend/django.log
RUN mkdir /provision
WORKDIR /provision
COPY deploy/docker_local_dev/backend/requirements.txt requirements.txt
RUN pip install -r requirements.txt --compile --no-cache-dir
RUN python -m nltk.downloader punkt
RUN mkdir /app
WORKDIR /app
