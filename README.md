ModuleSync
==========

[![dockeri.co](http://dockeri.co/image/vshn/modulesync)](https://hub.docker.com/r/vshn/modulesync/)

[![Build Status](https://img.shields.io/travis/vshn/docker-modulesync/master.svg)](https://travis-ci.org/vshn/docker-modulesync
) [![GitHub issues](https://img.shields.io/github/issues-raw/vshn/docker-modulesync.svg)](https://github.com/vshn/docker-modulesync/issues
) [![GitHub PRs](https://img.shields.io/github/issues-pr-raw/vshn/docker-modulesync.svg)](https://github.com/vshn/docker-modulesync/pulls
) [![License](https://img.shields.io/github/license/vshn/docker-modulesync.svg)](https://github.com/vshn/docker-modulesync/blob/master/LICENSE)

Repository File Sync
--------------------

Originally, a utility script to keep configuration files in sync for Puppet modules,
[ModuleSync](https://github.com/voxpupuli/modulesync/) allows you to keep files in
sync across your many repositories on your Git servers. Pulls your repositories,
applies and commits changes based on the file templates you prepare, and pushes the
changes back to each repo. Support for creating GitHub PRs and GitLab MRs (since v2.0.0)
in an automated fashion is included.

This Docker image runs ModuleSync with an unprivileged `msync` user in `/app`.

See [Concierge](https://github.com/vshn/docker-concierge/) if you want to sync
multiple configurations from a single configuration repository.

Supported Tags
--------------

- [![latest](
  https://img.shields.io/badge/latest-blue.svg?colorA=22313f&colorB=4a637b&logo=docker)](
  https://github.com/vshn/docker-modulesync/blob/master/Dockerfile) [![size/layers](
  https://images.microbadger.com/badges/image/vshn/modulesync:latest.svg)](
  https://microbadger.com/images/vshn/modulesync:latest) [![based on](
  https://img.shields.io/badge/Git-master-grey.svg?colorA=5a5b5c&colorB=9a9b9c&logo=github)](
  https://github.com/voxpupuli/modulesync)
- [![2.0.0](
  https://img.shields.io/badge/2.0.0-blue.svg?colorA=22313f&colorB=4a637b&logo=docker)](
  https://github.com/vshn/docker-modulesync/blob/master/2.0.0/Dockerfile) [![size/layers](
  https://images.microbadger.com/badges/image/vshn/modulesync:2.0.0.svg)](
  https://microbadger.com/images/vshn/modulesync:2.0.0) [![based on](
  https://img.shields.io/badge/Gem-2.0.0-red.svg?colorA=ff919f&colorB=9a9b9c&logo=ruby)](
  https://rubygems.org/gems/modulesync/versions/2.0.0)
- [![1.3.0](
  https://img.shields.io/badge/1.3.0-blue.svg?colorA=22313f&colorB=4a637b&logo=docker)](
  https://github.com/vshn/docker-modulesync/blob/master/1.3.0/Dockerfile) [![size/layers](
  https://images.microbadger.com/badges/image/vshn/modulesync:1.3.0.svg)](
  https://microbadger.com/images/vshn/modulesync:1.3.0) [![based on](
  https://img.shields.io/badge/Gem-1.3.0-red.svg?colorA=ff919f&colorB=9a9b9c&logo=ruby)](
  https://rubygems.org/gems/modulesync/versions/1.3.0)
- [![1.2.0](
  https://img.shields.io/badge/1.2.0-blue.svg?colorA=22313f&colorB=4a637b&logo=docker)](
  https://github.com/vshn/docker-modulesync/blob/master/1.2.0/Dockerfile) [![size/layers](
  https://images.microbadger.com/badges/image/vshn/modulesync:1.2.0.svg)](
  https://microbadger.com/images/vshn/modulesync:1.2.0) [![based on](
  https://img.shields.io/badge/Gem-1.2.0-red.svg?colorA=ff919f&colorB=9a9b9c&logo=ruby)](
  https://rubygems.org/gems/modulesync/versions/1.2.0)
- [![1.1.0](
  https://img.shields.io/badge/1.1.0-blue.svg?colorA=22313f&colorB=4a637b&logo=docker)](
  https://github.com/vshn/docker-modulesync/blob/master/1.1.0/Dockerfile) [![size/layers](
  https://images.microbadger.com/badges/image/vshn/modulesync:1.1.0.svg)](
  https://microbadger.com/images/vshn/modulesync:1.1.0) [![based on](
  https://img.shields.io/badge/Gem-1.1.0-red.svg?colorA=ff919f&colorB=9a9b9c&logo=ruby)](
  https://rubygems.org/gems/modulesync/versions/1.1.0)
- [![1.0.0](
  https://img.shields.io/badge/1.0.0-blue.svg?colorA=22313f&colorB=4a637b&logo=docker)](
  https://github.com/vshn/docker-modulesync/blob/master/1.0.0/Dockerfile) [![size/layers](
  https://images.microbadger.com/badges/image/vshn/modulesync:1.0.0.svg)](
  https://microbadger.com/images/vshn/modulesync:1.0.0) [![based on](
  https://img.shields.io/badge/Gem-1.0.0-red.svg?colorA=ff919f&colorB=9a9b9c&logo=ruby)](
  https://rubygems.org/gems/modulesync/versions/1.0.0)
- [![0.10.0](
  https://img.shields.io/badge/0.10.0-blue.svg?colorA=22313f&colorB=4a637b&logo=docker)](
  https://github.com/vshn/docker-modulesync/blob/master/0.10.0/Dockerfile) [![size/layers](
  https://images.microbadger.com/badges/image/vshn/modulesync:0.10.0.svg)](
  https://microbadger.com/images/vshn/modulesync:0.10.0) [![based on](
  https://img.shields.io/badge/Gem-0.10.0-red.svg?colorA=ff919f&colorB=9a9b9c&logo=ruby)](
  https://rubygems.org/gems/modulesync/versions/0.10.0)
- [![0.9.0](
  https://img.shields.io/badge/0.9.0-blue.svg?colorA=22313f&colorB=4a637b&logo=docker)](
  https://github.com/vshn/docker-modulesync/blob/master/0.9.0/Dockerfile) [![size/layers](
  https://images.microbadger.com/badges/image/vshn/modulesync:0.9.0.svg)](
  https://microbadger.com/images/vshn/modulesync:0.9.0) [![based on](
  https://img.shields.io/badge/Gem-0.9.0-red.svg?colorA=ff919f&colorB=9a9b9c&logo=ruby)](
  https://rubygems.org/gems/modulesync/versions/0.9.0)

Usage
-----

In a GitLab CI configuration file:

```
  image: vshn/modulesync
  script:
    - msync update
```

In a Docker Compose file as a pseudo-service:

```
  modulesync:
    image: vshn/modulesync
    volumes:
      - .:/app
```

With Docker on the command line:

```bash
$ docker run --rm -v "$PWD":/app vshn/modulesync msync update
```

Development
-----------

- [Issue tracker](https://github.com/vshn/docker-modulesync/) (GitHub)

To add a new ModuleSync version tag:

1. Add the version number to the [update script](
   https://github.com/vshn/docker-modulesync/blob/master/update.py#L7-L10), and
1. Run `./update.py` and update the Docker build settings as indicated.

Please, run [tox](https://tox.readthedocs.io/) before contributing changes.
