# machine is part of MicroPython for the RPi Pico
from machine import Pin,I2C
from time import sleep
import random

# Define I2C pins
led = Pin("LED",Pin.OUT)
i2c = I2C(0, scl=Pin(17), sda=Pin(16), freq=400000)
random.seed(123)

def strobe(n):
    count = 0
    led.value(0)
    while(count < n):
        led.toggle()
        sleep(.025)
        led.toggle()
        sleep(.025)
        count = count + 1

while(True):
    devices = i2c.scan()
    for device in devices:
        print("Device at:\t", hex(device))
    print("\n")

    for device in devices:
        strobe(10)
        raw_msg = i2c.readfrom(device,50)
        msg = (str(raw_msg).partition("b'")[2]).partition("\\xff")[0]
        print(msg)
        sleep(0.5)
    wait_time = random.randint(5,10)
    sleep(wait_time)