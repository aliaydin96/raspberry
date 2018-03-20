import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

pin1  = 35
pin2 = 37
pin3 = 33
pin4 = 31
pin5 = 29
pin6 = 32
pin7 = 36
pin8 = 38
GPIO.setup(pin1,GPIO.OUT)
GPIO.setup(pin2,GPIO.OUT)
GPIO.setup(pin3,GPIO.OUT)
GPIO.setup(pin4,GPIO.OUT)
GPIO.setup(pin5,GPIO.OUT)
GPIO.setup(pin6,GPIO.OUT)
GPIO.setup(pin7,GPIO.OUT)
GPIO.setup(pin8,GPIO.OUT)

while True:

                GPIO.output(pin1,GPIO.HIGH)
                time.sleep(0.1)
                GPIO.output(pin3,GPIO.HIGH)
                GPIO.output(pin1,GPIO.LOW)
                time.sleep(0.1)
                GPIO.output(pin2,GPIO.HIGH)
                GPIO.output(pin3,GPIO.LOW)
                time.sleep(0.1)
                GPIO.output(pin2,GPIO.LOW)
                GPIO.output(pin4,GPIO.HIGH)
                time.sleep(0.1)
                GPIO.output(pin4,GPIO.LOW)

                GPIO.output(pin5,GPIO.HIGH)
                time.sleep(0.1)
                GPIO.output(pin6,GPIO.HIGH)
                GPIO.output(pin5,GPIO.LOW)
                time.sleep(0.1)
                GPIO.output(pin7,GPIO.HIGH)
                GPIO.output(pin6,GPIO.LOW)
time.sleep(0.1)
                GPIO.output(pin7,GPIO.LOW)
                GPIO.output(pin8,GPIO.HIGH)
                time.sleep(0.1)
                GPIO.output(pin8,GPIO.LOW)


                GPIO.output(pin7,GPIO.HIGH)
                time.sleep(0.1)
                GPIO.output(pin6,GPIO.HIGH)
                GPIO.output(pin7,GPIO.LOW)
                time.sleep(0.1)
                GPIO.output(pin5,GPIO.HIGH)
                GPIO.output(pin6,GPIO.LOW)
                time.sleep(0.1)
                GPIO.output(pin5,GPIO.LOW)
                GPIO.output(pin4,GPIO.HIGH)
                time.sleep(0.1)
                GPIO.output(pin4,GPIO.LOW)

                GPIO.output(pin2,GPIO.HIGH)
                time.sleep(0.1)
                GPIO.output(pin3,GPIO.HIGH)
 		GPIO.output(pin2,GPIO.LOW)
                time.sleep(0.1)
                GPIO.output(pin3,GPIO.LOW)
