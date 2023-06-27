ARG REPO_URL

FROM ubuntu:22.04

WORKDIR /app

RUN apt-get -y update && apt-get -y install git && apt-get install -y python3.10

RUN git clone $REPO_URL
