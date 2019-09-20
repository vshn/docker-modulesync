FROM ruby:2.5-slim

LABEL maintainer="VSHN AG <tech@vshn.ch>"

WORKDIR /app

RUN adduser --disabled-password --gecos '' msync \
 && apt-get update \
 && apt-get install -y --no-install-recommends \
      build-essential \
      git \
 && gem install modulesync --version 1.0.0 \
 && apt-get purge -y build-essential \
 && apt-get autoremove --purge -y \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

USER msync

CMD ["msync"]
