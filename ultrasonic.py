#! /usr/bin/env python3
import rospy
import RPi.GPIO as GPIO
import time
from sensor_msgs.msg import Range
from settings import settings
from node import Node


ultrasonic_node = Node("raspberry_ultra_distance")
ultrasonic_node_publisher = "distance_publisher"


TRIGGER_PIN = settings.TRIGGER_PIN
ECHO_PIN = settings.ECHO_PIN

def init_GPIO():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(TRIGGER_PIN, GPIO.OUT)
    GPIO.setup(ECHO_PIN, GPIO.IN)
    GPIO.output(TRIGGER_PIN, GPIO.LOW)
    time.sleep(1)

def calaulate_distance():
    GPIO.output(TRIGGER_PIN, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(TRIGGER_PIN, GPIO.LOW)
    while GPIO.input(ECHO_PIN) == 0:
        pulse_start_time = time.time()
    while GPIO.input(ECHO_PIN) == 1:
        pulse_end_time = time.time()
    pulse_duration = pulse_end_time - pulse_start_time
    return round(pulse_duration * 17150)


def main():
    ultrasonic_node.init_publisher(ultrasonic_node_publisher,"raspberry/data/distance", Range)
    dist = Range()
    dist.min_range = 0
    dist.max_range = 400
    try:
        init_GPIO()
        while not rospy.is_shutdown():
            distance = calaulate_distance()
            dist.range = distance
            ultrasonic_node.publish(ultrasonic_node_publisher ,dist)
            time.sleep(settings.DISTANCE_DELTA_TIME)
    finally:
        GPIO.cleanup()

main()
