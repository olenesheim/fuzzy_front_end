#Lights test

from time import sleep
import numpy as np
import RPi.GPIO as GPIO


if __name__ == "__main__":

    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(23, GPIO.OUT)
    GPIO.setup(24, GPIO.OUT)

    GPIO.output(23, GPIO.HIGH)
    sleep(3)
    GPIO.output(23, GPIO.LOW)
    sleep(1)
    GPIO.output(24, GPIO.HIGH)
    sleep(3)
    GPIO.output(24, GPIO.LOW)
