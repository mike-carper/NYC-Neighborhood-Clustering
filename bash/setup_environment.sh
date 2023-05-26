#!/bin/bash
#
# Dev script to compile python packages from a requirements.in file to a requirements.txt file.
set -e
RELATIVE_SCRIPTPATH=$0

# creating virtual environment
# TODO check if it already exists first

# activate virtual environment
echo "~~~ Activating virtual environment ~~~"
source .venv/bin/activate
which python
python --version

# Update and install packages used to compile requirements
echo "~~~ Installing build packages ~~~"
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade pip-tools wheel

# Delete existing requirements file to ensure full dependency resolution
echo "~~~ Deleting requirements.txt ~~~"
rm -rf requirements.txt

# Compile python package requirements
echo "~~~ Compiling requirements.txt ~~~"
CUSTOM_COMPILE_COMMAND="${RELATIVE_SCRIPTPATH}" python3 -m piptools compile --output-file=requirements.txt requirements.in

# install python packages
echo "~~~ Installing python packages via pip-sync ~~~"
pip-sync requirements.txt
