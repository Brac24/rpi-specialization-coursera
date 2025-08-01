# Raspberry Pi Specialization on Coursera
Course taken for technical practice and fun.

## Beginning Custom Projects with Raspberry Pi
The first course in the specialization.

In module 2 the key thing I found interesting was using the web to remotely control an LED connected to the Raspberry Pi. The module began by controlling an LED hooked up to pin 11 (GPIO 17) on the pi using the gpiozero python library used to control Rpi gpio pins. With gpiozero library we create an object of the class LED and pass in the gpio number to it. Using the LED instance we call on() and off() functions to turn that pin on and off.

Once we were able to control the LED we added the web layer on top to "request" to turn the LED on and off from another computer on the network. We created a python script that runs on the Rpi that starts a very basic http server that listens for requests on port 8080. We use a REST API convention to request led on and off from a remote machine. To request to turn on led we go to the url http://rpi-IP:8080/led/on and our python script will listen for this request and check if the request ends with /led/on and then call the gpiozero library to turn on the LED. To request to turn off we end the url request in /led/off.


Module 3 mainly talked about communication protocols such as I2C and SPI and about types of motors and brief intro on how to control them. Did not feel the need to note too much since I've already had some background on these communication protocols as well as have worked with stepper motors, servos, and brushless dc motors so even though I am not an expert I think it would be easy enough for me to look it up when this is needed.


In module 4 I found that a important piece was in the lecture explaining how ssh authentication works. 
With his explanation this concept made it easier for me to grasp and understand. 
What clicked for me was the notion of there being an encrypt key and a decrypt key on the client machine and the server machine having the encrypt key. 
The encrypt key was used to encrypt information that would flow through a network between client and server. 
The decrypt key is used to decrypt the information that was encrypted with the encrypt key. 
The decrypt key and encrypt are dependent on each and can only be used in their specified way (i.e. encrypt key cannot be used to try to decrypt and vice versa). 
The way ssh authentication worked was that when a client machine (i.e. us the user) would initiate an ssh login to the server (i.e. the raspberry pi) then the server would send a "challenge" message to the client and that message is encrypted using the encrypt key that is on the client machine. 
So after the server sends the challenge message to the client, the server is waiting for a response from the client and the server is expecting to receive back the challenge message but decrypted. 
If the client can respond with the decrypted challenge message then the server knows: "ok this is an authorized user because they knew how to decrypt my encrypted message" and the client is then authenticated and logged in to the server.

In order to use ssh authentication without requiring a password everytime we use ssh-keygen on the client machine. ssh-keygen will generate a public and private key pair. 
We then send the public key to the server (i.e. raspberry pi) but we need to place that in the directory ~/.ssh/authorized_keys. 
If we don't place it in that directory then it won't work. 
Now every time we ssh with our client machine into the raspberry pi the pi will look at the public key (i.e. the encrypt key) and do the challenge message process and authenticate us. 

