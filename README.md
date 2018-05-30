ModuleSync
==========

[![dockeri.co](http://dockeri.co/image/vshn/modulesync)](https://hub.docker.com/r/vshn/modulesync/)

[![MIT License](https://img.shields.io/github/license/vshn/docker-modulesync.svg)](https://github.com/vshn/docker-modulesync/blob/master/LICENSE
) [![GitHub issues](https://img.shields.io/github/issues-raw/vshn/docker-modulesync.svg)](https://github.com/vshn/docker-modulesync/issues
) [![GitHub PRs](https://img.shields.io/github/issues-pr-raw/vshn/docker-modulesync.svg)](https://github.com/vshn/docker-modulesync/pulls)

Repository File Sync
--------------------

Originally, a utility script to keep configuration files in sync for Puppet modules,
[ModuleSync](https://github.com/voxpupuli/modulesync/) allows you to keep files in
sync across your many repositories on your Git servers. Pulls your repositories,
applies and commits changes based on the file templates you prepare, and pushes the
changes back to each repo. PR support is included (for GitHub only, as of today).

Supported Tags
--------------

- [`latest`](https://github.com/vshn/docker-modulesync/blob/master/Dockerfile) [![Image Layers](
  https://img.shields.io/imagelayers/layers/vshn/modulesync/latest.svg)](https://imagelayers.io/?images=vshn/modulesync:latest
  ) (based on current GitHub `master`)
- [`0.9.0`](https://github.com/vshn/docker-modulesync/blob/master/0.9.0/Dockerfile) [![Image Layers](
  https://img.shields.io/imagelayers/layers/vshn/modulesync/0.9.0.svg)](https://imagelayers.io/?images=vshn/modulesync:0.9.0
  ) ([Ruby Gem v0.9.0](https://rubygems.org/gems/modulesync/versions/0.9.0))

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
