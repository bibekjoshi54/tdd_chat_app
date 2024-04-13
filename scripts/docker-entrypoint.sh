#!/bin/bash
set -e
set -x
usage() {
    echo "Usage: $0 [-c] [-e] [-i]" 1>&2
    echo "Options:" 1>&2
    echo "  -c  Execute coverage-report.sh" 1>&2
    exit 1
}

# Run the setup script to install additional libraries and clean the enviroment before doing dev stuff on docker
#
bash ./scripts/setup.sh
# Parse options
while getopts ":cei" opt; do
    case ${opt} in
        c)
          ./scripts/coverage-report.sh
            ;;
        *)
            usage
            ;;
    esac
done
shift $((OPTIND -1))
