from machine import Pin
import time

# IR sensor connected to GPIO 15 (change pin if needed)
ir_sensor = Pin(15, Pin.IN)

while True:
    if ir_sensor.value() == 0:   # Most IR obstacle sensors give 0 when object detected
        print("Sensor is working - Object detected")
    else:
        print("Sensor is not working - No object")
    
    time.sleep(1)   # check every 1 second
