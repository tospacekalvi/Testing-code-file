# bmp280.py

import time
from micropython import const

BMP280_I2C_ADDR = const(0x76)

class BMP280:
    def __init__(self, i2c, addr=BMP280_I2C_ADDR):
        self.i2c = i2c
        self.addr = addr
        self._load_calibration()
        self._configure()

    def _read16(self, reg):
        data = self.i2c.readfrom_mem(self.addr, reg, 2)
        return data[0] | (data[1] << 8)

    def _readS16(self, reg):
        result = self._read16(reg)
        if result > 32767:
            result -= 65536
        return result

    def _read24(self, reg):
        data = self.i2c.readfrom_mem(self.addr, reg, 3)
        return data[0] << 16 | data[1] << 8 | data[2]

    def _load_calibration(self):
        self.dig_T1 = self._read16(0x88)
        self.dig_T2 = self._readS16(0x8A)
        self.dig_T3 = self._readS16(0x8C)
        self.dig_P1 = self._read16(0x8E)
        self.dig_P2 = self._readS16(0x90)
        self.dig_P3 = self._readS16(0x92)
        self.dig_P4 = self._readS16(0x94)
        self.dig_P5 = self._readS16(0x96)
        self.dig_P6 = self._readS16(0x98)
        self.dig_P7 = self._readS16(0x9A)
        self.dig_P8 = self._readS16(0x9C)
        self.dig_P9 = self._readS16(0x9E)

    def _configure(self):
        self.i2c.writeto_mem(self.addr, 0xF4, b'\x27')  # ctrl_meas
        self.i2c.writeto_mem(self.addr, 0xF5, b'\xA0')  # config

    def read_raw_temp(self):
        return self._read24(0xFA) >> 4

    def read_raw_pressure(self):
        return self._read24(0xF7) >> 4

    def compensate_temp(self, adc_T):
        var1 = (((adc_T >> 3) - (self.dig_T1 << 1)) * self.dig_T2) >> 11
        var2 = (((((adc_T >> 4) - self.dig_T1) * ((adc_T >> 4) - self.dig_T1)) >> 12) * self.dig_T3) >> 14
        self.t_fine = var1 + var2
        T = (self.t_fine * 5 + 128) >> 8
        return T / 100

    def compensate_pressure(self, adc_P):
        var1 = self.t_fine - 128000
        var2 = var1 * var1 * self.dig_P6
        var2 = var2 + ((var1 * self.dig_P5) << 17)
        var2 = var2 + (self.dig_P4 << 35)
        var1 = ((var1 * var1 * self.dig_P3) >> 8) + ((var1 * self.dig_P2) << 12)
        var1 = ((1 << 47) + var1) * self.dig_P1 >> 33
        if var1 == 0:
            return 0
        p = 1048576 - adc_P
        p = ((p << 31) - var2) * 3125 // var1
        var1 = self.dig_P9 * (p >> 13) * (p >> 13) >> 25
        var2 = self.dig_P8 * p >> 19
        p = ((p + var1 + var2) >> 8) + (self.dig_P7 << 4)
        return p / 25600

    def read_compensated_data(self):
        adc_T = self.read_raw_temp()
        adc_P = self.read_raw_pressure()
        temp = self.compensate_temp(adc_T)
        pressure = self.compensate_pressure(adc_P)
        return temp, pressure
