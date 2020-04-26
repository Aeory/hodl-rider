import os
from dotenv import load_dotenv

load_dotenv()

TIINGO_CONFIG = {
    'api_key': os.environ.get('TIINGO_API_KEY'),
    'session': True
}

RESAMPLE_FREQUENCY = 'daily'

STARTING_ACCELERATION_LINES = 30

SMOOTHING = {
    'type': 'ROLLING_AVERAGE',
    'coefficient': 20
}
