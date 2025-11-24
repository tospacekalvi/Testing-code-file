from machine import Pin
from machine import Pin, reset
from time import sleep
from network import WLAN

m1 = Pin(18, Pin.OUT)   
m2 = Pin(19, Pin.OUT)  
m3 = Pin(22, Pin.OUT) 
SSID = "ToSpace"
PASSWORD = "ToSpace@123"

m1 = Pin(18, Pin.OUT)
m2 = Pin(19, Pin.OUT)
m3 = Pin(22, Pin.OUT)
m4 = Pin(23, Pin.OUT)
led = Pin(2,Pin.OUT)
led1= Pin(16,Pin.OUT)
led2= Pin(32,Pin.OUT)
led3= Pin(27,Pin.OUT)

led = Pin(2, Pin.OUT) # for the indication purpose
led1 = Pin(16, Pin.OUT)
led2 = Pin(32, Pin.OUT)
led3 = Pin(27, Pin.OUT)

def forward():
    m1.on()
    m2.off()
    m3.on()
    m4.off()
    print("Motor is moving forward")
    print("Motor moving forward")

def backward():
    m1.off()
    m2.on()
    m3.off()
    m4.on()
    print("Motor is moving backward")
    
    print("Motor moving backward")

def stop():
    m1.off()
    m2.off()
    m3.off()
    m4.off()
    print("Bot stopped")

def blink():
    led.on()
    led2.on()
@@ -35,28 +47,50 @@ def blink():
    sleep(1)
    led1.off()
    led3.off()
    print("Blinking")
def stop():
    m1.off()
    m2.off()
    m3.off()
    m4.off()
    print("bot has been stopped")
    print("--------Blinking-------")


while True:
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

    blink()
#     stop()
#     sleep(3)
    forward()
#     sleep(3)
#     stop()
#     sleep(3)
#     backward()
    print("✅ WiFi connected! IP:", wifi.ifconfig()[0])
    return True

def main():
    if connect_wifi():
        print("Starting robot sequence...\n")
        while True:
            blink()
            forward()
            sleep(2)
            stop()
            sleep(1)
            backward()
            sleep(2)
            stop()
            sleep(1)
    else:
        print("WiFi connection failed — bot will not move.")
        stop()
        for _ in range(5):
            led.on()
            sleep(0.3)
            led.off()
            sleep(0.3)
        #reset() 

main()