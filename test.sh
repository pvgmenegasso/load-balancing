#!/bin/bash

# Activate python venv and print version
echo "activating python venv"
source .venv/bin/activate
echo "python version: "
which python

# Install required packages
echo "installing packages"
pip3 install -r requirements.txt

# Start tests
export DEBUG="True"
echo "launching tests..."
pytest 


