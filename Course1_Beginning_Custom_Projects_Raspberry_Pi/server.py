# This program is meant to be run on an Rpi 4B
# The program will start an http server which listens on port 8080
# When the server receives a request on the url /led/on it will turn on the led connected to the rpi
# When the server receives a request on the url /led/off  it will turn off the led connected to the rpi

# For example, while this program is started on the Rpi I use a different machine like my PC that is on the same network and on that
# machine I can type the following in a browser url: http://192.168.86.191:8080/led/on and when I press Enter the Rpi should turn on the led.
# In this example the Rpi IP address is 192.168.86.191

from http.server import SimpleHTTPRequestHandler, HTTPServer

from gpiozero import LED

# create the led object to control the led connected to the rpi
red = LED(17)

# Defining a MyHandler class that implements the SimpleHTTPRequestHandler interface
# We need to implement that interface in order to have the http server invoke our led control logic on an http request.
class MyHandler(SimpleHTTPRequestHandler):
    
    # When a GET request is received on the http server this do_GET function runs
    # and will check if the request url ended with either /led/on or /led/off
    # and perform the appropriate action.
    def do_GET(self):
        if self.path == '/led/on':
            print("request received for led on")
            red.on()
        elif self.path == '/led/off':
            print("request received for led off")
            red.off()


        self.send_response(200) # respond back to the client that the request was handled
        self.end_headers()


# create the http server object and define it to listen on port 8080 and to use methods defined on the MyHandler class
# The MyHandler implements the SimpleHTTPRequestHandler interface which defines a do_GET method that is invoked on a GET request from a client machine.
httpd = HTTPServer(("", 8080), MyHandler)

# Start the server
httpd.serve_forever()
