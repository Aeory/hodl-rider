import os
from dotenv import load_dotenv

load_dotenv()

TIINGO_CONFIG = {
    'api_key': os.environ.get('TIINGO_API_KEY'),
    'session': True
}

RESAMPLE_FREQUENCY = 'daily'

STARTING_ACCELERATION_LINES = 10

SMOOTHING = {
    'type': 'ROLLING_AVERAGE',
    'coefficient': 10
}

STARTING_TRACK = True

CREDITS = True

TITLE = True

STARTING_AREA_X = 100
STARTING_AREA_Y = 4

MINIMUM_ACCELERATION_CHANCE = 0.2  # As a decimal representing a percentage chance out of 100