FROM docker.io/library/ruby:3.3-slim
WORKDIR /app

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
      git \
      openssh-client && \
    apt-get clean all && \
    rm -rf /var/lib/apt/lists/* && \
    adduser --disabled-password --gecos '' msync

# renovate: datasource=rubygems depName=modulesync versioning=ruby
ENV MODULESYNC_VERSION="3.2.0"
RUN gem install modulesync --version="$MODULESYNC_VERSION"

USER msync
CMD ["msync", "help"]
