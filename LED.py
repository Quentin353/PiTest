#import the GPIO and time package
import RPi.GPIO as GPIO
import time

GPIO_LED_GREEN  = 35
GPIO_LED_RED    = 11
GPIO_LED_BLUE   = 37

GPIO.setmode(GPIO.BOARD)
GPIO.setup(GPIO_LED_BLUE, GPIO.OUT,initial = GPIO.HIGH)
GPIO.setup(GPIO_LED_RED, GPIO.OUT,initial = GPIO.HIGH)
GPIO.setup(GPIO_LED_GREEN, GPIO.OUT,initial = GPIO.HIGH)

# loop through 10 times, on/off for 1 second
for i in range(10):
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
