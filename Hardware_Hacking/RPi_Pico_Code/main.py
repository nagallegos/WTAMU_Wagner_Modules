# machine is part of MicroPython for the RPi Pico
from machine import Pin,I2C
from time import sleep
import random

# Define I2C pins
led = Pin(25,Pin.OUT)
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

def startup_sig():
    itter = 3
    count = 0
    while(count < itter):
        strobe(3)
        sleep(.1)
        strobe(3)
        sleep(.3)
        count = count + 1

def run():
    while(True):
        print("\n")
        devices = i2c.scan()
        if(len(devices) == 0):
            print("No devices found.\nExiting...")
            return
        for device in devices:
            print("Device found at:  DEC:",device,"| HEX:",hex(device))
        print("\n")

        for device in devices:
            strobe(10)
            raw_msg = i2c.readfrom(device,50)
            #raw_num = i2c.readfrom(device,10)
            msg = (str(raw_msg).partition("b'")[2]).partition("\\xff")[0]
            print(str(msg))
            sleep(0.5)
        wait_time = random.randint(5,10)
        sleep(wait_time)

def main():
    startup_sig()
    try:
        run()
    except KeyboardInterrupt:
        print("Ctrl-C pressed: Ending program.\n")
        
if __name__ == "__main__":
    main()