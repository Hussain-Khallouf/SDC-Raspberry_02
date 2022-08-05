import numpy as np
import cv2 as cv


def encode_image(image):
    encoded_image = np.array(cv.imencode(".jpg", image)[1]).tostring()
    return encoded_image