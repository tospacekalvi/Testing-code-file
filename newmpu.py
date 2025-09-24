# this for the 8 channel only later I will updat it as a 16 to 64 channel QC model

from machine import Pin, I2C
from mpu6050 import MPU6050
import time

# Setup I2C
i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=400000)

PCA9548A_ADDR = 0x70

def select_channel(ch):
    """Select I2C channel on PCA9548A"""
    i2c.writeto(PCA9548A_ADDR, bytes([1 << ch]))
    time.sleep(1.5)

def test_mpu(ch):
    """Test MPU6050 on given channel"""
    try:
        select_channel(ch)
        mpu = MPU6050(i2c)

        accel = mpu.get_accel()
        gyro = mpu.get_gyro()
        temp = mpu.get_temp()

        # Basic range checks
        if -2 < accel['x'] < 2 and -2 < accel['y'] < 2 and 0 < accel['z'] < 2.5 and -100 < temp < 100:
            print(f"[PASS] Channel {ch}: Accel={accel}, Gyro={gyro}, Temp={temp:.2f}C")
        else:
            print(f"[FAIL] Channel {ch}: Out of range values")
    except Exception as e:
        print(f"[FAIL] Channel {ch}: {e}")

# ---- Run QC ----
print("Starting MPU6050 QC Test...\n")

for ch in range(8):  # PCA9548A has 8 channels (0-7)
    test_mpu(ch)

print("\nQC Test Completed ✅")

