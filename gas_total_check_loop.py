from machine import ADC, Pin
import time

# Connect MQ sensor AOUT to GP26 (ADC0)
gas_sensor = ADC(Pin(26))

# Strict voltage threshold to confirm sensor is properly inserted
SENSOR_INSERT_THRESHOLD = 1.0  # in volts
GAS_DETECTION_THRESHOLD = 2.0  # in volts

def read_sensor():
    raw_value = gas_sensor.read_u16()
    voltage = (raw_value / 65535) * 3.3
    return raw_value, voltage

while True:
    raw, volt = read_sensor()

    # Check if sensor is properly inserted
    if volt > SENSOR_INSERT_THRESHOLD:
        print("Sensor Detected ✅")
        print("Raw Value:", raw, "| Voltage:", round(volt, 2), "V")

        # Gas detection logic
        if volt > GAS_DETECTION_THRESHOLD:
            print("⚠️ Gas Detected!")
        else:
            print("✅ Safe Air")
    else:
        print("❌ Sensor Not Inserted Properly or No Signal")

    time.sleep(0.5)
