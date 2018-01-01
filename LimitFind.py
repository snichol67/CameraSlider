#!/usr/bin/python
#import Adafruit_MotorHAT, Adafruit_DCMotor, Adafruit_Stepper 
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor, Adafruit_StepperMotor

import time
from time import sleep

import atexit
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN)
GPIO.setup(25, GPIO.IN)
GPIO.setup(12, GPIO.IN)

# create a default object, no changes to I2C address or frequency
mh = Adafruit_MotorHAT()

# recommended for auto-disabling motors on shutdown!
def turnOffMotors():
	mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
	mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
	mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
	mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)

atexit.register(turnOffMotors)

myStepper = mh.getStepper(200, 1)  	# 200 steps/rev, motor port #1
myStepper.setSpeed(70)  		# 30 RPM

if (GPIO.input(23) == True):
    print "Input 23 TRUE!"
else:
    print "Input 23 FALSE!"
if (GPIO.input(25) == True):
    print "Input 25 TRUE"
else:
    print "Input 25 FALSE"


direction = Adafruit_MotorHAT.FORWARD
while (True):
    print("Single coil steps")
    myStepper.step(10, direction,  Adafruit_MotorHAT.INTERLEAVE)

    if (GPIO.input(25) == True):
      print "Changing direction: BACKWARD"
      direction = Adafruit_MotorHAT.BACKWARD

    if (GPIO.input(12) == True):
      print "Changing direction: FORWARD"
      direction = Adafruit_MotorHAT.FORWARD

