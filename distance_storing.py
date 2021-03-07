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
    #Returns the distance from the sensor in cm

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


def create_file(filename):
    #Create a new txt-file

    new_file = filename
    file1 = open(new_file, "a")
    file1.close()
    return new_file


def write_to_file(filename, value):
    #Writes the value to the file

    file1 = open(filename, "a")
    writing_value = str(value)
    file1.write(writing_value + "\n")
    file1.close()
    return 0


if __name__ == "__main__":

    GPIO.setmode(GPIO.BCM)

    #Trigger = GPIO23, echo = GPIO24
    sensor = DistanceSensor(23, 24)

    #Create a file
    filename = "distances_test1.txt"
    create_file(filename)

    for i in range(10):
        distance = get_distance(sensor)
        print("Writing distance: ", distance, " to the file ", filename)
        write_to_file(filename, distance)
        time.sleep(1)
