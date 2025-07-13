# To run this application you need flask installed which can be done with pip3 install flask
# To run it do the following in a terminal: FLASK_APP=api.py flask run
# Flask requires us to set the FLASK_APP env variable to know the program to run
# flask run is the command we run so that the flask framework starts a server for us
# flask does a lot of the heavy lifting and abstracts the server infrastructure
# we define a "route" so that the flask server knows what to call when it receives a certain request

from flask import Flask

# __name__ will end up being the name of the file in this case api.py
app = Flask(__name__)

# they call the @app.route a decorator that "decorates" the function led_on()
# the decorator essentially defines the api endpoint similar to the previous http server application I wrote in earler module.
# So now when the url ends in /led/on then the led_on function will get called.
@app.route('/led/on')
def led_on():
    return "Turning on the LED"
