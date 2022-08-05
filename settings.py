from json import load
from dotenv import load_dotenv
import os

load_dotenv('.env')


class Settings():
    TRIGGER_PIN = int(os.getenv('ULTRASONIC_TRIGGER_PIN')) 
    ECHO_PIN = int(os.getenv('ULTRASONIC_ECHO_PIN'))
    DISTANCE_DELTA_TIME= float(os.getenv('DISTANCE_DELTA_TIME'))
    IMAGE_WIDTH = int(os.getenv('IMAGE_WIDTH'))
    IMAGE_HEIGHT = int(os.getenv('IMAGE_HEIGHT'))






settings = Settings()