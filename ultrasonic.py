#! /usr/bin/env python3
import rospy
import RPi.GPIO as GPIO
import time
from sensor_msgs.msg import Range

# from node import Node

rospy.init_node("raspberry_ultra_distance")
distance_publisher = rospy.Publisher("raspberry/data/distance", Range, queue_size=1)

PIN_TRIGGER = 8
PIN_ECHO = 12

try:
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(PIN_TRIGGER, GPIO.OUT)
    GPIO.setup(PIN_ECHO, GPIO.IN)
    GPIO.output(PIN_TRIGGER, GPIO.LOW)
    time.sleep(1)

    while not rospy.is_shutdown():
        GPIO.output(PIN_TRIGGER, GPIO.HIGH)
        time.sleep(0.00001)
        GPIO.output(PIN_TRIGGER, GPIO.LOW)
        while GPIO.input(PIN_ECHO) == 0:
            pulse_start_time = time.time()
        while GPIO.input(PIN_ECHO) == 1:
            pulse_end_time = time.time()
        pulse_duration = pulse_end_time - pulse_start_time
        distance = round(pulse_duration * 17150)
        dist = Range()
        dist.min_range = 0
        dist.max_range = 400
        dist.range = distance
        #          print(distance)
        distance_publisher.publish(dist)
        time.sleep(0.1)
finally:
    GPIO.cleanup()
