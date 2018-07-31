import RPi.GPIO as GPIO
from time import sleep

#test synchro automatique 
 
GPIO.setmode(GPIO.BOARD)
 
#moteur 1
Motor1A = 16
Motor1B = 18
Motor1E = 22

#moteur 2
Motor2A = 11
Motor2B = 40
Motor2E = 15

#servo motor 
servo_pin = 29
duty_cycle = 4

LED_VErt = 7
GPIO.setup(LED_VErt,GPIO.OUT)


GPIO.output(LED_VErt,GPIO.HIGH)
sleep(1)
GPIO.output(LED_VErt,GPIO.LOW)
sleep(2)
 
GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)
GPIO.setup(Motor1E,GPIO.OUT)
GPIO.setup(LED_VErt,GPIO.OUT)

GPIO.setup(Motor2A,GPIO.OUT)
GPIO.setup(Motor2B,GPIO.OUT)
GPIO.setup(Motor2E,GPIO.OUT)

GPIO.setup(servo_pin, GPIO.OUT)

# Create PWM channel on the servo pin with a frequency of 50Hz
pwm_servo = GPIO.PWM(servo_pin, 50)
pwm_servo.start(duty_cycle)

try:
    while True:
        duty_cycle = float(input("Enter Duty Cycle (Left = 5 to Right = 10):"))
        pwm_servo.ChangeDutyCycle(duty_cycle)
            
except KeyboardInterrupt:
    print("CTRL-C: Terminating program.")

    

print "Turning motor on"
GPIO.output(LED_VErt,GPIO.HIGH)
GPIO.output(Motor1A,GPIO.HIGH)
GPIO.output(Motor1B,GPIO.LOW)
GPIO.output(Motor1E,GPIO.HIGH)

GPIO.output(Motor2A,GPIO.HIGH)
GPIO.output(Motor2B,GPIO.LOW)
GPIO.output(Motor2E,GPIO.HIGH)
 
sleep(2)
 
print "Stopping motor"
GPIO.output(Motor1E,GPIO.LOW)
GPIO.output(Motor2E,GPIO.LOW)

GPIO.output(LED_VErt,GPIO.LOW)

sleep(2)

print "Turning motor on, dans l'autre sens"
GPIO.output(LED_VErt,GPIO.HIGH)
GPIO.output(Motor1A,GPIO.LOW)
GPIO.output(Motor1B,GPIO.HIGH)
GPIO.output(Motor1E,GPIO.HIGH)

GPIO.output(Motor2A,GPIO.LOW)
GPIO.output(Motor2B,GPIO.HIGH)
GPIO.output(Motor2E,GPIO.HIGH)

sleep(2) 

print "Stopping motor"
GPIO.output(Motor1E,GPIO.LOW)
GPIO.output(Motor2E,GPIO.LOW)
GPIO.output(LED_VErt,GPIO.LOW)

sleep(2)
GPIO.output(LED_VErt,GPIO.HIGH)
sleep(1)
GPIO.output(LED_VErt,GPIO.LOW)
sleep(2)

 
GPIO.cleanup()