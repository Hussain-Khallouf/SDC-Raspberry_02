#! /usr/bin/env python3

import cv2 as cv
import rospy
from sensor_msgs.msg import CompressedImage
import numpy as np


rospy.init_node("camera_image")
image_publisher = rospy.Publisher("data/image", CompressedImage, queue_size=1)

cap = cv.VideoCapture(0)
cap.set(cv.CAP_PROP_FRAME_WIDTH,640)
cap.set(cv.CAP_PROP_FRAME_HEIGHT,360)

while not rospy.is_shutdown():
    _, frame = cap.read()
    msg = CompressedImage()
    msg.header.stamp = rospy.Time.now()
    msg.format = "jpeg"
    msg.data = np.array(cv.imencode('.jpg', frame)[1]).tostring()
    image_publisher.publish(msg)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
