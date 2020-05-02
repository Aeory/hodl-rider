from tiingo_client import client as tiingo_client
from models import Track, Point
from dateutil import parser
from export.export_to_json import track_to_json
from datetime import date
import settings
from copy import deepcopy

DEFAULT_CONFIG = {
    'BTCUSD': {
        'x_scale': 0.1, 'y_scale': -10.0
    },
    'GOOGL': {
        'x_scale': 0.1, 'y_scale': -2.0
    },
    'AAPL': {
        'x_scale': 0.1, 'y_scale': -0.4
    },
    'NFLX': {
        'x_scale': 0.1, 'y_scale': -0.3
    }
}


def hodl(ticker: str, start_date: date, end_date: date, user_config: dict = None):
    user_config = user_config or {}

    config = deepcopy(
        DEFAULT_CONFIG.get(
            ticker,
            {'x_scale': settings.DEFAULT_X_SCALE, 'y_scale': settings.DEFAULT_Y_SCALE}
        )
    )
    for k, v in user_config.items():
        if v is not None:
            config[k] = v

    start_date_string = start_date.isoformat() if start_date else ""
    end_date_string = end_date.isoformat() if end_date else ""
    data = tiingo_client.get(start_date_string, end_date_string, ticker)
    start = data[0]
    start_date = parser.parse(start["date"]).date()
    end_date = parser.parse(data[-1]["date"]).date()

    x_scale = config["x_scale"]
    y_scale = config["y_scale"]

    track = Track(
        start_date,
        end_date,
        ticker,
        [
            Point(
                x=idx + settings.STARTING_AREA_X * x_scale,
                y=day["close"] - start["close"] + settings.STARTING_AREA_Y * y_scale,
                date_recorded=day["date"].split('T')[0],
                price=day["close"],
            )
            for idx, day in enumerate(data)
        ],
        config,
    )
    return track_to_json(track)
