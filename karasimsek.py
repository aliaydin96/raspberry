import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)

led = [35, 37, 33, 31, 29, 32, 36, 38]
for i in range(8):
        GPIO.setup(led[i], GPIO.OUT)
        GPIO.output(led[i],GPIO.LOW)
try:
        while True:
                for i in range(8):
                        GPIO.output(led[i],GPIO.HIGH)
                        time.sleep(0.06)
                        GPIO.output(led[i],GPIO.LOW)
                for i in range(6):
                        GPIO.output(led[6-i],GPIO.HIGH)
                        time.sleep(0.06)
                        GPIO.output(led[6-i],GPIO.LOW)
except KeyboardInterrupt:
        GPIO.cleanup()
