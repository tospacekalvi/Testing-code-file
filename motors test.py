from machine import Pin
from time import sleep

m1 = Pin(18, Pin.OUT)   
m2 = Pin(19, Pin.OUT)  
m3 = Pin(22, Pin.OUT) 
m4 = Pin(23, Pin.OUT)
led = Pin(2,Pin.OUT)
led1= Pin(16,Pin.OUT)
led2= Pin(32,Pin.OUT)
led3= Pin(27,Pin.OUT)

def forward():
    m1.on()
    m2.off()
    m3.on()
    m4.off()
    print("Motor is moving forward")

def backward():
    m1.off()
    m2.on()
    m3.off()
    m4.on()
    print("Motor is moving backward")
    
def blink():
    led.on()
    led2.on()
    sleep(1)
    led.off()
    led2.off()
    led1.on()
    led3.on()
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


while True:
    
    blink()
#     stop()
#     sleep(3)
    forward()
#     sleep(3)
#     stop()
#     sleep(3)
#     backward()


    
     
    

