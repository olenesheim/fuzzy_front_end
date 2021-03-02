from gpiozero import DistanceSensor
from time import sleep
import numpy as np

if __name__ == "__main__":
    sensor = DistanceSensor(1, 16) #Trig = GPIO1, Echo = GPIO16
    while True:
        print("Distance: ", sensor.distance)
        sleep(1)

        #end