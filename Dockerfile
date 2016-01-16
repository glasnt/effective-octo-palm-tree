FROM python:slim

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY . /usr/src/app
RUN pip install octohatrack

RUN pip install bottle

RUN groupadd web
RUN useradd -d /usr/src/app -m bottle


# in case you'd prefer to use links, expose the port
EXPOSE 8081
ENTRYPOINT ["/usr/bin/python", "/usr/src/app/server.py"]
USER bottle
