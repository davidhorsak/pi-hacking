import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)


break_width = 0.002
middle_width = 0.00152
deviation    = 0.0012

min_width = middle_width - deviation
max_width = middle_width + deviation

def length(angle):
    return min_width + (angle/180.0) * (max_width - min_width)

while(1):
   for angle in range(0, 180):
        GPIO.output(17, 1)
        l = length(angle)
        print l
        sleep(l)
        GPIO.output(17, 0)
        sleep(break_width)

   for angle in range(0, 180):
        GPIO.output(17, 1)
        l = length(180 - angle)
        print l
        sleep(l)
        GPIO.output(17, 0)
        sleep(break_width)

GPIO.cleanup()
