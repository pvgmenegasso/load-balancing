#!/bin/bash

# Activate python venv and print version
echo "activating python venv"
source .venv/bin/activate

# Install required packages
echo "installing packages"
cd load_balancing
pip3 install -r requirements.txt

# Start tests
export DEBUG="True"
echo "launching tests..."

pytest 


