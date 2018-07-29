#import the GPIO and time package
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT,initial = GPIO.HIGH)
# loop through 50 times, on/off for 1 second
for i in range(50):
    GPIO.output(11,True)
    time.sleep(1)
    GPIO.output(11,False)
    time.sleep(1)
GPIO.cleanup()
