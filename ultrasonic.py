from gpiozero import DistanceSensor
from time import sleep
import numpy as np
import RPi.GPIO as GPIO

if __name__ == "__main__":

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(1, GPIO.OUT)

    GPIO.output(1, GPIO.HIGH)
    sleep(3)
    GPIO.output(1, GPIO.LOW)


    GPIO.setup(16, GPIO.IN)

    sensor = DistanceSensor(1, 16) #Trig = GPIO1, Echo = GPIO16
    while True:
        print("Distance: ", sensor.distance)
        sleep(1)

        #end