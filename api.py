from tiingo_client import client as tiingo_client
from models import Track, Point
from dateutil import parser
from export.export_to_json import track_to_json
from datetime import date
import settings


def hodl(
        ticker: str,
        start_date: str,
        end_date: str,
        config: dict = {}
):

    data = tiingo_client.get(start_date or None, end_date or None, ticker)
    start = data[0]
    x_scale, y_scale = config.get('x_scale', settings.DEFAULT_X_SCALE), config.get('y_scale', settings.DEFAULT_Y_SCALE)
    track = Track(
        parser.parse(start_date or start['date']).date(),
        parser.parse(end_date or data[-1]['date']).date(),
        ticker,
        [
            Point(
                x=idx + settings.STARTING_AREA_X * x_scale,
                y=day['close'] - start['close'] + settings.STARTING_AREA_Y * y_scale,
                date_recorded=parser.parse(day['date']).date(),
                price=day['close']
            )
            for idx, day in enumerate(data)
        ],
        config
    )
    return track_to_json(track)
