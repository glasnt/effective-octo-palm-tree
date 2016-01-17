FROM python:slim

RUN pip install bottle
RUN pip install octohatrack

COPY . /usr/src/app

EXPOSE 8080

ENTRYPOINT ["/usr/local/bin/python", "/usr/src/app/server.py"]

