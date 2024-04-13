#!/usr/bin/env bash

set -e
set -x

PREFIX_CMD="poetry run"


${PREFIX_CMD} mypy tdd_chat_app
./scripts/format.sh
