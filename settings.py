from json import load
from dotenv import load_dotenv
import os

load_dotenv('.env')


class Settings():
    TRIGGER_PIN = 8
    ECHO_PIN = 12

    DISTANCE_DELTA_TIME= 0.1
    IMAGE_WIDTH = 640
    IMAGE_HEIGHT = 360






settings = Settings()