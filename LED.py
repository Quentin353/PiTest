#import the GPIO and time package
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)

GPIO_LED_GREEN  = 17
GPIO_LED_RED    = 4
GPIO_LED_BLUE   = 25

GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_LED_BLUE, GPIO.OUT,initial = GPIO.HIGH)
GPIO.setup(GPIO_LED_RED, GPIO.OUT,initial = GPIO.HIGH)
GPIO.setup(GPIO_LED_GREEN, GPIO.OUT,initial = GPIO.HIGH)

# loop through 10 times, on/off for 1 second
for i in range(5):
    GPIO.output(GPIO_LED_BLUE,True)
    time.sleep(1)
    GPIO.output(GPIO_LED_RED,True)
    time.sleep(1)
    GPIO.output(GPIO_LED_GREEN,True)
    time.sleep(1)
    GPIO.output(GPIO_LED_BLUE,False)
    GPIO.output(GPIO_LED_RED,False)
    GPIO.output(GPIO_LED_GREEN,False)
    time.sleep(1)
    GPIO.output(GPIO_LED_BLUE,True)
    GPIO.output(GPIO_LED_RED,True)
    GPIO.output(GPIO_LED_GREEN,True)
    time.sleep(1)
    GPIO.output(GPIO_LED_BLUE,False)
    GPIO.output(GPIO_LED_RED,False)
    GPIO.output(GPIO_LED_GREEN,False)
    time.sleep(1)
GPIO.cleanup()
