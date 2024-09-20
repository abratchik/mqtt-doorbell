# образ на основе которого создаём контейнер
FROM python:alpine

WORKDIR /config



# переменные окружения для python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# RUN apk update && apk add --no-cache build-base cmake pkgconf cairo-dev gobject-introspection-dev
# RUN pip install --upgrade setuptools wheel
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt
RUN pip uninstall pipenv -y

COPY . .

# RUN ["ln", "-sf", "/usr/local/bin/python3", "/usr/bin/python3"]
RUN ["chmod", "+x", "/config/entrypoint.sh"]

ENTRYPOINT ["/config/entrypoint.sh"]