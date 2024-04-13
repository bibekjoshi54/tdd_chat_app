#!/bin/bash

set -o errexit


# Change directory to the project root directory.
cd "$(dirname "$0")/.."

# Install the dependencies into the mypy env.
# Note that this can take seconds to run.
# In my case, I need to use a custom index URL.
# Avoid pip spending time quietly retrying since
# likely cause of failure is lack of VPN connection.
#pip install --editable . \
#  --index-url https://custom-index-url.com/simple \
#  --retries 1 \
#  --no-input \
#  --quiet

# Run on all files,
# ignoring the paths passed to this script,
# so as not to miss type errors.
# My repo makes use of namespace packages.
# Use the namespace-packages flag
# and specify the package to run on explicitly.
# Note that we do not use --ignore-missing-imports,
# as this can give us false confidence in our results.
mypy --package tdd_chat_app --namespace-packages
