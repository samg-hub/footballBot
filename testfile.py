import RPi.GPIO as GPIO
import time 


pin1 = 23
pin2 = 24

pin3 = 27
pin4 = 22

ENA = 13
ENB = 12

def forward(power: int = 0.2):
		GPIO.output(pin1, True)
		GPIO.output(pin2, False)
		GPIO.output(pin3, True)
		GPIO.output(pin4, False)
		ena_pwm = GPIO.PWM(ENA,1000)
		enb_pwm = GPIO.PWM(ENB,1000)
		ena_pwm.start(0)
		enb_pwm.start(0)
		ena_pwm.ChangeDutyCycle(70)
		enb_pwm.ChangeDutyCycle(70)
		time.sleep(power)
		GPIO.output(pin1, False)
		GPIO.output(pin2 , False)
		GPIO.output(pin3, False)
		GPIO.output(pin4,False)
		ena_pwm.stop()
		enb_pwm.stop()
def setup_gpios():
    GPIO.setmode(GPIO.BCM)
    #DIRVER MOTORS 
    GPIO.setup(pin1,GPIO.OUT)
    GPIO.setup(pin2,GPIO.OUT)
    GPIO.setup(pin3,GPIO.OUT)
    GPIO.setup(pin4,GPIO.OUT)
    GPIO.setup(ENB,GPIO.OUT)
    GPIO.setup(ENA,GPIO.OUT)
    ##SHOOTER
setup_gpios()
#GPIO.setmode(GPIO.BCM)
forward()
