FROM ruby:2.5-slim

LABEL maintainer="VSHN AG <tech@vshn.ch>"

WORKDIR /app

RUN adduser --disabled-password --gecos '' msync \
 && apt-get update \
 && apt-get install -y build-essential git \
 && git clone --depth=1 https://github.com/voxpupuli/modulesync.git \
 && cd modulesync \
 && gem build modulesync.gemspec \
 && gem install --no-document modulesync-*.gem \
 && apt-get purge -y build-essential git \
 && apt-get autoremove --purge -y \
 && apt-get clean \
 && cd .. \
 && rm -rf modulesync

USER msync

CMD ["msync"]
