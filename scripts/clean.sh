#!/bin/bash
set -e
set -x
if [ -d 'dist' ] ; then
    rm -r dist
fi
if [ -d 'site' ] ; then
    rm -r site
fi

find . | grep -E "(/__pycache__$|\.pyc$|\.pyo$)" | xargs rm -rf
