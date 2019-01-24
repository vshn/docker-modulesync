FROM ruby:2.5.1

LABEL maintainer="VSHN AG <tech@vshn.ch>"

WORKDIR /app

RUN adduser --disabled-password --gecos '' msync \
 && git clone --depth=1 https://github.com/voxpupuli/modulesync.git \
 && cd modulesync \
 && gem build modulesync.gemspec \
 && gem install --no-document modulesync-*.gem \
 && cd .. \
 && rm -rf modulesync

USER msync

CMD ["msync"]
