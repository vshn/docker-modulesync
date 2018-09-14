#!/usr/bin/env python3
"""
Creates and updates version-based Dockerfile folders.
"""
from os import makedirs, path

VERSIONS = [
    # add new versions here
    '0.9.0',
]
DOCKER_IMAGE = 'vshn/modulesync'
GIT_REPO = 'vshn/docker-modulesync'


def create_dockerfile(ver):
    """
    Create a Dockerfile in a version subdirectory, taking the main,
    off-repository install based, Dockerfile as a template.
    """
    print(f"Updating Dockerfile: version {ver} ...")

    build_commands_needle = ' git clone '
    install_command = f" gem install modulesync --version {ver}"
    empty_line = '\n\n'

    makedirs(ver, exist_ok=True)
    target_filename = path.join(ver, 'Dockerfile')

    # replace gem build command sequence by gem install command
    with open('Dockerfile', 'r') as dockerfile, \
            open(target_filename, 'w') as target_file:
        original = dockerfile.read()
        start = original.index(build_commands_needle)
        stop = original.index(empty_line, start)
        target_conf = original[:start] + install_command + original[stop:]
        target_file.write(target_conf)


def add_tag_badge_to_readme(ver):
    """
    Add links of supported tags to the README.
    """
    print(f"Updating README: tag {ver} ...")

    dockerfile_url = f"https://github.com/{GIT_REPO}/blob/master/{ver}/Dockerfile"
    imagelayers_badge = f"https://img.shields.io/imagelayers/layers/" \
                        f"{DOCKER_IMAGE}/{ver}.svg"
    imagelayers_url = f"https://imagelayers.io/?images={DOCKER_IMAGE}:{ver}"
    rubygem_url = f"https://rubygems.org/gems/modulesync/versions/{ver}"
    tag_lines = [
        f"- [`{ver}`]({dockerfile_url}) [![Image Layers](",
        f"  {imagelayers_badge})]({imagelayers_url}",
        f"  ) ([Ruby Gem v{ver}]({rubygem_url}))",
    ]
    tag_anchor = f"  ) (based on current GitHub `master`)"

    with open('README.md', 'r+') as readme:
        lines = readme.read().splitlines()
        for line in tag_lines:
            if line in lines:
                lines.remove(line)
        anchor = lines.index(tag_anchor) + 1
        lines = lines[:anchor] + tag_lines + lines[anchor:]

        readme.seek(0)
        readme.write('\n'.join(lines) + '\n')
        readme.truncate()


def main():
    """
    Take the main Dockerfile as a template and create Dockerfiles in
    subdirectories (with ModuleSync version numbers), replacing the 'bundle
    install' by Ruby Gem installs. Also update the README file.
    """
    for version in VERSIONS:
        create_dockerfile(version)
        add_tag_badge_to_readme(version)

    print(f"Done. Put the changes under version control now, "
          f"and update your Docker image configuration at "
          f"https://hub.docker.com/r/{DOCKER_IMAGE}/~/settings/automated-builds/. "
          f"Thank you!")


if __name__ == '__main__':
    main()
