
import RPi.GPIO as GPIO
import time

GPIO.setwarning(False)
GPIO.setmode(GPIO.BOARD)

trig = 16
echo = 18

GPIO.setup(trig, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)

GPIO.output(trig, False)
time.sleep(1)

GPIO.output(trig, True)
time.sleep(0.00001)
GPIO.output(trig, False)
timestart = time.time()

try:
    while True:

        GPIO.output(TRIG, False)
        print
        "Olculuyor..."
        time.sleep(2)

        GPIO.output(TRIG, True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)

        while GPIO.input(ECHO) == 0:
            pulse_start = time.time()

        while GPIO.input(ECHO) == 1:
            pulse_end = time.time()

        pulse_duration = pulse_end - pulse_start

        distance = pulse_duration * 17150
        distance = round(distance, 2)

        if distance > 2 and distance < 400:
            print"Mesafe:", distance - 0.5, "cm"
        else:
            print"Menzil asildi"

except:
    GPIO.cleanup()

