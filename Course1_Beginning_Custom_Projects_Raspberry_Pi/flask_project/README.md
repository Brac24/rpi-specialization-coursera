There is a python virtual environment in this directory.
virtual environment or venv is kind of a like a container where you can install your own packages so as to not contaminate the host machine if we are just testing things out.

Start the environment by running from within this directory: source my_env/bin/activate
api.py is a flask program which can be run with: FLASK_APP=api.py flask run
Then in a browser type in the url: 127.0.0.1:5000/led/on
You should see some text appear in the browser after

Get out of the venv by calling deactivate from within the venv.


