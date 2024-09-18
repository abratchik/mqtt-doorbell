# образ на основе которого создаём контейнер
FROM python:alpine

WORKDIR /config



# переменные окружения для python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .

RUN ["chmod", "+x", "/config/entrypoint.sh"]

ENTRYPOINT ["/config/entrypoint.sh"]