Gardenbot 2.0
================

The Gardenbot is a physical apparatus and a set of scripts that lets you water your plants remotely by tweeting at them. 


### Dependencies:

Python 3.5.X, PySerial, NumPy, Tweepy, Arduino IDE 

### The Circuit:

Before you run any of the scripts in this repository, make sure you set up the circuit shown below.

![circuit](http://i.imgur.com/Ei5pCk3.png?1)

This circuit lets you spin up a 12V pump motor with your Arduino's analog outputs. By sending a 5V signal from your Arduino 
to the base pin of a bipolar-junction transistor, you let a high voltage from an external power supply flow
through the transistor and into the motor. The diode running in parallel with the motor is there to prevent the
motor from inducing a large current -- and possibly damaging your components -- when it slows down, and the resistor in series 
with the base pin to protect the Arduino from electrical damage.

### The Scripts:

Assuming you've installed all the dependencies listed above, you should be ready to test out the repository's scripts.
It's important to note that Arduino and Python don't tend to get along too well. First, run _arduino_main.ino_, and
make sure you don't get any run-time errors. If you do, try resetting your Arduino, or if you're using a UNIX-like system,
using the *fuser* utility with the *-k* modifier to kill processes associated with the serial port your Arduino is connected to.

Next, assuming your Arduino code is running fine (you can test this by sending a '1' into the serial monitor. An onboard LED should turn on, and a voltage should be applied to the A0 pin for a few seconds), run *serialtest.py*. If the Arduino reacts to
Python's serial data input, you're in the clear. You can now run *tweepy_main.py*, and tweet at your plant.

