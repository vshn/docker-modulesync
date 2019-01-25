FROM ruby:2.5-slim

LABEL maintainer="VSHN AG <tech@vshn.ch>"

WORKDIR /app

RUN adduser --disabled-password --gecos '' msync \
 && apt-get update \
 && apt-get install -y build-essential \
 && gem install modulesync --version 0.9.0 \
 && apt-get purge -y build-essential \
 && apt-get autoremove --purge -y \
 && apt-get clean

USER msync

CMD ["msync"]
