FROM python:slim

COPY . /usr/src/app

RUN pip install bottle
RUN cd /usr/src/app/octohatrack && pip install .


EXPOSE 8080

ENTRYPOINT ["/usr/local/bin/python", "/usr/src/app/server.py"]

