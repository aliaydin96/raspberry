import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

pwmpin = 16

GPIO.setup(pwmpin, GPIO.OUT)

p = GPIO.PWM(pwmpin, 50)

p.start(7.5)
try:
    while True:
        p.ChangeDutyCycle(7.5)
        time.sleep(1)
        p.ChangeDutyCycle(2.5)
        time.sleep(1)
        p.ChangeDutyCycle(12.5)
        time.sleep(1)
except:
    GPIO.cleanup()