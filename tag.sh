#!/bin/sh

tag="v$(awk -F'"' '/ENV MODULESYNC_VERSION/{ print $2 }' Dockerfile)"
git tag -s "${tag}" -m "Release ${tag}"

echo "---> Tagged as ${tag}"
echo "     Don't forget to push the tag: git push --follow-tags"
