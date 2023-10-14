FROM python:3.7

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y postgresql-client

WORKDIR /app

COPY ./requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN pip install psycopg2


COPY ./docker /app/docker

COPY . /app/backend

RUN ["chmod", "+x", "/app/docker/backend/wsgi-entrypoint.sh"]

EXPOSE 8000

CMD ["./docker/backend/wsgi-entrypoint.sh"]
