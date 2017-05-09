Gardenbot 2.0
================

The Gardenbot is a physical apparatus and a set of scripts that lets you water your plants remotely by tweeting at them. 


### Dependencies:

Python 3.5.X, PySerial, NumPy, Tweepy, Arduino IDE 

### The Circuit:

Before you run any of the scripts in this repository, make sure you set up the circuit shown below.

![circuit](http://i.imgur.com/Ei5pCk3.png?1)

This circuit lets you control a 12V pump motor with your Arduino's analog outputs. By sending a 5V signal from your Arduino 
to the base pin of your transistor, you let a high voltage from an external power supply flow through the transistor and into
the motor. The PN-diode running in parallel with the motor is there to prevent the
motor from inducing a large current -- and possibly damaging your components -- when it slows down.
