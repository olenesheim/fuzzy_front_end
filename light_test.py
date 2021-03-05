#Lights test

from time import sleep
import numpy as np
import RPi.GPIO as GPIO


if __name__ == "__main__":

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(1, GPIO.OUT)
    GPIO.setup(16, GPIO.OUT)

    GPIO.output(1, GPIO.HIGH)
    sleep(3)
    GPIO.output(1, GPIO.LOW)
    sleep(1)
    GPIO.output(16, GPIO.HIGH)
    sleep(3)
    GPIO.output(16, GPIO.LOW)