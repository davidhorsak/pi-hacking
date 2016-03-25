import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(17, GPIO.OUT)
GPIO.setup(22, GPIO.IN, pull_up_down = GPIO.PUD_IN)

try:
    while True:
        if(GPIO.input(22) == 1):
            GPIO.output(17, 1)
        else:
            GPIO.output(17, 0)
except KeyboardInterrupt:
    GPIO.cleanup()
