import time
import numpy as np
import RPi.GPIO as GPIO


#Ultrasonic test-program
#Takes one measurement of the distance


if __name__ == "__main__":

    GPIO.setmode(GPIO.BCM)

    TRIG = 23
    ECHO = 24

    GPIO.setup(TRIG, GPIO.OUT)
    GPIO.setup(ECHO, GPIO.IN)

    GPIO.output(TRIG, False)
    time.sleep(1)

    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    #test first
    # GPIO.setup(23, GPIO.OUT)
    # GPIO.output(23, GPIO.HIGH)
    # sleep(3)
    # GPIO.output(23, GPIO.LOW)


    while GPIO.input(ECHO) == 0:
        pulse_start = time.time()

    while GPIO.input(ECHO) == 1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start

    distance = pulse_duration * 17150

    distance = round(distance, 2)

    print("Distance: ", distance, " cm")

    GPIO.cleanup()