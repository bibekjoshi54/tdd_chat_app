#!/bin/sh -e
set -x

PREFIX_CMD="poetry run"

${PREFIX_CMD} ruff tdd_chat_app tests scripts --fix
${PREFIX_CMD} ruff format tdd_chat_app tests scripts
