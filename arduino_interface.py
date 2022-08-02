#! /usr/bin/env python3

import serial
from std_msgs.msg import String
from node import Node


speed = 100
angle_step = 2

commands = {
    "stop": "S0",
    "go": f"S{speed}",
    "left": f"I{angle_step}",
    "right": f"D{angle_step}",
}

ArduinoSerial = serial.Serial("/dev/ttyACM0", 9600, timeout=0.1)
node = Node("arduino_interface_node")


def callback(msg: String):
    print(msg.data)
    ArduinoSerial.write(commands[msg.data].encode('utf-8'))


node.init_subscriber("dist_2_arduino", "/engine/commands", String, callback)
node.spin()

# while True:
#     string = input('input speed')
#     ArduinoSerial.write(string.encode('utf-8'))
