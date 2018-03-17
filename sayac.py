import RPi.GPIO as GPIO
import time

buton =
led =

GPIO.setmode(GPIO.BOARD)
GPIO.setup(led, GPIO.OUT)
GPIO.setup(buton, GPIO.IN)

GPIO.setup(buton, GPIO.IN, pull_up_down = GPIO.PUD_UP)
def ledyak():
    GPIO.output(led, GPIO.HIGH)

def ledsondur():
    GPIO.output(led, GPIO.LOW)
while True:
    butons = GPIO.input(buton)
    sayac = 0
    if(butons == False):
        sayac+=1
    if sayac%2 == 0:
        ledyak()
    elif sayac%2 == 1:
        ledsondur()
    else:
        pass



