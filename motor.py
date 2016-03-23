import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)


width = 0.0015

while(1):
    GPIO.output(17, 1)
    sleep(width)
    GPIO.output(17, 0)
    sleep(width)

GPIO.cleanup()
