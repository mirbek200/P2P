# Используем базовый образ Python 3.10
FROM python:3.10

# Устанавливаем переменные окружения
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Устанавливаем PostgreSQL клиент
RUN apt-get update && apt-get install -y postgresql-client

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем requirements.txt и устанавливаем зависимости
COPY ./requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Устанавливаем psycopg2-binary для подключения к PostgreSQL
RUN pip install psycopg2-binary

# Копируем файлы из каталога ./docker внутрь контейнера
COPY ./docker /app/docker

# Копируем только необходимые файлы и директории для вашего приложения
COPY . /app/backend

# Предоставляем права на выполнение для wsgi-entrypoint.sh, если это необходимо
RUN ["chmod", "+x", "/app/docker/backend/wsgi-entrypoint.sh"]

# Открываем порт 8000
EXPOSE 8000

# Команда для запуска вашего приложения
CMD ["./docker/backend/wsgi-entrypoint.sh"]
