#!/usr/bin/env bash
#
# Creates and updates version-based Dockerfile folders.
#

VERSIONS="0.9.0"

for ver in ${VERSIONS}; do
  echo "Updating Dockerfile for version ${ver} ..."
  mkdir -pv "$ver"
  cp -fv Dockerfile "$ver/"
  sed -i "$ver/Dockerfile" \
      -e "/COPY Gemfile Gemfile/d" \
      -e "s/RUN bundle install/RUN gem install modulesync --version ${ver}/"
done

echo "Done. Put the changes under version control now, and update your Docker image configuration"
echo "at https://hub.docker.com/r/vshn/modulesync/~/settings/automated-builds/. Thank you!"
