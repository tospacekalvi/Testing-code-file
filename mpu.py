from machine import I2C, Pin
from mpu6050 import MPU6050
from time import sleep

i2c = I2C(0, scl=Pin(1), sda=Pin(0))  # Adjust pins for your board
mpu = MPU6050(i2c)
led = Pin(25, Pin.OUT)

while True:
    # Blink LED to show sensor reading cycle
    led.on()
    sleep(0.2)
    led.off()

    # Get raw values
    accel = mpu.get_accel()
    gyro = mpu.get_gyro()
    temp = mpu.get_temp()

    # Print raw numbers
    print("\n-----------------------------")
    print("📊 Accelerometer (g): X={:.2f}, Y={:.2f}, Z={:.2f}".format(accel['x'], accel['y'], accel['z']))
    print("🌀 Gyroscope (°/s):   X={:.2f}, Y={:.2f}, Z={:.2f}".format(gyro['x'], gyro['y'], gyro['z']))
    print("🌡 Temperature:       {:.2f} °C".format(temp))
    print("-----------------------------\n")

    sleep(1)   # delay for readability
