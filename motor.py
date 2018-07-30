import RPi.GPIO as GPIO
from time import sleep
 
GPIO.setmode(GPIO.BOARD)
 
Motor1A = 16
Motor1B = 18
Motor1E = 22
LED_VErt = 7
 
GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)
GPIO.setup(Motor1E,GPIO.OUT)
GPIO.setup(LED_VErt,GPIO.OUT)
 
print "Turning motor on"
GPIO.output(LED_VErt,GPIO.HIGH)
GPIO.output(Motor1A,GPIO.HIGH)
GPIO.output(Motor1B,GPIO.LOW)
GPIO.output(Motor1E,GPIO.HIGH)
 
sleep(2)
 
print "Stopping motor"
GPIO.output(Motor1E,GPIO.LOW)
GPIO.output(LED_VErt,GPIO.LOW)

 
GPIO.cleanup()