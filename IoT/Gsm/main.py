from machine import UART, Pin
import time

# UART0: TX=GPIO0, RX=GPIO1
uart = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1))

def send_at_command(cmd, delay=1):
    uart.write((cmd + '\r\n').encode())
    time.sleep(delay)
    if uart.any():
        response = uart.read().decode()
        print("Response:", response)
    else:
        print("No response")

# Test SIM800L
print("Checking SIM800L...")
send_at_command("AT")               # Basic test
send_at_command("AT+CSQ")           # Signal quality
send_at_command("AT+CCID")          # SIM card info
send_at_command("AT+CREG?")         # Network registration

