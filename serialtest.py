import serial, sys, time
import math as mth
import numpy as np

'''
def getData(serialport):
    return serialport.readline()
'''

port1 = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)

time.sleep(2)

while True:

    data = np.random.randint(0, 2)
    print(data)
    #port1.write(bytes(data))
    port1.write(bytes(data))
    time.sleep(10)
