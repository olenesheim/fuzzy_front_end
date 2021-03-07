import time
import numpy as np
import RPi.GPIO as GPIO

class DistanceSensor:
    def __init__(self, trig, echo):
        self.trig = trig
        self.echo = echo
        GPIO.setup(trig, GPIO.OUT)
        GPIO.setup(echo, GPIO.IN)
        GPIO.output(trig, False)
        time.sleep(0.5)

def get_distance(sensor):
    GPIO.output(sensor.trig, True)
    time.sleep(0.00001)
    GPIO.output(sensor.trig, False)

    while GPIO.input(sensor.echo) == 0:
        pulse_start = time.time()

    while GPIO.input(sensor.echo) == 1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150
    distance = round(distance, 2)

    return distance


if __name__ == "__main__":

    GPIO.setmode(GPIO.BCM)

    #Trigger = GPIO23, echo = GPIO24
    sensor = DistanceSensor(23, 24)

    distance = get_distance(sensor)

    print("Distance: ", distance, " cm")