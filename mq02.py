from machine import Pin, ADC
from time import sleep


mq02 = ADC(Pin(26))
# mq02.atten(ADC.ATTN_11DB)   # Range: 0 - 3.3V

while True:
    value = mq02.read()   
#     voltage = (value / 4095) * 3.3  # Convert to volts
    
    print("Raw Value:", value)
    
    sleep(1)
