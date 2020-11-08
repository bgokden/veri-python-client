#!/usr/bin/env bash

rm -rf ./dist/*
pip3 install twine
python3 setup.py sdist bdist_wheel
twine upload dist/*

