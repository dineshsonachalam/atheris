#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$DIR"

sudo docker build -t atheris-builder ./
sudo docker run -it --env ATHERIS_VERSION="$ATHERIS_VERSION" --mount type=bind,source=$PWD/../,target=/atheris atheris-builder
