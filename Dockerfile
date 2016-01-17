FROM python:slim

RUN pip install bottle
RUN pip install octohatrack

COPY . /usr/src/app

EXPOSE 8080

ENTRYPOINT ["python", "/usr/src/app/server.py"]

