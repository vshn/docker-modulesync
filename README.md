# ModuleSync

## Repository File Sync

Originally, a utility script to keep configuration files in sync for Puppet modules,
[ModuleSync](https://github.com/voxpupuli/modulesync/) allows you to keep files in
sync across your many repositories on your Git servers. Pulls your repositories,
applies and commits changes based on the file templates you prepare, and pushes the
changes back to each repo. Support for creating GitHub PRs and GitLab MRs (since v2.0.0)
in an automated fashion is included.

This Docker image runs ModuleSync with an unprivileged `msync` user in `/app`.

See [Concierge](https://github.com/vshn/docker-concierge/) if you want to sync
multiple configurations from a single configuration repository.

## Usage

In a GitLab CI configuration file:

```yaml
image: ghcr.io/vshn/modulesync
script:
  - msync update
```

With Docker on the command line:

```sh
$ docker run --rm -v "$PWD":/app ghcr.io/vshn/modulesync msync update
```

## Development

- [Issue tracker](https://github.com/vshn/docker-modulesync/) (GitHub)

To add a new ModuleSync version tag:

1. Renovate should automatically create a [Pull Request](https://github.com/vshn/docker-modulesync/pulls).
1. After merging it, make sure you pulled the latest commits, and run `./tag.sh` to create an appropriate Git Tag.
1. `git push --follow-tags` to push the tag. A new docker image is built automatically.
