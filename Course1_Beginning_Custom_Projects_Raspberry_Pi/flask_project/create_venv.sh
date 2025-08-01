#!/bin/bash

# creates a python virtual environment.
# this script should only be ran once.
# if you already have a venv directory then no need to run this script

# the second venv is the name of the virtual environment. I could have said my_venv but naming it venv is convention
# running the command below will create a directory called venv as well
# to run the virtual environment you need to run: source venv/bin/activate
# to quit the venv run: decactivate from within the venv
python3 -m venv venv
