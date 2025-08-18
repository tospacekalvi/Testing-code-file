from machine import Pin, I2C
from bmp280 import BMP280
import time

i2c = I2C(0, scl=Pin(1), sda=Pin(0))  # Adjust pins as needed
bmp = BMP280(i2c)

while True:
    temp, pressure = bmp.read_compensated_data()
    print("Temperature:", temp, "°C")
    print("Pressure:", pressure, "hPa")
    time.sleep(2)
