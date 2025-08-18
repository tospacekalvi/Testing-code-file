from machine import Pin
from time import sleep

m1 = Pin(18, Pin.OUT)   
m2 = Pin(19, Pin.OUT)  
m3 = Pin(22, Pin.OUT) 
m4 = Pin(23, Pin.OUT)  

def forward():
    m1.on()
    m2.off()
    m3.on()
    m4.off()

def backward():
    m1.off()
    m2.on()
    m3.off()
    m4.on()  

while True:
    forward()
    sleep(5)
    backward()
    sleep(3)

    
     
    