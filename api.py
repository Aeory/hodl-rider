from tiingo_client import client as tiingo_client
from models import Track, Point
from dateutil import parser
from export.export_to_json import track_to_json
from datetime import date
import settings


def hodl(ticker: str, start_date: date, end_date: date, config: dict = {}):
    start_date_string = start_date.isoformat() if start_date else ""
    end_date_string = end_date.isoformat() if end_date else ""
    data = tiingo_client.get(start_date_string, end_date_string, ticker)
    start = data[0]
    start_date = parser.parse(start["date"]).date()
    end_date = parser.parse(data[-1]["date"]).date()
    x_scale = config.get("x_scale") or settings.DEFAULT_X_SCALE
    y_scale = config.get("y_scale") or settings.DEFAULT_Y_SCALE
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
