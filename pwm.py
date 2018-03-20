import RPi.GPIO as GPIO
import time

pwmpin=18

GPIO.setmode(GPIO.BCM)
GPIO.setup(pwmpin, GPIO.OUT)

p = GPIO.PWM(pwmpin, 100)
p.start(0)

while True:
        for i in range(101):
                p.ChangeDutyCycle(i)

                time.sleep(0.006)
        for i in range(100):
                p.ChangeDutyCycle(100-i)
                time.sleep(0.006)
