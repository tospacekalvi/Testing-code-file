from machine import Pin, reset
from time import sleep
from network import WLAN

SSID = "ToSpace"
PASSWORD = "ToSpace@123"

R1 = Pin(14, Pin.OUT)
R2 = Pin(13, Pin.OUT)
L1 = Pin(27, Pin.OUT)
L2 = Pin(16, Pin.OUT)
B1 = Pin(15, Pin.OUT)

def IoT_Check():
    R1.on()
    sleep(1)
    R1.off()
    
    R2.on()
    sleep(1)
    R2.off()
    
    L1.on()
    sleep(1)
    L1.off()
    
    L2.on()
    sleep(1)
    L2.off()
    
    B1.on()
    sleep(1)
    B1.off()
    
    

def connect_wifi():
    print("Connecting to WiFi...")
    wifi = WLAN()
    wifi.active(True)
    wifi.connect(SSID, PASSWORD)

    attempts = 0
    while not wifi.isconnected():
        print("...trying", attempts + 1)
        sleep(1)
        attempts += 1
        if attempts > 10:
            print("WiFi not connected! Check credentials or signal.")
            return False

    print("WiFi connected! IP:", wifi.ifconfig()[0])
    return True

def main():
    if connect_wifi():
        while True:
            IoT_Check()
    else:
        print("Not working")
        sleep(3)

main()
