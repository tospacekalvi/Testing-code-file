from machine import UART, Pin
import time

# UART0 → TX=GP0, RX=GP1
uart = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1))

def read_gps():
    while True:
        if uart.any():
            line = uart.readline()
            try:
                print(line.decode('utf-8').strip())
            except:
                pass
        time.sleep(0.1)

read_gps()
