ModuleSync
==========

[![dockeri.co](http://dockeri.co/image/vshn/modulesync)](https://hub.docker.com/r/vshn/modulesync/)

[![Build Status](https://img.shields.io/travis/vshn/docker-modulesync/master.svg)](https://travis-ci.org/vshn/docker-modulesync
) [![GitHub issues](https://img.shields.io/github/issues-raw/vshn/docker-modulesync.svg)](https://github.com/vshn/docker-modulesync/issues
) [![GitHub PRs](https://img.shields.io/github/issues-pr-raw/vshn/docker-modulesync.svg)](https://github.com/vshn/docker-modulesync/pulls
) [![MIT License](https://img.shields.io/github/license/vshn/docker-modulesync.svg)](https://github.com/vshn/docker-modulesync/blob/master/LICENSE)

Repository File Sync
--------------------

Originally, a utility script to keep configuration files in sync for Puppet modules,
[ModuleSync](https://github.com/voxpupuli/modulesync/) allows you to keep files in
sync across your many repositories on your Git servers. Pulls your repositories,
applies and commits changes based on the file templates you prepare, and pushes the
changes back to each repo. PR support is included (for GitHub only, as of today).

This Docker image runs ModuleSync with an unprivileged `msync` user in `/app`.

Supported Tags
--------------

- [`latest`](
  https://github.com/vshn/docker-modulesync/blob/master/Dockerfile) [![image layers](
  https://img.shields.io/microbadger/layers/vshn/modulesync/latest.svg)](
  https://microbadger.com/images/vshn/modulesync) [![image size](
  https://img.shields.io/microbadger/image-size/vshn/modulesync/latest.svg)](
  https://microbadger.com/images/vshn/modulesync) (based on current GitHub `master`)
- [`0.10.0`](
  https://github.com/vshn/docker-modulesync/blob/master/0.10.0/Dockerfile) [![image layers](
  https://img.shields.io/microbadger/layers/vshn/modulesync/0.10.0.svg)](
  https://microbadger.com/images/vshn/modulesync) [![image size](
  https://img.shields.io/microbadger/image-size/vshn/modulesync/0.10.0.svg)](
  https://microbadger.com/images/vshn/modulesync) ([Ruby Gem v0.10.0](
  https://rubygems.org/gems/modulesync/versions/0.10.0))
- [`0.9.0`](
  https://github.com/vshn/docker-modulesync/blob/master/0.9.0/Dockerfile) [![image layers](
  https://img.shields.io/microbadger/layers/vshn/modulesync/0.9.0.svg)](
  https://microbadger.com/images/vshn/modulesync) [![image size](
  https://img.shields.io/microbadger/image-size/vshn/modulesync/0.9.0.svg)](
  https://microbadger.com/images/vshn/modulesync) ([Ruby Gem v0.9.0](
  https://rubygems.org/gems/modulesync/versions/0.9.0))

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
