# Need seperate file for screen module
# Moisture and Temp/Humidity readings for my plants

from machine import ADC, Pin
import utime

soil1 = ADC(Pin(26))
soil2 = ADC(Pin())

# Calibration values
min_moisture = 0
max_moisture = 65535

readDelay = 0.5

while True:
    
    moisture1 = (max_moisture - soil1.read_u16()) * 100 / (max_moisture - min_moisture)
    moisture2 = (max_moisture - soil2.read_u16()) * 100 / (max_moisture - min_moisture)
    
    # Print values
    print("Moisture 1: " + "%.2f" % moisture1 + "% (adc: "+str(soil1.read_u16())+")")
    print("Moisture 2: " + "%.2f" % moisture2 + "% (adc: "+str(soil2.read_u16())+")")
    
    # Delay between readings
    utime.sleep(readDelay)
