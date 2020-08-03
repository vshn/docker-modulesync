#!/usr/bin/env python3
"""
Creates and updates version-based Dockerfile folders.
"""
from os import makedirs, path

VERSIONS = [
    '0.9.0',
    '0.10.0',
    '1.0.0',
    '1.1.0',
    '1.2.0',
    '1.3.0',
    # add new versions here
]
DOCKER_IMAGE = 'vshn/modulesync'
DOCKERHUB_USER = 'vshn'
GIT_REPO = 'vshn/docker-modulesync'

EMPTY_LINE = '\n\n'

README_TAG_ANCHOR = '  https://github.com/voxpupuli/modulesync)'

TESTS_CONTEXT_NEEDLE = '  - CONTEXT='
TESTS_CONTEXT_ANCHOR = '  - CONTEXT=.'


def create_dockerfile(ver):
    """
    Create a Dockerfile in a version subdirectory, taking the main,
    off-repository install based, Dockerfile as a template.
    """
    print(f"Updating Dockerfile: version {ver} ...")

    build_commands_needle = ' && apt-get update '
    install_commands = [
        " && apt-get update \\",
        " && apt-get install -y --no-install-recommends \\",
        "      build-essential \\",
        "      git \\",
        f" && gem install modulesync --version {ver} \\",
        " && apt-get purge -y build-essential \\",
        " && apt-get autoremove --purge -y \\",
        " && apt-get clean \\",
        " && rm -rf /var/lib/apt/lists/*",
    ]

    makedirs(ver, exist_ok=True)
    target_filename = path.join(ver, 'Dockerfile')

    # replace gem build command sequence by gem install command
    with open('Dockerfile', 'r') as dockerfile, \
            open(target_filename, 'w') as target_file:
        original = dockerfile.read()
        start = original.index(build_commands_needle)
        stop = original.index(EMPTY_LINE, start)
        target_conf = (
            original[:start] +
            '\n'.join(install_commands) +
            original[stop:]
        )
        target_file.write(target_conf)


def remove_old_badges_from_readme():
    """
    Remove all version tag badges from the README.
    """
    print('Clearing old tags from README ...')

    with open('README.md', 'r+') as readme:
        lines = readme.read().splitlines()

        anchor = lines.index(README_TAG_ANCHOR) + 1
        next_blank_line = lines.index('', anchor)
        lines = lines[:anchor] + lines[next_blank_line:]

        readme.seek(0)
        readme.truncate()
        readme.write('\n'.join(lines) + '\n')


def remove_old_versions_from_tests():
    """
    Remove all version ENV values from the test setup.
    """
    print('Clearing old test setup from CI config ...')

    with open('.travis.yml', 'r+') as file:
        lines = file.read().splitlines()

        anchor = lines.index(TESTS_CONTEXT_ANCHOR) + 1
        next_blank_line = lines.index('', anchor)
        lines = lines[:anchor] + lines[next_blank_line:]

        file.seek(0)
        file.truncate()
        file.write('\n'.join(lines) + '\n')


def add_tag_badge_to_readme(ver):
    """
    Add links of supported tags to the README.
    """
    print(f"Updating README: tag {ver} ...")

    dockerfile_badge = f"https://img.shields.io/badge/{ver}-blue.svg" \
                       "?colorA=22313f&colorB=4a637b&logo=docker"
    dockerfile_url = f"https://github.com/{GIT_REPO}/blob/master/{ver}/Dockerfile"
    sizelayers_badge = "https://images.microbadger.com/badges/image/" \
                       f"{DOCKER_IMAGE}:{ver}.svg"
    sizelayers_url = f"https://microbadger.com/images/{DOCKER_IMAGE}:{ver}"
    rubygem_badge = f"https://img.shields.io/badge/Gem-{ver}-red.svg" \
                    "?colorA=ff919f&colorB=9a9b9c&logo=ruby"
    rubygem_url = f"https://rubygems.org/gems/modulesync/versions/{ver}"
    tag_lines = [
        f"- [![{ver}](",
        f"  {dockerfile_badge})](",
        f"  {dockerfile_url}) [![size/layers](",
        f"  {sizelayers_badge})](",
        f"  {sizelayers_url}) [![based on](",
        f"  {rubygem_badge})](",
        f"  {rubygem_url})",
    ]

    with open('README.md', 'r+') as file:
        lines = file.read().splitlines()

        anchor = lines.index(README_TAG_ANCHOR) + 1
        lines = lines[:anchor] + tag_lines + lines[anchor:]

        file.seek(0)
        file.truncate()
        file.write('\n'.join(lines) + '\n')


def add_version_to_tests(ver):
    """
    Ensure all versions of the image are built on Travis CI.
    """
    print(f"Updating CI config: test build for {ver} ...")

    context_line = f"{TESTS_CONTEXT_NEEDLE}{ver}"

    with open('.travis.yml', 'r+') as file:
        lines = file.read().splitlines()

        anchor = lines.index(TESTS_CONTEXT_ANCHOR) + 1
        lines = lines[:anchor] + [context_line] + lines[anchor:]

        file.seek(0)
        file.truncate()
        file.write('\n'.join(lines) + '\n')


def main():
    """
    Take the main Dockerfile as a template and create Dockerfiles in
    subdirectories (with ModuleSync version numbers), replacing the 'bundle
    install' by Ruby Gem installs. Also update the README file.
    """
    remove_old_badges_from_readme()
    remove_old_versions_from_tests()

    for version in VERSIONS:
        create_dockerfile(version)
        add_tag_badge_to_readme(version)
        add_version_to_tests(version)

    print("Done. Put the changes under version control now, "
          "and update your Docker image configuration at "
          f"https://cloud.docker.com/u/{DOCKERHUB_USER}/repository/docker/"
          f"{DOCKER_IMAGE}/hubbuilds. Thank you!")


if __name__ == '__main__':
    main()
