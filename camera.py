#! /usr/bin/env python3

import cv2 as cv
import rospy
from sensor_msgs.msg import CompressedImage
from settings import settings
from utils import encode_image
from node import Node


camera_node = Node('raspberry_camera_node')
camera_node.init_publisher("image_publisher", "raspberry/data/image", CompressedImage)

cap = cv.VideoCapture(0)
cap.set(cv.CAP_PROP_FRAME_WIDTH, settings.IMAGE_WIDTH)
cap.set(cv.CAP_PROP_FRAME_HEIGHT, settings.IMAGE_HEIGHT)

def init_image_msg(encoded_image):
    msg = CompressedImage()
    msg.header.stamp = rospy.Time.now()
    msg.format = "jpeg"
    msg.data = encoded_image


while not rospy.is_shutdown():
    _, frame = cap.read()
    encoded_image = encode_image(frame)
    msg = init_image_msg(encoded_image)
    camera_node.publish('image_publisher', msg)

    if cv.waitKey(1) & 0xFF == ord("q"):
        break


cap.release()
cv.destroyAllWindows()
