FROM python:slim


#RUN export DEBIAN_FRONTEND=noninteractive && apt-get update && apt-get install -y python-pip python-dev && apt-get clean

RUN pip install bottle
RUN pip install octohatrack

RUN groupadd -r apprunner
RUN useradd -r -g apprunner -d / -s /usr/sbin/nologin -c "Docker image user" apprunner

COPY . /usr/src/app



ENTRYPOINT ["python", "/usr/src/app/server.py"]

