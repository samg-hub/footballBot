import RPi.GPIO as GPIO
from consts import *
from time import sleep
def settingup_pins():
    GPIO.setmode(GPIO.BCM)
    #ULTRASONIC
    GPIO.setup(TRIGGER_PIN,GPIO.OUT)
    GPIO.setup(ECHO_PIN,GPIO.IN)
    #DIRVER MOTORS 
    GPIO.setup(RM_IN1,GPIO.OUT)
    pass
GPIO.setmode(GPIO.BCM)
id = RM_IN1
GPIO.setup(id , GPIO.OUT)
GPIO.output(id , True)

sleep(20)
GPIO.cleanup()