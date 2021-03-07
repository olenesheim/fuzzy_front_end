from gpiozero import DistanceSensor
from time import sleep
import numpy as np
import RPi.GPIO as GPIO

if __name__ == "__main__":

    GPIO.setmode(GPIO.BCM)
    #PIO.setup(23, GPIO.OUT)
    #GPIO.setup(24, GPIO.IN)

    sensor = DistanceSensor(23, 24) #Trig = GPIO23, Echo = GPIO24
    while True:
        print("Distance: ", sensor.distance)
        sleep(1)