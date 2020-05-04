import os
from dotenv import load_dotenv
import logging

load_dotenv()

TIINGO_CONFIG = {"api_key": os.environ.get("TIINGO_API_KEY"), "session": True}

RESAMPLE_FREQUENCY = "daily"

STARTING_ACCELERATION_LINES = 10

SMOOTHING = {"type": "ROLLING_AVERAGE", "coefficient": 10}

STARTING_TRACK = True

CREDITS = True

TITLE = True

STARTING_AREA_X = 100
STARTING_AREA_Y = 4

MINIMUM_ACCELERATION_CHANCE = (
    0.2  # As a decimal representing a percentage chance out of 100
)

DEFAULT_X_SCALE = 0.1
DEFAULT_Y_SCALE = -0.4

RECAPTCHA = {
    'site_key': "",
    'secret_key': ""
}

APP_NAME="Hodl Rider"

logging.basicConfig(level=logging.DEBUG)

GOOGLE_ANALYTICS = {
    'id': os.environ.get('GOOGLE_ANALYTICS_ID')
}
