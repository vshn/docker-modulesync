FROM ruby:2.5.1

LABEL maintainer "VSHN AG <tech@vshn.ch>"

WORKDIR /app

RUN adduser --disabled-password --gecos '' msync \
 && gem install modulesync --version 0.9.0

USER msync

CMD ["msync"]
