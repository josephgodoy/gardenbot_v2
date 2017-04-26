## serialtest.py ##
## joseph godoy  ##
'''
This script is a simple test to see whether or not your Arduino
is working with pySerial. If you're using the .ino file I included
with the repository, you should be getting two-second-long
blinks in the integrated board LED when a '1' is printed to the
command line, and nothing when a '0' is printed to the command line.

If your test isn't working, try resetting the board or re-uploading.
It often helps to manually enter values into the serial monitor before
running the script.
'''

import serial, sys, time
import numpy as np

port1 = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
time.sleep(2)

while True:

    data = np.random.randint(0, 2)
    print(data)
    port1.write(bytes(data))
    time.sleep(10)
