# Need seperate file for screen module
# Moisture and Temp/Humidity readings for my plants

from machine import ADC, Pin, I2C
import utime as time
from dht11 import DHT11, InvalidChecksum

# GND = 3, 8, 13, 18, 23, 28, 33, 38
# 3V3 Out = 36
# DHT11 sensor = GPIO28/Pin 34

soil1 = ADC(Pin(26))    # Pin 31 on Pico
soil2 = ADC(Pin(27))    # Pin 32 on Pico

dht11_pin = Pin(28, Pin.OUT, Pin.PULL_DOWN)    # Pin 34 on Pico
dht = DHT11(dht11_pin)

# Calibration values
min_moisture = 0
max_moisture = 65535

readDelay = 0.5

while True:
    
    time.sleep(5)
    
    t = (dht.temperature)
    h = (dht.humidity)
    moisture1 = (max_moisture - soil1.read_u16()) * 100 / (max_moisture - min_moisture)
    moisture2 = (max_moisture - soil2.read_u16()) * 100 / (max_moisture - min_moisture)
    
    # Print values
    print("Moisture 1: " + "%.2f" % moisture1 + "% (adc: "+str(soil1.read_u16())+")")
    print("Moisture 2: " + "%.2f" % moisture2 + "% (adc: "+str(soil2.read_u16())+")")
    print("Temp: {}".format(dht.temperature))
    print("Humidity: {}".format(dht.humidity))
