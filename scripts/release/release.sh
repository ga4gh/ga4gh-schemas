#!/bin/sh

# do we have enough arguments?
if [ $# < 3 ]; then
    echo "Usage:"
    echo
    echo "./release.sh <release version> <development version>"
    exit 1
fi

# pick arguments
release=$1
devel=$2

commit=$(git log --pretty=format:"%H" | head -n 1)
echo "releasing from ${commit} on branch ${branch}"

git push origin ${branch}

mvn --batch-mode \
  -P release \
  -Dresume=false \
  -Dtag=ga4gh-schemas-${release} \
  -DreleaseVersion=${release} \
  -DdevelopmentVersion=${devel} \
  release:clean \
  release:prepare \
  release:perform

if [ $? != 0 ]; then
  echo "Releasing failed."
  exit 1
fi
