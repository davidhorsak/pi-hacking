import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)

diodes = { 17: 1, 18: 0 }


for _ in range(10):
    for key, value in diodes.iteritems():
        new_value = 0 if value == 1 else 1
        GPIO.output(key, new_value)
        diodes[key] = new_value

    sleep(0.5)

GPIO.cleanup()
