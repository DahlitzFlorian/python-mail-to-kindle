FROM floriandahlitz/docker-calibre:latest

RUN mkdir /app
WORKDIR /app

RUN python -m pip install pipenv

COPY Pipfile Pipfile
RUN pipenv lock -r > requirements.txt
RUN pip install -r requirements.txt

LABEL maintainer="Florian Dahlitz <f2dahlitz@freenet.de>" \
      version="1.0.0"

COPY . .