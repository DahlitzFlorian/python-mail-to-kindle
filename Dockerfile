FROM floriandahlitz/docker-calibre:latest

USER worker
WORKDIR /home/worker

RUN python -m pip install --upgrade pip
RUN python -m pip install pipenv

COPY --chown=worker:worker Pipfile Pipfile
RUN pipenv lock -r > requirements.txt
RUN pip install -r requirements.txt

LABEL maintainer="Florian Dahlitz <f2dahlitz@freenet.de>" \
      version="1.1.1"

COPY --chown=worker:worker . .