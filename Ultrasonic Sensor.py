from machine import Pin, time_pulse_us
import time

# Define pins
trigger = Pin(5, Pin.OUT)   # Trigger pin
echo = Pin(18, Pin.IN)      # Echo pin

def get_distance():
    # Send 10µs pulse
    trigger.value(0)
    time.sleep_us(2)
    trigger.value(1)
    time.sleep_us(10)
    trigger.value(0)
    
    # Measure echo pulse
    duration = time_pulse_us(echo, 1, 30000)  # timeout 30ms
    distance = (duration / 2) / 29.1          # convert to cm
    return distance

while True:
    dist = get_distance()
    print("Distance:", dist, "cm")
    time.sleep(1)
