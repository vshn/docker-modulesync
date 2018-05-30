ModuleSync
==========

[![dockeri.co](http://dockeri.co/image/vshn/modulesync)](https://hub.docker.com/r/vshn/modulesync/)

[![MIT License](https://img.shields.io/github/license/vshn/docker-modulesync.svg)](https://github.com/vshn/docker-modulesync/blob/master/LICENSE
) [![GitHub issues](https://img.shields.io/github/issues-raw/vshn/docker-modulesync.svg)](https://github.com/vshn/docker-modulesync/issues
) [![GitHub PRs](https://img.shields.io/github/issues-pr-raw/vshn/docker-modulesync.svg)](https://github.com/vshn/docker-modulesync/pulls)

Repository File Sync
--------------------

Originally a utility script to keep configuration files in sync for Puppet modules,
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

Add a pseudo-service to your Docker Compose configuration, e.g.

```
  modulesync:
    image: vshn/modulesync
    volumes:
      - .:/var/www/html
```

Development
-----------

- [Contribute](https://github.com/vshn/docker-modulesync/) (GitHub repository)

Please, run [tox](https://tox.readthedocs.io/) before contributing changes.
