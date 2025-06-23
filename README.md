# Raspberry Pi Specialization on Coursera
Course taken for technical practice and fun.

## Beginning Custom Projects with Raspberry Pi
The first course in the specialization.

In module 1 the key thing I found interesting was using the web to remotely control an LED connected to the Raspberry Pi. The module began by controlling an LED hooked up to pin 11 (GPIO 17) on the pi using the gpiozero python library used to control Rpi gpio pins. With gpiozero library we create an object of the class LED and pass in the gpio number to it. Using the LED instance we call on() and off() functions to turn that pin on and off.

Once we were able to control the LED we added the web layer on top to "request" to turn the LED on and off from another computer on the network. We created a python script that runs on the Rpi that starts a very basic http server that listens for requests on port 8080. We use a REST API convention to request led on and off from a remote machine. To request to turn on led we go to the url http://rpi-IP:8080/led/on and our python script will listen for this request and check if the request ends with /led/on and then call the gpiozero library to turn on the LED. To request to turn off we end the url request in /led/off.
