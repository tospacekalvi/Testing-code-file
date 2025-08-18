# mpu6050.py

import math

class MPU6050:
    def __init__(self, i2c, addr=0x68):
        self.i2c = i2c
        self.addr = addr
        # Wake up MPU6050 (it's in sleep mode by default)
        self.i2c.writeto_mem(self.addr, 0x6B, b'\x00')

    def read_raw_data(self, reg):
        data = self.i2c.readfrom_mem(self.addr, reg, 2)
        value = int.from_bytes(data, 'big')
        if value > 32767:
            value -= 65536
        return value

    def get_accel(self):
        ax = self.read_raw_data(0x3B) / 16384.0
        ay = self.read_raw_data(0x3D) / 16384.0
        az = self.read_raw_data(0x3F) / 16384.0
        return {'x': ax, 'y': ay, 'z': az}

    def get_gyro(self):
        gx = self.read_raw_data(0x43) / 131.0
        gy = self.read_raw_data(0x45) / 131.0
        gz = self.read_raw_data(0x47) / 131.0
        return {'x': gx, 'y': gy, 'z': gz}

    def get_temp(self):
        temp_row = self.read_raw_data(0x41)
        return (temp_row / 340.0) + 36.53
