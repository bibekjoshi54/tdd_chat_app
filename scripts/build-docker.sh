#!/bin/bash

set -e
set -x


HOST_UID=$(id -u) HOST_GID=$(id -g) docker build --build-arg UID=$HOST_UID --build-arg GID=$HOST_GID -t tdd_chat_app_app:latest .

